#!/usr/bin/env python3
"""
PHYS 115 - Lab M1, Part A: circle fit to the (Bx, By) data of the phone
magnetometer, to determine the sensor offset (x0, y0) and the horizontal
component B_h of the Earth's magnetic field.

Model:     (Bx - x0)^2 + (By - y0)^2 = B_h^2

Linearization (Kasa method):
           Bx^2 + By^2 = 2 x0 Bx + 2 y0 By + c,   c = B_h^2 - x0^2 - y0^2
i.e. a linear least-squares fit in two variables (Bx, By) plus a constant:
           z = p0*Bx + p1*By + p2,   z = Bx^2 + By^2
with p0 = 2*x0, p1 = 2*y0, p2 = c.

If scipy is installed, the result is refined with a geometric fit
(minimizing the distances of the points from the circle), which does not
have the small systematic bias of the linearized method.

Usage:
  python3 fit_offset_circle.py data.csv
  python3 fit_offset_circle.py data.csv --plot fit.png
  python3 fit_offset_circle.py --demo            (test with simulated data)

Data file format:
  (a) CSV export of phyphox ("Magnetometer" experiment): the x, y (and z)
      magnetic-field columns, in uT, are recognized automatically.
  (b) Plain text/CSV file with columns:  phi  Bx  By  [Bz]
      (e.g. Table 7.1.1), separated by comma, semicolon, tab or space.
      Lines starting with # are ignored.

All output is plain ASCII (uT = microtesla), so it displays correctly in
any terminal.
"""
import argparse
import csv
import sys

import numpy as np


# --------------------------------------------------------------------------
# Reading the data
# --------------------------------------------------------------------------
def read_data(path):
    """Return (Bx, By, Bz or None) in uT."""
    with open(path, encoding='utf-8-sig') as f:
        text = f.read()
    lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith('#')]
    if not lines:
        sys.exit('The file contains no data.')

    # Detect the delimiter
    sample = '\n'.join(lines[:5])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=',;\t ')
        delim = dialect.delimiter
    except csv.Error:
        delim = None

    def split(l):
        return [s.strip().strip('"') for s in (l.split(delim) if delim else l.split())]

    first = split(lines[0])
    has_header = any(not _isnum(s) for s in first if s)
    header = [h.lower() for h in first] if has_header else None
    rows = [split(l) for l in (lines[1:] if has_header else lines)]
    rows = [[_tofloat(s) for s in r if s != ''] for r in rows]
    rows = [r for r in rows if r and all(v is not None for v in r)]
    data = np.array([r for r in rows if len(r) == len(rows[0])], dtype=float)

    ix = iy = iz = None
    if header:
        for i, h in enumerate(header):
            # phyphox headers contain the micro sign; map both variants to 'u'
            hh = h.replace('magnetic field', '').replace('μ', 'u').replace('µ', 'u')
            if ix is None and ('x' in hh and 'time' not in hh and 'abs' not in hh):
                ix = i
            elif iy is None and ('y' in hh and 'abs' not in hh):
                iy = i
            elif iz is None and ('z' in hh and 'abs' not in hh):
                iz = i
    if ix is None or iy is None:
        # No header: phi, Bx, By, [Bz]  or  Bx, By, [Bz]
        ncol = data.shape[1]
        if ncol >= 4:
            ix, iy, iz = 1, 2, 3
        elif ncol == 3:
            # if the first column looks like an increasing angle 0..360 -> phi, Bx, By
            c0 = data[:, 0]
            if np.all(np.diff(c0) > 0) and c0.max() <= 360:
                ix, iy, iz = 1, 2, None
            else:
                ix, iy, iz = 0, 1, 2
        elif ncol == 2:
            ix, iy, iz = 0, 1, None
        else:
            sys.exit('Could not identify the Bx, By columns.')
    Bz = data[:, iz] if iz is not None else None
    return data[:, ix], data[:, iy], Bz


def _isnum(s):
    return _tofloat(s) is not None


def _tofloat(s):
    # accepts a decimal comma (e.g. "12,5") as well as a decimal point
    try:
        return float(s.replace(',', '.')) if s.count(',') == 1 and '.' not in s else float(s)
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Fitting
# --------------------------------------------------------------------------
def fit_linear(Bx, By):
    """Linearized circle fit (Kasa) with uncertainties."""
    N = len(Bx)
    A = np.column_stack([Bx, By, np.ones(N)])      # design matrix
    z = Bx**2 + By**2
    p, rss, rank, _ = np.linalg.lstsq(A, z, rcond=None)
    resid = z - A @ p
    dof = N - 3
    s2 = resid @ resid / dof                        # residual variance
    cov_p = s2 * np.linalg.inv(A.T @ A)             # covariance of (p0, p1, p2)

    x0, y0 = p[0] / 2, p[1] / 2
    r = np.sqrt(p[2] + x0**2 + y0**2)
    # Jacobian of (x0, y0, r) with respect to (p0, p1, p2)
    J = np.array([[0.5, 0, 0],
                  [0, 0.5, 0],
                  [p[0] / (4 * r), p[1] / (4 * r), 1 / (2 * r)]])
    cov = J @ cov_p @ J.T                           # error propagation
    return np.array([x0, y0, r]), cov


def fit_geometric(Bx, By, start):
    """Geometric fit: minimize sum (d_i - r)^2 (requires scipy)."""
    try:
        from scipy.optimize import least_squares
    except ImportError:
        return None, None

    def res(q):
        return np.hypot(Bx - q[0], By - q[1]) - q[2]

    sol = least_squares(res, start)
    N = len(Bx)
    s2 = (sol.fun @ sol.fun) / (N - 3)
    J = sol.jac
    cov = s2 * np.linalg.inv(J.T @ J)
    return sol.x, cov


# --------------------------------------------------------------------------
# Simulated data for testing
# --------------------------------------------------------------------------
def demo_data(seed=1):
    rng = np.random.default_rng(seed)
    Bh, x0, y0, z0, Bv = 28.0, -12.0, 35.0, 14.0, -34.0
    phi = np.radians(np.arange(0, 360, 15))
    noise = 0.5
    Bx = x0 + Bh * np.sin(phi) + rng.normal(0, noise, phi.size)
    By = y0 + Bh * np.cos(phi) + rng.normal(0, noise, phi.size)
    Bz = z0 + Bv + rng.normal(0, noise, phi.size)
    print(f'Simulation: B_h = {Bh} uT, offset = ({x0}, {y0}) uT, noise {noise} uT, N = {phi.size}\n')
    return Bx, By, Bz


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description='Circle fit (B_h and offset) - Lab M1')
    ap.add_argument('file', nargs='?', help='data file (phyphox CSV, or phi Bx By [Bz])')
    ap.add_argument('--plot', metavar='PNG', help='save the plot to a file')
    ap.add_argument('--show', action='store_true', help='show the plot on screen')
    ap.add_argument('--demo', action='store_true', help='test with simulated data')
    a = ap.parse_args()

    if a.demo:
        Bx, By, Bz = demo_data()
    elif a.file:
        Bx, By, Bz = read_data(a.file)
    else:
        ap.error('give a data file or --demo')

    N = len(Bx)
    if N < 4:
        sys.exit('At least 4 points are needed.')

    q, cov = fit_linear(Bx, By)
    e = np.sqrt(np.diag(cov))
    print(f'Number of points: N = {N}')
    print('\n1) Linearized fit:  Bx^2 + By^2 = 2*x0*Bx + 2*y0*By + c')
    print(f'   x0  = {q[0]:8.2f} +/- {e[0]:.2f} uT')
    print(f'   y0  = {q[1]:8.2f} +/- {e[1]:.2f} uT')
    print(f'   B_h = {q[2]:8.2f} +/- {e[2]:.2f} uT')

    qg, covg = fit_geometric(Bx, By, q)
    if qg is not None:
        eg = np.sqrt(np.diag(covg))
        print('\n2) Geometric fit (minimizing the distances from the circle):')
        print(f'   x0  = {qg[0]:8.2f} +/- {eg[0]:.2f} uT')
        print(f'   y0  = {qg[1]:8.2f} +/- {eg[1]:.2f} uT')
        print(f'   B_h = {qg[2]:8.2f} +/- {eg[2]:.2f} uT')
        best, ebest = qg, eg
    else:
        print('\n(scipy is not installed: the geometric fit is skipped.)')
        best, ebest = q, e

    d = np.hypot(Bx - best[0], By - best[1]) - best[2]
    print(f'\n   Standard deviation of the distances from the circle: {d.std(ddof=3):.2f} uT')
    if Bz is not None:
        print(f'   B_z during the rotation: mean {Bz.mean():.2f} uT, '
              f'standard deviation {Bz.std(ddof=1):.2f} uT (should be constant)')

    if a.plot or a.show:
        import matplotlib
        if not a.show:
            matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, (ax, axr) = plt.subplots(1, 2, figsize=(11, 5), gridspec_kw={'width_ratios': [1.3, 1]})
        t = np.linspace(0, 2 * np.pi, 400)
        ax.plot(Bx, By, 'o', ms=5, label='measurements')
        ax.plot(best[0] + best[2] * np.cos(t), best[1] + best[2] * np.sin(t), '-',
                label=f'circle: B$_h$ = {best[2]:.1f} $\\pm$ {ebest[2]:.1f} $\\mu$T')
        ax.plot(best[0], best[1], '+', ms=14, mew=2,
                label=f'offset ({best[0]:.1f}, {best[1]:.1f}) $\\mu$T')
        ax.plot(0, 0, 'kx', ms=8, label='origin')
        ax.set_aspect('equal', adjustable='datalim')
        ax.set_xlabel('B$_x$ ($\\mu$T)')
        ax.set_ylabel('B$_y$ ($\\mu$T)')
        ax.grid(alpha=0.3)
        ax.legend(fontsize=9, loc='upper center', bbox_to_anchor=(0.5, -0.13), ncol=2)
        ax.set_title('Circle fit to (B$_x$, B$_y$)')
        ang = np.degrees(np.arctan2(By - best[1], Bx - best[0]))
        axr.axhline(0, color='k', lw=0.8)
        axr.plot(ang, d, 'o', ms=5)
        axr.set_xlabel('angle about the centre (deg)')
        axr.set_ylabel('distance from the circle ($\\mu$T)')
        axr.grid(alpha=0.3)
        axr.set_title('Residuals')
        fig.tight_layout()
        if a.plot:
            fig.savefig(a.plot, dpi=150)
            print(f'\nPlot saved to {a.plot}')
        if a.show:
            plt.show()


if __name__ == '__main__':
    main()

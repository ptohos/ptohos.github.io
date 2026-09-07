#!/usr/bin/env python3
"""
generic_fit.py
==============

Ena genikis xrisis programma prosarmogis dedomenwn me tyxaia synartisi
Ta dedomena dinontai apo ena ekswteriko txt arxeio to opoio tha prepei
na einai sti morfi

       x   y   y_err   [x_err]

- x_err den einai aparaitio. An einai 0 ii den exei timi gia oles tis grammes
  tou arxeio tote den lambanetai ypopsi kai to zygismeno prosarmogi gia tin
  methodo twn elaxistwn tetragwnwn gineta me tin synartisi toy paketou scipy
  scipy.optimize.curve_fit  (weights = 1/y_err^2).

- An uparxon kapoies mi midenikes times gia to x_err tote i prosarmogi ginetai
  me tin palindromisi orthogwnias apostasis. poy lambanei ypopsi toso to sfalma
  sto y oso kai sto x. 

Grammes pou sto data file ksekinoyn me diaisi # theooroyntai sxolia kai den
lambanotau ypopsi 

Xrisi
-----
Mporeite na allakse to tmima "USER SETTINGS" sto telos toy arxeioy aytou
    1. prosdioriste sto DATA_FILE to arxeio me ta dedomena sas 
    2. oriste ti theoritiki sunartisi pou tha prosarmosete sta dedomena sas
    3. dwste kapoies arxikes ektimiseis gia tis times twn parametrwn tis synartisis sas
Treksete to programma:
    python generic_fit.py
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.odr import ODR, Model, RealData


# ----------------------------------------------------------------------
# 1. Reading the data
# ----------------------------------------------------------------------
def read_data(filename):
    """
    Anagnwsi twn dedomenwn apo to arxeio me stiles: x  y  y_err  [x_err]

    Epistrefei
    ----------
    x, y, y_err, x_err : numpy arrays
        x_err einai enas array me midenika an kapoia stili den einai paroysa 
    """
    raw = np.loadtxt(filename, comments="#")

    if raw.ndim == 1:
        # ena mono dedomeno sto arxeio? 
        raw = raw.reshape(1, -1)

    ncols = raw.shape[1]
    if ncols < 3:
        raise ValueError(
            "Data file must have at least 3 columns: x  y  y_err "
            "(x_err is optional)."
        )

    x = raw[:, 0]
    y = raw[:, 1]
    y_err = raw[:, 2]
    x_err = raw[:, 3] if ncols >= 4 else np.zeros_like(x)

    return x, y, y_err, x_err


# ----------------------------------------------------------------------
# 2. H prosarmogi
# ----------------------------------------------------------------------
def fit_function(func, x, y, y_err, x_err, p0):
    """
    Prosarmozei ti synartisi `func` sta dedomena (x, y) me sfalmata (x_err, y_err).

    Parametroi
    ----------
    func : kaleitai
        H synartisi montelou me func(x, *params) -- paromoios orismos pou yparxei
        stin scipy.optimize.curve_fit, p.x. def line(x, a, b): return a*x + b
    x, y, y_err, x_err : arrays
    p0 : sequence
        Arxiki ektimisi gia tis parametrous tis synartisis

    Returns
    -------
    popt : array
        Best-fit parameters.
    perr : array
        1-sigma errors on the parameters (sqrt of diagonal of covariance).
    pcov : 2D array
        Full covariance matrix of the parameters.
    method : str
        'curve_fit' or 'odr', analoga me to poio modelo xrisimopoiithike.
    """
    has_xerr = np.any(x_err > 0)

    if not has_xerr:
        # ---- to kanoniko zugismeno Least square fit (sfalmata mono sto y) ----
        popt, pcov = curve_fit(
            func, x, y, p0=p0,
            sigma=y_err,
            absolute_sigma=True,   # y_err are true 1-sigma avevaiotita
        )
        perr = np.sqrt(np.diag(pcov))
        return popt, perr, pcov, "curve_fit (y-errors only)"

    else:
        # ---- Orthogonal Distance Regression (sfalmata sto x KAI y) ----
        # ODR wants a function of the form f(params, x), i.e. params first
        def odr_func(params, x):
            return func(x, *params)

        # ODR apotygxanei an to sfalma einai 0; epomenws vazoume ena polu mikro sfalma
        # pososto tou mikroterou mi midenikou sfalmatos etsi wste ta simeia ayta den
        # exoun varos sto x anti na prokaloun provlima sto programma. 
        safe_x_err = np.where(x_err > 0, x_err,
                               np.min(x_err[x_err > 0]) * 1e-6
                               if np.any(x_err > 0) else 1e-12)

        model = Model(odr_func)
        data = RealData(x, y, sx=safe_x_err, sy=y_err)
        odr = ODR(data, model, beta0=p0)
        out = odr.run()

        popt = out.beta
        perr = out.sd_beta
        pcov = out.cov_beta
        return popt, perr, pcov, "odr (x and y errors)"


# ----------------------------------------------------------------------
# 3. Ektupwsi apotelesmatwn
# ----------------------------------------------------------------------
def print_results(popt, perr, pcov, method, param_names=None):
    n = len(popt)
    if param_names is None:
        param_names = [f"p{i}" for i in range(n)]

    print("=" * 60)
    print(f"Fit method used : {method}")
    print("-" * 60)
    print("Best-fit parameters and 1-sigma errors:")
    for name, val, err in zip(param_names, popt, perr):
        print(f"  {name:>10s} = {val: .6g}  +/-  {err:.6g}")

    print("-" * 60)
    print("Covariance matrix:")
    with np.printoptions(precision=4, suppress=False, linewidth=120):
        print(pcov)

    print("-" * 60)
    print("Correlation matrix:")
    diag = np.sqrt(np.diag(pcov))
    corr = pcov / np.outer(diag, diag)
    with np.printoptions(precision=3, suppress=True, linewidth=120):
        print(corr)
    print("=" * 60)


# ----------------------------------------------------------------------
# 4. Epilogi: to grafima twn dedomenwn kai tis prosarmogis
# ----------------------------------------------------------------------
def plot_fit(func, x, y, y_err, x_err, popt, outfile_base="fit_plot",
              formats=("png", "pdf")):
    """
    Kanei to grafima me ta sfalmata mazi me tin kampuli prosarmogis kai 
    to apothukeuei sto disko san .png kai .pdf 

    Parameters
    ----------
    outfile_base : str
        file name without extension, e.g. "fit_plot" ->
        "fit_plot.png" and/or "fit_plot.pdf".
    formats : sequence of str
        Which formats to save. Any subset of ("png", "pdf"), e.g.
        formats=("pdf",) to save only the PDF.
    """
    import matplotlib.pyplot as plt

    xs = np.linspace(np.min(x), np.max(x), 400)
    ys = func(xs, *popt)

    plt.figure(figsize=(7, 5))
    plt.errorbar(
        x, y, yerr=y_err,
        xerr=x_err if np.any(x_err > 0) else None,
        fmt="o", ms=4, capsize=3, label="data"
    )
    plt.plot(xs, ys, "-", label="fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()

    for fmt in formats:
        outfile = f"{outfile_base}.{fmt}"
        plt.savefig(outfile, dpi=150)
        print(f"Plot saved to {outfile}")


# ========================================================================
# Settings tou xristi -- tha prepei na allaksoun analoga me tin periptwsi
# ========================================================================
if __name__ == "__main__":

    # ---- Example model: a simple linear function y = a*x + b ----------
    def linear_model(x, a, b):
        return a * x + b

    DATA_FILE = "example_data.txt"
    MODEL_FUNC = linear_model
    P0 = [1.0, 0.0]                 # initial guess for [a, b]
    PARAM_NAMES = ["a (slope)", "b (intercept)"]

    # --- An den uparxoun data auto to block dimiourgei ena paradeigma
    #     wste to programma na treksei mono tou. Tha prepei na to kanete
    #     commented out ga na treksei to programma sas tou fit. 
    import os
    if not os.path.exists(DATA_FILE):
        rng = np.random.default_rng(42)
        true_a, true_b = 2.5, 1.0
        x_true = np.linspace(0, 10, 20)
        x_err_example = np.full_like(x_true, 0.15)
        y_err_example = np.full_like(x_true, 0.5)

        x_obs = x_true + rng.normal(0, x_err_example)
        y_obs = true_a * x_true + true_b + rng.normal(0, y_err_example)

        with open(DATA_FILE, "w") as f:
            f.write("# x   y   y_err   x_err\n")
            for xi, yi, yei, xei in zip(x_obs, y_obs, y_err_example, x_err_example):
                f.write(f"{xi:.6f}  {yi:.6f}  {yei:.6f}  {xei:.6f}\n")
        print(f"(No data file found -- created synthetic example: {DATA_FILE})\n")

    # ---- Read data --------------------------------------------------
    x, y, y_err, x_err = read_data(DATA_FILE)

    # ---- Fit ----------------------------------------------------------
    popt, perr, pcov, method = fit_function(MODEL_FUNC, x, y, y_err, x_err, P0)

    # ---- Report ---------------------------------------------------
    print_results(popt, perr, pcov, method, PARAM_NAMES)

    # ---- Plot: data (with error bars) + fitted curve ------------------
    plot_fit(MODEL_FUNC, x, y, y_err, x_err, popt)

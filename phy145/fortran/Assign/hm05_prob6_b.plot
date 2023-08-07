set termoption enhanced
set xtic auto
set ytic auto
#
set title 'Period vs Energy - Optimum T_{step} = 3.125x10^{-3}s'
set ylabel 'Period, T (sec)'
set xlabel 'log_{10}(Energy) (Joule)'
unset key
set xrange [-1.6:1.6]
set yrange [1:9]
set xtics nomirror
set ytics nomirror
plot 'period_vs_energy_nonlinear.dat' using 2:3 title ' '
#
set term postscript enhanced color 18
set out 'hm05_prob06_b.ps'
replot
unset out
set terminal X11

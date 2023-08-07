set termoption enhanced
set xtic auto
set ytic auto
#
set title 'Force vs velocity - RK4 - t_{step} = 0.001s '
set ylabel 'Force, F (Nt)'
set xlabel 'Velocity, v (m/s)'
unset key
set xrange [-30:50]
set yrange [-0.35:0.0]
set mytics 5
set xtics nomirror
set ytics nomirror
plot 'stone_rk4.dat' using 3:5 title ' ' with lines
#
set term postscript enhanced color 18
set out 'hm06_prob10.ps'
replot
unset out
set terminal X11

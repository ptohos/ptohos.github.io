set termoption enhanced
set term postscript enhanced color 12
set out 'hm05_prob06_a.ps'
set multiplot
set size 1,1
set xtic auto
set ytic auto
#
set origin 0.0,0.5
set size 0.5,0.5
set title 'Position vs time - T_{step} = 0.05s'
set ylabel 'Position, x (cm)'
set xlabel 'Time (sec)'
set xrange [0:13]
set yrange [-1.3:1.3]
set pointsize 0.5
unset key
plot 'nonlinear_oscil.dat' using 1:2 
#
set origin 0.5,0.5
set size 0.5,0.5
set title '{/Symbol D}E vs time - T_{step} = 0.05s'
set ylabel '{/Symbol D}E  (Joule)'
set xlabel 'Time (sec)'
set xrange [0:13]
set yrange [0:1.4]
set pointsize 0.5
unset key
plot 'nonlinear_oscil.dat' using 1:3
#
set origin 0.0,0.0
set size 0.5, 0.5
set title 'Position vs time - Optimum T_{step} = 3.125x10^{-3}s'
set ylabel 'Position, x (cm)'
set xlabel 'Time (sec)'
set xrange [0:13]
set yrange [-1.:1.]
set pointsize 0.5
unset key
plot 'nonlinear_oscil_opt.dat' using 1:2
#
set origin 0.5,0.0
set size 0.5, 0.5
set title '{/Symbol D}E vs time - Optimum T_{step} = 3.125x10^{-3}s'
set ylabel '{/Symbol D}E  (Joule)'
set xlabel 'Time (sec)'
set xrange [0:13]
set yrange [0:0.05]
set pointsize 0.5
unset key
plot 'nonlinear_oscil_opt.dat' using 1:3
#
unset multiplot
unset out
set terminal X11

set termoption enhanced
set xtic auto
set ytic auto
#
set title 'Polyonumo Legendre 8-is taksis - vima dx = 0.05'
set ylabel 'P(L=8,x)'
set xlabel 'x'
unset key
set xrange [-1.05:1.05]
set yrange [-0.5:1.05]
set mytics 5
set xtics nomirror
set ytics nomirror
plot 'Legendre.dat' using 1:2 title ' ' with p 
#
set term postscript enhanced color 18
set out 'hm05_prob3.ps'
replot
unset out
set terminal X11

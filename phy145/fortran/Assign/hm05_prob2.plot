set termoption enhanced
set term X11 enhanced
set title 'Talantwsi me aposvesi'
set ylabel 'Position x(m)'
set xlabel 'Time, t(s)'
set xrange [0:25]
set yrange [-6:6]
set xtic auto
set ytic auto
set size 0.8,0.8
plot 'hm05_prob2.dat' using 1:2 title 'Euler' with p,\
     'hm05_prob2.dat' using 1:4 title 'analytiki' with lines lt 2 lc 2,\
     'hm05_prob2.dat' using 1:5 title 'velocity-Verlet' with p
set term postscript enhanced color 18
set out 'hm05_prob2.ps'
replot
set terminal X11

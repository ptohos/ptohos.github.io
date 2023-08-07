set termoption enhanced
set term X11 enhanced
set title 'Kinisi Podilati'
set ylabel 'Velocity u(m/s)'
set xlabel 'Time, t(s)'
set xrange [0:30]
set yrange [0:20]
set xtic auto
set ytic auto
set size 0.8,0.8
plot 'bicycle.dat' using 1:2 title 'C_{air}=0.0' with lines lt 1 lc 2 ,\
     'bicycle.dat' using 1:3 title 'C_{air}=0.5' with lines lt 2 lc 4
set term postscript enhanced color 18
set out 'hm05_prob1.ps'
replot
set terminal X11

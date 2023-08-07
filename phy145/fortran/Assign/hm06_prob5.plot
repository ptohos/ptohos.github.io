set termoption enhanced
set xtic auto
set ytic auto
#
set title 'Monte Carlo method for the radioactive decay of two nuclei'
set ylabel 'Number of nuclei, N'
set xlabel 'Time, t(sec)'
set xrange [0:1000]
set yrange [0:1000]
set mytics 5
set mxtics 5
set xtics nomirror
set ytics nomirror
set pointsize 0.5
plot 'radioactive_decay.dat' u 1:3 title 'N_X MC method - {/Symbol t}_X=100s' w p pt 1,\
    'radioactive_decay.dat' u 1:2 title 'N_X Analytiki' w lines lt 1 lc 2,\
    'radioactive_decay.dat' u 1:5 title 'N_Y MC method - {/Symbol t}_Y=500s' w p pt 2,\
    'radioactive_decay.dat' u 1:4 title 'N_Y Analytiki' w lines lt 1 lc 1
#
set term postscript enhanced color 18
set out 'hm06_prob5.ps'
replot
unset out
set terminal X11

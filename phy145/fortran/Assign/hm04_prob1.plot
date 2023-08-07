set termoption enhanced
set term X11 enhanced
set title 'Eksartisi tis methodou Euler apo to megethos tou vimatos'
set ylabel 'Temperature, {/Symbol Q} (K)'
set xlabel 'Xroniko vima, dt (sec)'
set xrange [0:500]  
set yrange [-1200:800]
set xtic (0,100,200,300,400,500)        
set ytic (-1200,-800,-400,0,400,800)
set size 0.8,0.8
unset key
plot 'hm04_prob1.dat' using 1:2 w linespoints lt -1 lc 3 pt 6
set term postscript enhanced color 18
set out 'hm04_prob1.ps'
replot
set terminal X11

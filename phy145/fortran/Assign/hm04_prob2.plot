set termoption enhanced
set term postscript enhanced color 18
set out 'hm04_prob2.ps'
set multiplot
set size 1,1
set xtic auto
set ytic auto
#
set origin 0,0.5
set size 1, 0.5
set title 'Population growth - N_0 = 10, a = 10, b=3, T_{step}=0.001'
set ylabel 'Population, N'
set xlabel 'Time, t (months)'
set xrange [0:10]
set yrange [0:11]
set pointsize 0.6
plot 'hm04_prob2_case1.dat' using 1:2 title 'Mid point:' with points pt 6, \
     'hm04_prob2_case1.dat' using 1:3 title 'Theory:' with lines lt 1     
#
set origin 0,0
set size 1, 0.5
set title 'Population growth - N_0 = 1000, a = 10, b=0.01, T_{step}=0.001'
set ylabel 'Population, N'
set xlabel 'Time, t (months)'
set xrange [0:10]
set yrange [800:1100]
set pointsize 0.6
plot 'hm04_prob2_case2.dat' using 1:2 title 'Mid point:' with points pt 6, \
     'hm04_prob2_case2.dat' using 1:3 title 'Theory:' with lines lt 1     
#
unset multiplot
unset out
set terminal X11

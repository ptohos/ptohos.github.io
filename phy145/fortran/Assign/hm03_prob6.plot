set termoption enhanced
set term X11 enhanced
set title 'Fourier Results'
set ylabel 'Amplitude'
set xlabel 'Phase (rad)'
set xrange [-pi/18:pi+pi/18]  # -10 - 190 moires
set yrange [-0.1:1.8]
set xtic auto
set ytic auto
set size 0.8,0.8
plot 'fourier.dat' using 1:2 title 'f(x)'       with lines 1,\
     'fourier.dat' using 1:3 title 'f_{1}(x)'   with lines 2,\
     'fourier.dat' using 1:4 title 'f_{5}(x)'   with lines 3,\
     'fourier.dat' using 1:5 title 'f_{10}(x)'  with lines 4,\
     'fourier.dat' using 1:6 title 'f_{100}(x)' with lines 5
set term postscript enhanced color 18
set out 'hm03_prob06.ps'
replot
set terminal X11

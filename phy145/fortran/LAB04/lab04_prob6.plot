#
# Plot the frequency data kai ena paradeigma apo fit
#
set termoption enhanced
set term X11 enhanced
set title 'Frequency results with a fit'
set ylabel 'Number of events'
set xlabel 'Numbers'
set xrange [0:31]  
set yrange [0:200]
set xtic auto
set ytic auto
set size 0.8,0.8
#
f(x) = norm*exp(-(x-mean)**2/(2.*sigma)**2) # fit function - gaussian
norm = 162 ; mean = 14.9 ; sigma = 3.45  # arxikes times gia fit functions 
#
fit f(x) 'frequency.dat' using 1:2 via norm, mean, sigma 
plot 'frequency.dat' using 1:2 title 'Data: ' with points 3,\
      norm*exp(-(x-mean)**2/(2.*sigma)**2) title 'Gaussian-fit:' with lines 1
set term postscript enhanced color 18
set out 'frequency.ps'
replot
set out            # reset the output file name
set terminal X11

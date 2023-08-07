#
# Plot the function and 
# the program output
#
set termoption enhanced
set term X11 enhanced
set title 'Function - Points and Function'
set ylabel 'y'
set xlabel 'x'
set xrange [-20.2:20.2]  
set yrange [0:450]
set xtic auto
set ytic auto
set size 0.9,0.9
#
f(x) = x**2+2*x+1
plot 'function.dat' using 1:2 title 'Program output: ' with points 3,\
      f(x) title 'F(x)=x^{2}+2x+1:' with lines 1
set term postscript enhanced color 18
set out 'function.ps'
replot
set out            # reset the output file name
set terminal X11

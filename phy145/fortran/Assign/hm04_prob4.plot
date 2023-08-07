set termoption enhanced
set term postscript enhanced color 18
set out 'hm04_prob4.ps'
set multiplot
set size 1,1
set xtic auto
set ytic auto
unset hidden3d
#
set origin 0, 0
set size 0.6, 1
set notitle 
set ylabel 'y-axis' offset +1
set xlabel 'x-axis' offset -1
set zlabel 'Potential V(x,y)' offset -2 rotate by 90
unset key
set contour 
set cntrparam levels 10
set xrange [0:101]
set yrange [0:101]
set xtics (0,20,40,60,80,100)
set ytics (0,20,40,60,80,100)
set view 65,50
splot 'hm04_prob4_trac.dat' w lines
unset label
#
set origin 0.5, 0.0
set size 0.6, 1.0
set notitle
unset key
set ylabel 'y-axis'
set xlabel 'x-axis'
set xrange [0:101]
set yrange [0:101]
set xtics (0,20,40,60,80,100)
set ytics (0,20,40,60,80,100)
unset zlabel
unset surface
set contour base
set cntrparam bspline
set cntrparam levels 10
set view map
splot 'hm04_prob4_trac.dat' w lines
unset multiplot
unset out
set terminal X11
quit
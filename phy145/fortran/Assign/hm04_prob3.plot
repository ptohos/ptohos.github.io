set termoption enhanced
set term postscript enhanced color 18
set out 'hm04_prob3.ps'
set multiplot
set size 1,1
set xtic auto
set ytic auto
#
set origin 0,0.5
set size 0.38, 0.5
set notitle
set ylabel 'Height, h(m)'  offset 2
set xlabel 'Time, t (sec)'
set label 'm_1=m_2=1kg' at 5, 3.8
set xrange [0:30]
set yrange [0:3.5]
set nokey
plot 'hm04_prob3_case1.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case1.dat' using 1:3 w line lc 3 
unset label
#
set origin 0.33,0.5
set notitle 
set size 0.38, 0.5
set ylabel 'Height, h(m)' offset 2
set xlabel 'Time, t (sec)'
set xrange [31:60]
set yrange [0:3.5]
set nokey
plot 'hm04_prob3_case1.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case1.dat' using 1:3 w line lc 3 
#
set origin 0.67,0.5
set size 0.38, 0.5
set notitle
set ylabel 'Height, h(m)' offset 2
set xlabel 'Time, t (sec)'
set xrange [61:100]
set yrange [0:3.5]
set nokey
plot 'hm04_prob3_case1.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case1.dat' using 1:3 w line lc 3 
#
set origin 0,0
set size 0.38, 0.5
set notitle 
set ylabel 'Height, h(m)' offset 2
set xlabel 'Time, t (sec)'
set label 'm_1=2kgr m_2=1kg' at 5, 4.8
set xrange [0:30]
set yrange [0:4.5]
set nokey
plot 'hm04_prob3_case2.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case2.dat' using 1:3 w line lc 3 
unset label
#
set origin 0.33,0
set size 0.38, 0.5
set notitle
set ylabel 'Height, h(m)' offset 2
set xlabel 'Time, t (sec)'
set xrange [31:60]
set yrange [0:4.5]
set nokey
plot 'hm04_prob3_case2.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case2.dat' using 1:3 w line lc 3 
#
set origin 0.67,0
set size 0.38, 0.5
set notitle
set ylabel 'Height, h(m)' offset 2
set xlabel 'Time, t (sec)'
set xrange [61:100]
set yrange [0:4.5]
set nokey
plot 'hm04_prob3_case2.dat' using 1:2 w line lc 2, \
     'hm04_prob3_case2.dat' using 1:3 w line lc 3 

#
unset multiplot
unset out
set terminal X11

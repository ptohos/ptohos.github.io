# H elleipsi grafetai se parametriki morfi
# x=sqrt(25)*cos(t) y=sqrt(16)*sin(t) me t sto diastima [0,2pi]
#
set term postscript
set out 'hm03_prob8.ps'
set parametric
set dummy t
x1(t) = t
g(x)  = 0.85844563*(x+8) - 1
plot [-8:5] [-8:5] 5*cos(t),4*sin(t) w l title 'ellipse:x^2/25+y^2/16=1',\
                   x1(t), g(x1(t)) title 'efaptomeni:y(x)=0.85844563*(x+8)-1'
exit

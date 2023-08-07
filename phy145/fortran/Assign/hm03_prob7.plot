set term postscript
set out 'hm03_prob07.ps'
f(x) = 4*exp(-2*x)
g(x) = 0.5*x*x
plot [-3.0:2.0] [-1:10] f(x) title '4*exp(-2*x)', g(x) title '0.5*x^2'
exit
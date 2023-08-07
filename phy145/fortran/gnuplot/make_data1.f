c============================
      program make_data1
c============================
      implicit none
      integer n, i
      real step, pi
      real x, x_low, x_max

      pi = acos(-1.)
      n = 100
      x_low = 0.
      x_max = 2.*pi

      step = (x_max - x_low)/n

      open(unit=20,file='data1.dat',status='unknown',
     &     form='formatted',err=30)
      do I = 1, n+1
         x = (I-1)*step
         write(20,10)x,sin(x),0.5*cos(2.*x),sin(x)*exp(-x*x/5.),
     &              0.1*tan(2*x)
      enddo
      goto 40
 10   format(1x,f9.6,2x,f10.7,2x,f10.7,2x,f10.7,2x,f10.6)
 30   print *,'Error opening file data1.dat'
 40   continue
      close(20)
      end

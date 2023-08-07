c============================
      program make_data4
c============================
      implicit none
      integer n, i, j
      real*8 xmax
      real*8 x, y, z
      real*8 func

      n    = 100
      xmax = 10.

      open(unit=20,file='data4.dat',status='unknown',
     &     form='formatted',err=30)

      do I = 0, n
         x = (i*xmax)/n
         do J = 0, n
            y = (j*xmax)/n
            z = func(x,y)
            write(20,10)x,y,z
         enddo
      enddo
      goto 40
 10   format(1x,f10.7,2x,f10.7,2x,f10.7)
 30   print *,'Error opening file data2.dat'
 40   continue
      close(20)
      end

      double precision function func(x,y)
      implicit none
      real*8 x, y

      func = sin(x)*cos(x*y/10.)
      return
      end

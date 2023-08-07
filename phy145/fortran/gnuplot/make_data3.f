c============================
      program make_data3
c============================
      implicit none
      integer n, i, iseed
      real scale, xmin, xmax, step
      real x, y, dy_down, dy_up

      iseed = 12345
      call srand(iseed)   ! Arxi tis akolouthias pseudo-tuxaiwn arithmwn

      n = 1000
      scale = 0.1
      xmin = 0.0
      xmax = 10.0
      step = (xmax-xmin)/n

      open(unit=20,file='data3.dat',status='unknown',
     &     form='formatted',err=30)
      do I = 1, n+1
         x = (I-1)*step
         y = sin(x)
         dy_down = y - rand() * scale  
         dy_up   = y + rand() * scale
         write(20,10)x, y, dy_down, dy_up
      enddo
      goto 40
 10   format(1x,f7.4,2x,f10.7,2x,f10.7,2x,f10.7)
 30   print *,'Error opening file data3.dat'
 40   continue
      close(20)
      end

c============================
      program make_data2
c============================
      implicit none
      integer n, i, iseed
      real scale
      real x, y

      iseed = 12345
      call srand(iseed)   ! Arxi tis akolouthias pseudo-tuxaiwn arithmwn

      n = 5000
      scale = 10.0

      open(unit=20,file='data2.dat',status='unknown',
     &     form='formatted',err=30)
      do I = 1, n
         x = rand() * scale   ! Tyxaioi arithmoi pol/zmenoi me kapoia klimaka
         y = rand() * scale   ! Oi arithmoi tha einai sto diastima[0,10]
         write(20,10)x,y
      enddo
      goto 40
 10   format(1x,f10.7,2x,f10.7)
 30   print *,'Error opening file data2.dat'
 40   continue
      close(20)
      end

c=================================
      program mc_maximum
c=================================
c... Eyresi megistou synartisis 
c... me ti methodo Monte Carlo
c... H methodos pou akoloytheitai
c... einai idia me ayti tou 
c... programmatos min_mc sto 
c... ergastirio. 
c... Ypologizoume ti timi tis 
c... sunartisis se tuxaia simeia
c... tis aneksartitis timis x
c... sto diastima [A,B] pou mas
c... endiaferei. 
c... Apo tis epanalipseis kratame
c... pantote tin megisti timi 
c... pou briskoume
c=================================
      implicit none
      integer  iseed
      integer  i, j, n
      real     f1max, f2max
      real     x, x1max, x2max
      real     y, ymax
      real     x1low, x1up
      real     x2low, x2up
      real     ylow, yup
      real     F1, F2          ! Oi duo sunartiseis tis askisis 

      iseed = 123456
      call srand(iseed)

      print *,'Dwste to katw kai panw orio tou x tis 1is synartisis'
      read *, x1low, x1up
      print *,'Dwste to katw kai panw orio tou x tis 2is synartisis'
      read *, x2low, x2up
      print *,'Dwste to katw kai panw orio tou y tis 2is synartisis'
      read *, ylow, yup

      write(6,19)
      do I = 1, 8
         f1max = -9.0E9        ! arxiko megisto - mia mikri timi
         f2max = -9.0E9        
         N = 10**I             ! Arithmos prospatheiwn
         Do J = 1, N           ! Ayto einai to vasiko loop

c...Ypologismos tis 1-is synartisis
            x = x1low + (x1up - x1low)*rand()   ! x1 sto diastima [x1low,x1up]

            if (F1(x).gt.f1max) then   ! Brikame neo megisto 
               f1max  = F1(x)
               x1max  = x 
            endif

c... Ypologismos tis 2-is synartisis
            x = x2low + (x2up - x2low)*rand()   ! x2 tis 2-is sunartisis
            y = ylow + (yup - ylow)*rand()      ! y tis 2-is synartisis
            if (F2(x,y).gt.f2max) then
               f2max = F2(x,y)
               x2max = x
               ymax  = y
            endif
         enddo
         write(6,20)N,x1max,f1max,x2max,ymax,f2max
      enddo
 19   Format(3x,'Tries',9x,'F=x^2exp(-x)',9x,'F=y-x-2x^2-2xy-y^2',/,
     &       13x,'xmax',7x,'Fmax',7x,'xmax',7x,'ymax',7x,'Fmax')
 20   Format(1x,I9,5(2x,F9.6))
      end

c=================================
      real function f1(x)
c=================================
      implicit none
      real x

      f1 = x**2*exp(-x)
      return
      end

c=================================
      real function f2(x,y)
c=================================
      implicit none
      real x, y

      f2 = y - x - 2*x**2 - 2*x*y - y**2
      return
      end

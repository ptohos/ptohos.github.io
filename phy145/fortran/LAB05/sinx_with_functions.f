c============================
      program sinx_series
c============================
      implicit none
      Integer i, j, k, yesno
      Real*8 pi, twopi
      Real*8 x, x_inp, term, sum
      Real*8 fact, numerator
      Real*8 epsi
c
      Real*8 factorial, xcalc     ! Dilwsi synartisewn
c
      Print *,'Calculation of sin(x) from a series'
 50   continue
      Print *,'Dwste tin timi tou x in rads'
      Read *, x_inp
      Print *,'Dwste tin epithymiti akriveia tou athroismatos'
      Read *,epsi

      x = xcalc(x_inp)     ! Ypologismos toy upoloipou tis diairesis me 2pi
                           ! me xrisi sunartisis
      sum = 0.d0
      term = x
      I = 0
      do while (abs(term).ge.epsi)
         sum = sum + term 
         I = I + 1
         J = 2*I+1
         fact = factorial(J)           ! Ypologismos paragontikou me sunartisi
         numerator = (-1.d0)**i * x**j ! O arithmitis me to prosimo
         term = numerator/fact
      enddo
      write(6,10)
      write(6,11)x_inp,sum,sin(x_inp)
 10   format(11x,'Apotelesma tis seiras',/,46('*'))
 11   format(1x,'Gia x = ',F7.3,1x,'Sum = ',F9.6,1x,'kai sin(x) =',f9.6)
c
      print *
      print *,"Tha thelate na eksetasete alli timi [0:yes]?"
      read *,yesno
      if (yesno.eq.0) goto 50
      end
      
c=================================================
      double precision function xcalc(angle)
c=================================================
      implicit none
      real*8 angle
      real*8 pi, twopi, x

      pi = acos(-1.0)
      twopi = 2.0d0*pi
      x = angle - INT(angle/twopi)*twopi
      xcalc = x
      return
      end
c=================================================

c=================================================
      double precision function factorial(number)
c=================================================
c Ypologismos paragontikou enos akeraiou 
c arithmou number se dipli akriveia
c=================================================
      implicit none
      integer  number, j

      factorial = 1.d0         ! Dwsame timi sti synartisi opws tha eprepe
      if (number .lt. 0) then 
         print *,'Paragontiko arnitikou arithmou'
         print *,'Stop the program'
         stop
      endif
      do J = 1, Number
         factorial = factorial * J
      enddo
      return
      end
c================================================

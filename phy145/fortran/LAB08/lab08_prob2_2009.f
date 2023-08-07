c==============================
      program derivative
c==============================
c
c H diaforiki eksiswsi einai:
c y' = y^2 + 1 => dy/(y^2+1)=1
c opote arc(tan(y)) = x =>
c        y_theory = tan(x)
c 
c==============================
      implicit none
      real y_calc, y_theory
      real x, dx, deriv
      real xmin, xmax
      character*3,yesno
c
      print *,'Dwse to xmin kai xmax'
      read*,xmin,xmax
 10   print *,'Dwse to vima dx'
      read*,dx
c
      x = xmin
      y_calc = 0.
 15   if (x.gt.xmax) goto 25
c      do while (x.le.xmax)
         y_theory = tan(x)
         write(6,20)x, y_theory, y_calc
c
         deriv  = y_calc**2 + 1.
         y_calc = y_calc + deriv * dx
         x = x + dx
         goto 15
c      enddo
 25      print *,' Ypologismo me allo vima?'
      read *,yesno
      if (yesno(1:1).eq.'y'.or.yesno(1:1).eq.'Y') goto 10
 20   format(1x,f7.5,2(2x,f6.4))
      end

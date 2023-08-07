c=====================================
      program trigonometry
c=====================================
      implicit none
      integer i, j, nsteps
      real*8   pi, twopi
      real*8   frac, step
      real*8   low_limit, up_limit, angle


      print *,'Dwste to katwtero orio [rads]'
      read *, low_limit
      print *,'Dwste to anwteto orio [arithmos pol/sio tou pi]'
      read *, up_limit
      print *,'Dwste to klasma tou pi gia tin allagi gwnias '
      read *, frac

      pi = acos(-1.0)
      twopi  = 2.*pi
      up_limit = up_limit * pi
      step   = pi/frac
c==========================================
c Ta akoloutha einai paradeigma tis xrisis
c tis entolis format gia na grapsoume to 
c trigwnometriko pinaka stoixismeno
c==========================================
      angle = low_limit
      i = 0
      do while (angle.le.up_limit)
         i = i + 1
         if (i.eq.1) then 
            write(6,20)
            write(6,21)'x','sin(x)','cos(x)'
         endif
         write(6,22)angle, sin(angle), cos(angle)
         angle = angle + step
      enddo
 20   format(2x,11('='),1x,'4os tropos',1x,11('='))
 21   format(1x,a5,7x,a7,4x,a7)
 22   format(1x,f9.6,2x,f9.6,2x,f9.6)
      end

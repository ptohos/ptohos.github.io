c=========================
      program functc
c=========================
c xrisi statement function
c=========================
      real    y, x, z
      integer j

      do j = 1, 4
         x = (j-1)
         z=y(x)
         write(6,10)x,z
      enddo
 10   format(1x,' Gia x=',f2.0,1x,' y(x) = ',1x, f2.0)
      end

c===========================
      real function y(x_inp)
c===========================
      implicit none
      real  x_inp

      y = x_inp**2 - x_inp
      return
      end

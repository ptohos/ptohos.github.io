      program eulersimpson
c==================================
c Apo tin stigmi pou mas dinetai to 
c oloklirwma {6x^3*dx mporoume na to
c grapsoume sa na eina i lusi mias 
c diaforikis eksiswsis dy/dx = 6x^3
c me arxiki sunthiki y(x=5) = 0
c H timi tis y(x=8) tha dwsei tin
c timi tou oloklirwmatos gia oria 
c oloklirwsis apo 5 ews 8. 
c===================================
      implicit none 
      integer istep, nx
      real    lowlim, uplim
      real    x, dx, dydx
      real    y, y0, sum
      real    f1, f2, f3
      real    result, anal
      real    myfunc


 5    print *,'Dwste to katwtero kai anwtero orio oloklirwsis'
      read *, lowlim, uplim
      print *,'Dwste to vima dx'
      read *, dx
c
      nx = int((uplim-lowlim)/dx)
      if (mod(nx,2).ne.0) then 
         print *,'Den exete artio arithmo diastimatw'
         print *,'H methodos Simpson den mporei na efarmostei'
         print *,'Tha prepei na dwsete diaforetiki timi tou dx'
         print *,'i ta oria oloklirwsis einai lathos'
         goto 5
      endif
      anal = 3./2.*(uplim**4 - lowlim**4)
c...
c... Euler
c... =====
      x  = lowlim
      y0 = 0
      y  = y0
      do istep = 1, nx
         dydx = myfunc(x)
         y    = y + dydx*dx
         x    = x + dx
      enddo
      result = y - y0
      Write(6,10)lowlim, uplim, result, anal
 10   Format(1x,70('='),/,20x,'Apotelesma oloklirwsis me Euler',/,
     &       1x,'To oloklirwma 6x^3*dx me oria oloklirwsis apo ',f2.0,
     &       1x,'ws',1x,f2.0,1x,'einai ',f8.3,/,
     &       1x,'H analytiki timi tou oloklirwmatos einai: ',F8.3,/,
     &       1x,70('='))
c...
c... Simpson
c... =======
      sum = 0.
      do istep = 1, nx-1, 2
         x   = lowlim + (istep-1)*dx
         f1  = myfunc(x)
         x   = lowlim + istep*dx
         f2  = myfunc(x)
         x   = lowlim + (istep+1)*dx
         f3  = myfunc(x)
         sum = sum + f1 + 4*f2 + f3
      enddo
      result = sum * dx/3.
      Write(6,20)lowlim, uplim, result, anal
 20   Format(1x,70('='),/,20x,'Apotelesma oloklirwsis me Simpson',/,
     &       1x,'To oloklirwma 6x^3*dx me oria oloklirwsis apo ',f2.0,
     &       1x,'ws',1x,f2.0,1x,'einai ',f8.3,1x,/,
     &       1x,'H analytiki timi tou oloklirwmatos einai: ',F8.3,/,
     &       1x,70('='))
      end

c===================================
      real function myfunc(x)
c===================================
c H oloklirwtea sunartisi
c===================================
      implicit none
      real x
      myfunc = 6*x**3
      return
      end

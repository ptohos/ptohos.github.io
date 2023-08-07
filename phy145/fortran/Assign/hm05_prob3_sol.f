c==========================
      program problem
c==========================
c Oi rizes einai: 
c -0.960290   0.960290
c -0.796666   0.796666
c -0.525532   0.525532
c -0.183435   0.183435
c==========================
      implicit none
      integer iroot, mxroot, istep, nx
      parameter(mxroot=4)

      real*8 x0, xlow, xhi
      real*8 x, dx, xprev
      real*8 y, yprev, root
      real*8 precision
      real*8 legendre
      real*8 newton

      print *,'Dwste tin arxiki timi tou x'
      read *, x0
      print *,'Dwste to diastima twn timwn tou x [xlow,xhi]'
      read *, xlow,xhi
      print *,'Dwste to vima metavolis tou x'
      read *, dx
      print *,'Dwste tin akriveia upologismou twn rizwn'
      read *, precision

      open(unit=10,file='Legendre.dat',status='unknown')
      open(unit=20,file='LegendreRoots.dat',status='unknown')
      x = x0
      y = legendre(x)
      iroot = 0
      nx = INT((xhi-xlow)/dx)+1
      do istep = 1, nx
         xprev = x
         yprev = y
         write(10,10)x,y
         x = x0+istep*dx
         y = legendre(x)
         if (yprev*y.lt.0. .and. x.le.0) then   ! H synartisi allazei prosimo
            root = Newton(xprev,x,legendre,precision)
            iroot = iroot+1
            if (iroot.gt.mxroot) then 
               print*,'Polles rizes poluwnumou'
               iroot = mxroot
            endif
            write(20,20)root,abs(root)
         endif
      enddo
 10   format(1x,F6.3,3x,F6.3)
 20   format(1x,F9.6,3x,F8.6)
      end

c=================================
      real*8 function fact(inp)
c=================================
      implicit none
      integer j
      integer inp

      fact = 1.0D0
      if (inp.lt.0) then
         print*,'Lathos input integer gia ypologismo paragontikou'
         print*,'O akeraios einai ',inp
         fact = -1d0
         goto 10
      endif
      do j = 1, inp
         fact = fact*j
      enddo
 10   return
      end

c======================================
      real*8 function legendre(x)
c======================================
      implicit none
      integer iord, r
      integer LegOrd
      real*8    x, pros
      real*8    a, a1, sum
      real*8    p1, p2, p3
      real*8    fact
      
      LegOrd = 8
      a   = 1./2.**LegOrd
      sum = 0.0
      do r = 0, LegOrd/2
         a1 = fact(2*(LegOrd-r))
         p1 = fact(r)
         p2 = fact(LegOrd-r)
         p3 = fact(LegOrd-2*r)
         if (mod(r,2).eq.0) then
            pros = 1.
         else
            pros = -1.
         endif
         sum = sum + pros*x**(LegOrd-2*r)*a1/(p1*p2*p3)
      enddo
      legendre = sum*a
      return
      end

c===================================================
      real*8 function newton(x1,x2,funct,epsilon)
c===================================================
      implicit none
      real*8 x1, y1
      real*8 x2, y2
      real*8 x3, y3
      real*8 xx1, xx2
      real*8 epsilon
      real*8 funct        ! Ayti einai i synartisi legendre tin opoia pername 
                        ! san orisma stin synartisi newton.
      logical stay

      xx1 = x1          ! Antikatastasi se alles metavlites gia na min 
      xx2 = x2          ! allaksoume tis times tou x1 kai x2 pou xrisimopoiei
                        ! to kurio programma 
      y1 = funct(xx1)
      y2 = funct(xx2)
      stay = .true.
      do while (stay)
         x3 = xx1 - y1 * (xx1-xx2)/(y1-y2)
         y3 = funct(x3)
         xx1 = xx2
         xx2 = x3
         y1  = y2
         y2  = y3
         stay = abs(y2).gt.epsilon .and. abs(xx2-xx1).ge.epsilon
      enddo
      newton = x3
      return
      end
      
      

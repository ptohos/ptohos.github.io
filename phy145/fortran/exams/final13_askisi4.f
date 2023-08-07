c=========================================
      program gravityfield
c=========================================
      implicit none
      integer iseed
      data iseed /123456/
      integer j, nz, nx, ny, ntries
      real*8 zmax, zmin, z, dz
      real*8 xmin, xmax, ymin, ymax
      real*8 F_mc, Fsimp, Fsimp_old
      real*8 Factor, G, rho, area, mass
      parameter(G=6.674D-11)
      real*8 F_theory, pi
      parameter(pi = dacos(-1D0))
      real*8 mc_integration, simpson_integration, simpson_integral_old

      call srand(iseed)
      xmax   = 5D0
      xmin   = -5D0
      ymax   = 5D0
      ymin   = -5D0
      nx     = 100        ! Arithmos upodiairesewn sto x-aksona - artios
      ny     = 100        ! Arithmos upodiairesewn sto y-aksona - artios
      zmin   = 0.1D0
      zmax   = 1D0
      dz     = 1D-1
      mass   = 1D4
      area   = (xmax-xmin)*(ymax-ymin)
      rho    = mass/area
      ntries = 1E6
      Factor = G*rho
      F_theory = 2d0*pi*Factor  ! H dynami einai aneksartiti tis apostasis 
                                ! apo tin epifaneia arkei oi diastaseis tis
                                ! epifaneias na einai polu megaluteres apo 
                                ! tin apostasi z. Gia apeiri epipedi epifaneia
                                ! h dunami einai statheri kai isi me 2*pi*G*rho

      open(unit=10,file='gravitationalforce.dat',status='unknown')
      nz = (zmax-zmin)/dz + 1
      do j=1, nz
         z = zmin+(j-1)*dz
         F_mc  = mc_integration(z,xmin,xmax,ymin,ymax,ntries)
         Fsimp = simpson_integration(z,xmin,xmax,nx,ymin,ymax,ny)
         Fsimp_old = simpson_integral_old(z,xmin,xmax,nx,ymin,ymax,ny)
         F_mc  = Factor*F_mc
         Fsimp = Factor*Fsimp
         Fsimp_old = Factor*Fsimp_old
         write(10,10)z, F_mc, Fsimp, Fsimp_old, F_theory
      enddo
 10   Format(1x,F4.1,4(3x,G14.8))
      close(10)
      end

c=======================================================================
      real*8 function myfunc(x,y,z)
c=======================================================================
      implicit none
      real*8 x, y, z
      real*8 G, rho,factor

      myfunc = z/(x*x+y*y+z*z)**(3./2.)
      return
      end


c======================================================================
      real*8 function mc_integration(z,xmin,xmax,ymin,ymax,ntries)
c======================================================================
      implicit none
      integer ntries, itry
      real*8 x, y, z
      real*8 xmin, xmax, ymin, ymax
      real*8 sum, res
      real*8 myfunc

      sum = 0D0
      do itry = 1, ntries 
         x = xmin + (xmax-xmin)*rand()
         y = ymin + (ymax-ymin)*rand()
         sum = sum + myfunc(x,y,z)
      enddo
      res = (xmax-xmin)*(ymax-ymin)*sum/ntries
      mc_integration = res
      return
      end

c======================================================================
      real*8 function simpson_integration(z,xmin,xmax,nx,ymin,ymax,ny)
c======================================================================
      implicit none
      integer nx, ny, ix, iy
      real*8 x, xmin, xmax, dx
      real*8 y, ymin, ymax, dy
      real*8 z, sumx, sumxy
      real*8 facty, factx, myfunc

      dx = (xmax - xmin)/nx
      dy = (ymax - ymin)/ny

      sumxy = 0D0
      facty = 2D0
      do 10 iy = 0, ny       ! Loop gia y-oloklirwsi
         y = ymin + iy*dy
         sumx  = 0D0         ! Initialization tou athroismatos gia x-oloklirwsi
         factx = 2D0         ! Paragontas tou athroismatos
         do 20 ix = 0, nx
            x = xmin + ix*dx
            if (ix.eq.0) then                  ! Prwto simeio sto x
               sumx = sumx + myfunc(x,y,z)
               goto 20
            endif
            if (ix.eq.nx) then                 ! Teleytaio simeio sto x
               sumx = sumx + myfunc(x,y,z)
               goto 20
            endif
            if (factx.eq.2D0) then
               factx = 4D0
            else
               factx = 2D0
            endif
            sumx = sumx + factx*myfunc(x,y,z)  ! Neo athroisma tis x-oloklirwsis
 20      continue
         sumx = sumx * dx/3D0                  ! Telos tis x-oloklirwsis 

         if (ix .eq. 0) then                   ! Prwto simeio sto y
            sumxy = sumxy + sumx
            goto 10
         endif
         if (iy .eq. 0) then                   ! Teleytaio simeio sto y
            sumxy = sumxy + sumx
            goto 10
         endif
         if (facty .eq. 2D0) then 
            facty = 4D0
         else
            facty = 2D0
         endif
         sumxy = sumxy + facty*sumx           ! Neo athroisma tis y-oloklirwsis
 10   continue
      sumxy = sumxy * dy/3D0                  ! Telos tis y-oloklirwsis
      simpson_integration = sumxy
      return
      end

c======================================================================
      real*8 function simpson_integral_old(z,xmin,xmax,nx,ymin,ymax,ny)
c======================================================================
c Ayti i subroutine kanei tin oloklirwsi me tin methodo Simpson
c opws tin exoume deiksei sto paradeigma twn dialeksewn kai labs
c======================================================================
      implicit none
      integer nx, ny, ix, iy
      real*8 x, xmin, xmax, dx
      real*8 y, ymin, ymax, dy
      real*8 z, sumx, sumxy, sum
      real*8 myfunc, factor

      dx = (xmax - xmin)/nx
      dy = (ymax - ymin)/ny

      sum = 0D0
      do 10 iy = 0, ny
         y = ymin + dfloat(iy)*dy
         sumx = 0D0
         do 20 ix = 1, nx-1, 2
            x = xmin + dfloat(ix-1)*dx
            sumx = sumx + myfunc(x,y,z)
            x = xmin + dfloat(ix)*dx
            sumx = sumx + 4D0*myfunc(x,y,z)
            x = xmin + dfloat(ix+1)*dx
            sumx = sumx + myfunc(x,y,z)
 20      continue
         sumxy = sumx
         if (iy.eq.0 .or. iy.eq.ny) then
            factor = 1D0
         elseif (mod(iy,2).eq.1) then 
            factor = 4D0
         elseif (mod(iy,2).eq.0) then 
            factor = 2D0
         endif
         sum  = sum + factor*sumxy
 10   continue
      sum = sum * dx * dy/9D0
      simpson_integral_old = sum
      return
      end

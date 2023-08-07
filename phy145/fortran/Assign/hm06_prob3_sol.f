c=======================
      program integrator
c=======================
      implicit none 
      Double precision integrate_mc, func
      Double precision a, b, mc, err, x
      integer i, n
      integer ntot
      double precision pi
      integer iseed
      data iseed/123456/

      pi = acos(-1.)
      a  = 0.0d0          ! oria oloklirwsis: katwtero orio
      b  = pi             ! anwtero orio
      n  = 2
      ntot = 17
      x = rand(iseed)     ! ksekinima tis akoloutheias

      write(6,19)
      do i = 1, ntot
         mc = integrate_mc(err,a,b,n)  ! Apotelesma oloklirwmatos
         write(6,20)n, mc, err
         n  = n * 2
      enddo
 19   format(2x,'MC Points used',3x,'Oloklirwma',6x,'Error')
 20   format(5x,I7,7x,f9.6,4x,f9.6)
      end

c==========================================
      Double Precision Function func(x)
c==========================================
      implicit none
      double precision x
      func = sin(x)
      return
      end

c=======================================================
      Double Precision Function integrate_mc(err,a,b,n)
c=======================================================
c Input:  a, b ta oria oloklirwsis
c         n    o arithmos twn prospatheiwn
c Output: err  to sfalma
c=======================================================
      implicit none
      double precision func          ! H synartisi pros oloklirwsi
      double precision a, b, err
      double precision x, sum, sumsq
      double precision value_integ
      integer n, i

      sum   = 0.0d0
      sumsq = 0.0d0
      do i = 1, n
         x = a + (b-a)*rand()   ! Pernoume ena tyxaio x sto diastima [a,b]
         sum = sum + func(x)
         sumsq = sumsq + func(x)*func(x)
      enddo
      value_integ = (sum/n)*(b-a)
      sum = sum/n
      sumsq = sumsq/n
      err   = (b-a) * sqrt((sumsq - sum*sum)/n)
      integrate_mc = value_integ
      return 
      end

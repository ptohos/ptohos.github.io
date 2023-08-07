c==============================
      program fourier
c==============================
      implicit none
c
      integer i, NxSteps
      real    x, pi, xstep
      real    xmin, xmax
      real    f, sum1, sum5, sum10, sum100
c
      real    func_x, func_sum     ! Dilwsi twn synartisewn sto kurio programma
c
      pi = acos(-1.0) 
c
      xmin = 0.0
      xmax = pi
      xstep = pi/500.
c
      NxSteps = (xmax - xmin)/xstep
c
c Anoigma arxeiou gia apothikeusi apotelesmatwn
c ==============================================
      open(unit=10,file='fourier.dat',status='unknown',err=30)

      do I = 1, NxSteps 
        x      = (I-1) * xstep    ! eyresi tou x
        f      = func_x(x)        ! ypologismos tis f(x) me function funct
        sum1   = func_sum(x,1)    ! ypologismos tis seiras gia N=1
        sum5   = func_sum(x,5)    ! ypologismos tis seiras gia N=5
        sum10  = func_sum(x,10)   ! ypologismos tis seiras gia N=10
        sum100 = func_sum(x,100)  ! ypologismos tis seiras gia N=100
c
        write(10,20)x,f,sum1,sum5,sum10,sum100
c === 
c Tha mporousame na grafame mono
c     write(10,20)x,func_x(x),func_sum(x,1),func_sum(x,5),func_sum(x,10)
c xwris na anathesoume to apotelesma tis synartisis se kapoia metavliti
c====

      enddo
      goto 50
 30   print *,'Error opening file'
 20   format(1x,f7.4,1x,f4.1,4(1x,f7.4))
 50   close(10)
      end

c=====================================
      real function func_x(x)
      implicit none
      real x
c
      if (x.lt.0.) then 
         func_x = -1.0
      else
         func_x = 1.0
      endif
      return
      end
c=====================================

c=====================================
      real function func_sum(x,Nterms)
c=====================================
c Ypologismos toy athroismatos gia 
c kapoio x kai gia Nterms synolika
c orous
c=====================================
      implicit none
      integer  Nterms
      integer  j
      real     sum, pi, x
      real     term
      pi = acos(-1.0)

      sum = 0.0
      do J = 1, Nterms, 2         ! Vima 2 giati oi artioi oroi dinoun 
                                  ! miden afoun (1 - (-1)**n) = 0
         term = sin(j*x)/j
         sum  = sum + term
      enddo
      sum = 4.0*sum/pi            ! Gia tous peritous orous exoume panta 
                                  ! 2 * [1-(-1)]/pi = 4/pi opote to vgazoume
                                  ! koino paragonta
c
      func_sum = sum              ! Panta prepei na dinoume timi sti synartisi
      return
      end
c===================================

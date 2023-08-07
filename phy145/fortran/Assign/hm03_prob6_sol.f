c==============================
      program fourier
c==============================
      implicit none
c
      integer i, j, NSteps
      real    x, pi, step, term
      real    xmin, xmax, sum
      real    sum1, sum5, sum10, sum100
      real    func
c
      pi = acos(-1.0) 
c
      xmin = 0.0
      xmax = pi
      step = pi/500.
c
      NSteps = (xmax - xmin)/step
c
c Anoigma arxeiou gia apothikeusi apotelesmatwn
c ==============================================
      open(unit=10,file='fourier.dat',status='unknown',err=30)
      do I = 1, NSteps 
        x = (I-1) * step       ! eyresi tou x
        if (x.lt.0) then       ! H timi tis sunartisis vimatos
           func = -1.0         ! An einai mikroteri tou 0 tote f(x)=-1 
        else                   ! diaforetika 
           func = 1.0          ! f(x) = +1
        endif
c
        sum = 0.0              ! midenismos tis seiras gia kathe neo x
        do j = 1, 100          ! zitountai to polu 100 oroi [f_100]
           term = sin(j*x)/j
           term = term * 2.*(1.0-(-1.0)**j)/pi
           sum = sum + term
           if (j.eq.1)   sum1   = sum   ! ypologismos twn f1,f5,f10,f100
           if (j.eq.5)   sum5   = sum   ! mesa sto idio loop afou oi megistoi
           if (j.eq.10)  sum10  = sum   ! oroi pou zitame einai 100 simainei
           if (j.eq.100) sum100 = sum   ! oti tha ypologisw to sum gia 1,5,10
        enddo
c
        write(10,20)x,func,sum1,sum5,sum10,sum100
      enddo
      goto 50    ! Den prepei na typwsoume to parakatw munima an ola itan ok
                 ! Tupwnoume to munima se periptwsi pou i entoli open edwse
                 ! kapoio sfalma opws grafoume sto telos, err=30. Diladi
                 ! ektelese tin entoli 30 se periptwsi sfalmatos
 30   print *,'Error opening file'
c
 20   format(1x,f7.4,1x,f4.1,4(1x,f7.4))  ! typwnoume ta sum1,sum5,sum10,sum100
                                          ! me ton idio tropo gia to logo ayto
                                          ! grafoume 4(1x,f7.4) pou simainei 
                                          ! 4 noumera me to idio format 
                                          ! ksanathumizw oti i entolii format 
                                          ! den einai ektelesimi entoli kai 
                                          ! den mporw na steilw ti roi tou 
                                          ! programmatos stin entoli ayti
 50   close(10)
      end

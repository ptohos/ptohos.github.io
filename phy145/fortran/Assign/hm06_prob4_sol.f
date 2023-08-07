c==========================================
      program pollaplo_mcinteg
c==========================================
c...To programma ayto upologizei me ti 
c...methodo MonteCarlo to oloklirvma mias
c...poluwnimikis sunartisis tis morfis 
c...f(x1,x2,x3,..,xn)=(x1+x2+x3+...+xn)^2
c...
c==========================================
      implicit none
      integer iseed 
      data iseed/12345/
      integer ntries, istep, nstep
      integer ndim
      parameter(ndim=6)    ! Diastasi sunartisis - diladi arithmos metablitwn

      real*8 lolim(ndim),uplim(ndim)  ! Oria oloklirwsis kathe metablitis
      data lolim/0.,0.,0.,0.,0.,0./
      data uplim/1.,1.,1.,1.,1.,1./
      real*8 integral
      real*8 mc_integrate    ! Synartisi pou pragmatopoiei tin MC oloklirwsi

      open(unit=20,file='askisi6.dat',status='unknown')

      call srand(iseed)

      nstep = 25
      
      write(20,9)
      do istep = 1, nstep
         ntries = 2**istep
         integral = mc_integrate(ndim,lolim,uplim,ntries)
         print *,ntries, integral
         write(20,10)ntries,integral
      enddo
 9    format(3x,'Tries',5x,'Timi Oloklirwmatos')
 10   format(2x,I8,8x,F10.6)
      close(20)
      end


c=============================================
      real*8 function func(x,ndim)
c=============================================
      implicit none
      integer idim, ndim
      real*8 x(ndim)

      func = 0.0
      do idim = 1, ndim
         func = func + x(idim) ! f(x1,x2,x3,...,xn) = x1 + x2 + x3 + ... + xn
      enddo
      func = func**2           ! f(x1,x2,x3...xn)^2
      return
      end

c===========================================================================
      real*8 function mc_integrate(ndim,lolim,uplim,nMCtries)
c===========================================================================
c... Synartisi pou upologizei to oloklirwma mia sunartisis
c... n-diastasewn (n metavlitwn) me ti methodo tou MC. 
c... I synartisi xreiazetai san input
c... (a) ndim:    ton arithmo twn metablitwn tis oloklirwsimis sunartisis 
c... (b) lolim:   to katw orio oloklirwsis kathe metavlitis x_i
c... (c) uplim:   to panw orio oloklirwsis kathe metavlitis x_i
c... (d) nMCties: ton arithmo twn MC prospatheiwn gia ton upologismo
c...
c... H timi tou oloklirwmatos pou epistrefetai me tin synartisi 
c... stirizetai sti methodo tis mesis timis
c=========================================================================== 
      implicit none
      integer imc, idim
      integer ndim, nMCtries
      real*8 result, factor, fx, mesos
      real*8 lolim(ndim), uplim(ndim)
      real*8 xv(ndim)    ! Oi x-metavlites tis sunartisis
      real*8 func        ! Synartisi pros oloklirwsi

      result = 0.0
      do imc = 1, nMCtries   ! Loop MC prospatheiwn
         do idim = 1, ndim
c... Epilogi tuxaiou x_i simeiou sta oria oloklirwsis.
c... Prepei na to kanoume ndim fores
            xv(idim) = lolim(idim) + (uplim(idim) - lolim(idim))*rand()
         enddo
         fx = func(xv,ndim)   ! Timi ti synartisis
         result = result + fx ! Athroisma twn timwn tis sunartisis
      enddo
      mesos = result/nMCtries

c...Prepei na upologisoume to koino paragonta pou pol/zei kathe mesi timi
c...kai pou eksartatai apo ta oria oloklirwsis kathe metavlitis 
      factor = 1.0
      do idim = 1, ndim
         factor = factor * (uplim(idim) - lolim(idim))
      enddo
c...Teliko apotelesma
      mc_integrate = factor * mesos 
      return
      end

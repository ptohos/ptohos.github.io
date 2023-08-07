c====================================
      program second_deriv
c====================================
c To programma ayto ypologizei ti 
c 2-i paragwgo tis synartisis exp(x).
c====================================
      implicit none
      Integer i
      Integer nsteps, nsteps_max
      parameter(nsteps_max=10)
      Logical first
      Real*8  xlow, xup
      Real*8  xstep
      Real*8  xval
      Real*8  initial_step
      Real*8  result(nsteps_max)
      Real*8  error(nsteps_max)
      Real*8  h_step(nsteps_max)
      Real*8  theory
      Real*8  deriv    ! H synartisi tis 2-is paragwgou

      Print *,' Dwste to katwtero kai anwtero orio tou diastimatos x'
      read *, xlow, xup
      Print *,' Dwste to vima gia ti metavoli toy x'
      read *, xstep
      Print *,' Dwste to arxiko vima (h) ston upologismo tis paragwgou'
      read *, initial_step
 20   Print *,' Gia posa diaforetika h ypologizete ti paragwgo?'
      read *, nsteps
      if (nsteps .gt. 10) then 
         print *,'Exete dwsei polla vimata'
         print *,'O megistos epitreptos arithmos einai 10'
         print *,'Diorthwste tin epilogi sas'
         goto 20
      Endif
      
      first = .true.
      open(unit=20,file='deriv.dat',status='unknown')
      xval = xlow

      do while (xval .le. xup) 
         call derivative(nsteps,xval,initial_step,h_step,result,error)
         if (first) then 
            write(20,30)(h_step(i),i=1,nsteps)
            first = .false.
         endif
         write(20,40)xval,(result(i),i=1,nsteps),deriv(xval)
         xval = xval + xstep
      enddo
 30   format(1x,90('='),/,1x,'xval',2x,'h=',F3.1,5x,'h=',f4.2,
     &       4x,'h=',f5.3,4x,'h=',f6.4,3x,'h=',f7.5,
     &       2x,'h=',f8.6,1x,'h=',f9.7,2x,'Exact',/,1x,90('='))
 40   format(1x,F3.1,7(1x,F10.6),1x,F10.6)
      end

c======================================
      Double precision function func(x)
c======================================
      implicit none
      real*8  x
      func = exp(x)
      return
      end

c========================================
      Double precision function deriv(x)
c========================================
c... Theoritiki timi tis 2-is paragwgou
c========================================
      implicit none
      real*8 x
      deriv = exp(x)
      return
      end

c=======================================================================
      subroutine derivative(nsteps,xval,init_step,h_step,result,error)
c=======================================================================
      implicit none
      Integer nsteps
      Integer I
      Real*8  xval
      Real*8  init_step
      Real*8  result(nsteps)
      Real*8  h_step(nsteps)
      Real*8  error(nsteps)
      Real*8  h

      Real*8  func   ! Orismos tis synartisis pros paragwgisi
      Real*8  deriv  ! Orismos tis synartisis tis 2-is paragwgou 

      do i = 1, nsteps
         result(i) = 0d0
         error(i)  = 0d0
         h_step(i) = 0d0
      end do

      h = init_step  ! Arxiko bima
c...
c...Ypologismos tis paragwgou gia diaforetika vimata
c...Sumfvna me tin askisi xreiazomaste 5 diaforetika
c...vimata ta opoia diaferoun kata dynameis tou 10.
c...Epomenws tha epanalavoume ti diadikasia diairwnta
c...kathe fora to h me 10. 
c...
      do i = 1, nsteps
         h_step(i) = h
         result(i) = (func(xval+h) - 2.*func(xval) + func(xval-h))/(h*h)
         error(i)  = abs(result(i) - deriv(xval))/deriv(xval)  ! Sxetiko sfalma
         h = h/10.
      enddo
      return
      end

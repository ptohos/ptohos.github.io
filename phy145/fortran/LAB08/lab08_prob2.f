c==========================================================================
      program couple_rad_decay
c==========================================================================
c  Ayto poy prospathoyme na lusoume einai
c
c    dN(t)
c   ------ = - N(t)/tau 
c    dt 
c To opoio mporoume na grapsoume ws
c
c   N(t+Dt) - N(t) 
c  ---------------- = -N(t)/tau =>
c        Dt
c
c   N(t+Dt) = N(t) - N(t)*Dt/tau  i diaforetika 
c
c   N(i+1) = N(i) - N(i)*Dt/tau
c
c Stin periptwsi tou problimatos mas exoume duo 
c eidi radienergwn purinwn A kai B opote opws dinetai:
c
c   NA(i+1) =  NA(i) - NA(i)*Dt/tauA                       gia to eidos A
c   NB(i+1) = [NB(i) - NB(i)*Dt/tauB] + NA(i)*Dt/tauA      gia to eidos B
c Paratiroume oti NB(i+1) dinetai opws kai i sxesi gia to
c eidos A me epipleon ton oro pou prokuptei apo tis 
c diaspaseis tou eidous A se B. 
c
c==========================================================================
      implicit none
      real*8   tauA, tauB         ! Real*8 einai isodunamo me double precision
      real*8   dt, time, timetot, t0
      real*8   NA, NB1, NB2       ! Arithmos purinwn A, kai B ti stigmi t
      real*8   NA0, NB01, NB02    ! Arxikos arithmos purinwn
      common/condition/NA0,NB01,NB02,tauA,tauB,dt,timetot,t0 
      call initial
      open(unit=20,file='couple_decay.dat',status='unknown')

      time = t0                   ! Arxiki xroniki stigmi
      NA  = NA0                   ! Arxikoi purines A
      NB1 = NB01                  ! Arxikoi purines B - periptwsi 1
      NB2 = NB02                  ! Arxikoi purines B - periptwsi 2

      do while (time.le.timetot)
         write(20,30)time, NA, NB1, NB2
         NA  = NA - dt*NA/tauA           ! Oi eksiswseis Euler
         NB1 = NB1 + dt*NA/tauA - dt*NB1/tauB
         NB2 = NB2 + dt*NA/tauA - dt*NB2/tauB
         time = time + dt
      enddo
      close(20)
 30   format(1x,f7.5,3(2x,f9.5))
      end

c============================
      subroutine initial
c============================
      implicit none
      real*8   tauA, tauB
      real*8   dt, timetot, t0
      real*8   NA0, NB01, NB02
      common/condition/NA0,NB01,NB02,tauA,tauB,dt,timetot,t0 

      print *," Dwste ton arxiko arithmo purinwn typou A"
      read *, NA0
      print *," Dwste tin stathera diaspasis gia tous purines A"
      read *, tauA
      print *," Dwste ton arxiko arithmo purinwn typou B [NB01/NB02]"
      read *, NB01, NB02
      print *," Dwste tin stathera diaspasis gia tous purines B"
      read *, tauB
      print *," Dwste ton sunoliko xrono gia ti meleti"
      read *, timetot
      print *," Dwste to megethos tou xroniko diastimatos dt"
      read *, dt
      print *," Dwste tin arxiki xroniki stigmi [t0]"
      read *, t0
      return
      end



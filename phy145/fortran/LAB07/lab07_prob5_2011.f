c======================================
      program discharge
c======================================
c...To programma ayto lunei tis 
c...eksiswseis ekseliksis enos 
c...systimatos me tis methodous
c...Euler, Euler-Cromer kai
c...endiamesou simeiou.
c...To systima apoteleitai apo 
c...ena kuklwma RC kai meletoume
c...tin apofortisi tou puknwnti
c...To systima perigrafetai apo 
c...tin diaforiki eksiswsi:
c...
c... Icur = dQ/dt  opou Icur = V/R
c...               kai  V = Q/C
c... H analutiki lusi einai 
c... V = V0 exp(-t/RC)
c================================
      implicit none

      logical doit
      Real R, C, V0, V, Q
      Real dt, t, t0, tmax 
      Real I_eu, Q_eu, V_eu
      Real theory

      Print *,' Dwste to max xroniko diastima [tmax]'
      Read *,tmax
      Print *,' Dwste to xroniko vima [dt]'
      Read *, dt
      Print *,' Dwste tin arxiki xroniki stigmi'
      Read *, t0

      R  = 1000.  ! Antistasi tou kuklwmatos
      C  = 1E-6   ! Xwritikotita puknwti
      V0 = 12.    ! Arxiko dunamiko sto puknwti
      V  = V0     ! Arxiko dunamiko sto puknwti
      Q  = V*C    ! Arxiko fortio puknwti
      t  = t0     ! Arxiki xroniki stigmi
      
      V_eu = V    ! Antigrafi stis parametrous analoga me ti methodo
      Q_eu = Q    ! Voltage kai Charge gia methodo Euler (eu)

      doit = .true.
      theory = V0*exp(-t/(R*C))
         
      open(unit=10,file='Discharge_allEulers.dat',status='unknown')

      do while (doit) 
c...Ektupwsi twn apotelesmatwn apo ti proigoumeni xroniki stigmi
         write(10,20)t, V_eu, theory

c... Euler steps
         I_eu = V_eu/R           ! Reuma sto kuklwma (ayti einai i paragwgos)
         Q_eu = Q_eu - I_eu * dt ! Ellatwsi tou fortiou tou puknwti
         V_eu = Q_eu/C           ! me apotelesma metavoli tou dunamikou

c...Epomeni xroniki stigmi
         t = t + dt
         theory = V0*exp(-t/(R*C))
c...Elegxos gia to an ftasame stin teliki xroniki stigmi

         if (t.gt.tmax) doit = .false.
      end do
 20   format(1x,F7.5,4(2x,F8.5))
      close(20)
      end

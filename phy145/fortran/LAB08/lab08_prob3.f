c=======================================================
      program charge
c=======================================================
c...To programma ayto lunei tis 
c...eksiswseis ekseliksis enos 
c...systimatos me tis methodous
c...Euler, Euler-Cromer kai
c...endiamesou simeiou.
c...To systima apoteleitai apo 
c...ena kuklwma RC kai meletoume
c...tin fortisi tou puknwnti
c...To systima perigrafetai apo 
c...tin diaforiki eksiswsi:
c...
c... Icur = dQ/dt  opou Icur = (V0-V)/R
c...                    V0   = i tasi fortisis
c..                     V    = Q/C i tasi sto puknwti
c... H analutiki lusi einai 
c... V = V0 (1 - exp(-t/RC))
c=======================================================
      implicit none

      Logical doit
      Real R, C, V, V0, Q
      Real dt, t, t0, tmax 
      Real I_eu, Q_eu, V_eu
      Real I_ec, Q_ec, V_ec, I_old
      Real I_md, Q_md, V_md
      Real theory

      Print *,' Dwste to max xroniko diastima [tmax]'
      Read *,tmax
      Print *,' Dwste to xroniko vima [dt]'
      Read *, dt
      Print *,' Dwste tin arxiki xroniki stigmi'
      Read *, t0

      R  = 1000.  ! Antistasi tou kuklwmatos
      C  = 1E-6   ! Xwritikotita puknwti
      V0 = 12.    ! Dynamiko fortisis
      V  = 0.     ! Arxiko dynamiko sta akra tou puknwti
      Q  = 0.     ! Arxiko fortio puknwti (afortistos)
      t  = t0     ! Arxiki xroniki stigmi
      
      V_eu = V    ! Antigrafi metavlitwn gia kathe periptwsi lusis
      Q_eu = Q    ! Tasi kai fortio puknwti gia methodo Euler (eu)
      
      V_ec = V    ! Tasi kai fortio puknwti gia methodo Euler-Cromer (ec)
      Q_ec = Q

      V_md = V    ! tasi kai fortio puknwti gia method endiamesou simeiou (md)
      Q_md = Q 
      
      theory = V0*(1-exp(-t/(R*C)))
      doit = .true.
      
      open(unit=10,file='Charging_Eulerall.dat',status='unknown')

      do while (doit) 
c... Ektupwsi apotelesmatwn tis proigoumenis xronikis stigmis
         write(10,20)t, V_eu, V_ec, V_md, theory

c... Methodos Euler
         I_eu = (V0 - V_eu)/R      ! Reuma sto kuklwma ti xroniki stigmi t
         Q_eu = Q_eu + I_eu * dt   ! Anamenomeno fortio ti xroniki stigmi t+dt
         V_eu = Q_eu/C             ! Tasi ti stigmi t+dt

c... Methodos Euler-Cromer
         I_old = (V0 - V_ec)/R          ! Reuma sto kuklwma ti stigmi t
         V_ec  = (Q_ec + I_old * dt)/C  ! Euler bima gia ti V ti stigmi t+dt  
         I_ec  = (V0 - V_ec)/R          ! Reuma ti xroniki stigmi t+dt
         Q_ec  = Q_ec + I_ec * dt       ! Fortio ti xroniki stigmi t+dt
         V_ec  = Q_ec/C                 ! Tasi ti xroniki stigmi t+dt

c... Methodos endiamesou simeiou 
         I_old = (V0 - V_md)/R              ! Reuma sto kuklwma ti stimgmi t
         V_md  = (Q_md + I_old * dt)/C      ! Euler vima gia ti V ti stigmi t+dt
         I_md  = (V0 - V_md)/R              ! Reuma ti xroniki stigmi t+dt
         Q_md  = Q_md + dt *(I_md+I_old)/2  ! Fortio ti xroniki stigmi t+dt
         V_md  = Q_md/C                     ! Tasi ti xroniki stigmi t+dt

c... Epomeni xroniki stigmi
         t = t + dt         
         theory = V0*(1-exp(-t/(R*C)))

c... Elegxos an ftasame sti megisti epitreptomeni stigmi
         if (t.gt. tmax) doit = .false.

      enddo
 20   Format(1x,f7.5,4(2x,F8.5))
      close(20)
      end

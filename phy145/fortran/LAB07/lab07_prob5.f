c=======================================================
      program oilmotion
c=======================================================
c...To programma ayto lunei tis 
c...eksiswseis ekseliksis enos 
c...systimatos me tis methodous
c...Euler, Euler-Cromer kai
c...endiamesou simeiou.
c...
c...To systima apoteleitai apo 
c...mia mpilia i opoia kineitai
c...mesa se ena doxeio me ladi.
c...Meletoume ti taxutita tis 
c...mpilias i opoia perigrafetai 
c...apo ti diaforiki eksiswsi
c...(kinisi swmatos me antistasi):
c...
c... dv/dt = g - b*v/m opou 
c...                   g = epitaxunsi barutitas
c...                   b = antistasi tou mesou
c...                   m = i maza tis mpilias
c... H analutiki lusi einai 
c... v = (m*g/b)*[1 - exp(-b*t/m)]
c=======================================================
      implicit none

      Logical doit
      Real theory
      Real Coef
      Real g, b, m, v
      Real dt, t, t0, tmax 
      Real v_eu, v_ec, v_md
      Real accel0, accel

      Print *,' Dwste to max xroniko diastima [tmax]'
      Read *,tmax
      Print *,' Dwste to xroniko vima [dt]'
      Read *, dt
      Print *,' Dwste tin arxiki xroniki stigmi'
      Read *, t0

      g  = 9.81    ! Epitaxynsi logw barutitas 
      m  = 0.01    ! maza tis mpilias
      b  = 0.1     ! Stathera antistasis toy ugrou
      Coef = m*g/b ! Paragontas 

      v  = 0.      ! Arxiki taxutita tis mpilias
      t  = t0      ! Arxiki xroniki stigmi
      
      v_eu = v     ! Antigrafi stis metavlites kathe methodou

      open(unit=10,file='OilMotion_EulerAll.dat',status='unknown')

      theory = Coef*(1-exp(-b*t/m))
      doit = .true.

      do while (doit)
c... Print out ta apotelesmata apo to proigoumeno vima
         write(10,20)t, V_eu,  theory

c... Euler steps
         accel = g - b*v_eu/m      ! Ypologismos tis epitaxunsis 
         v_eu  = v_eu + accel * dt ! Anamenomeni taxutita ti stigmi t+dt

c... Epomeni xroniki stigmi
         t     = t + dt
         theory = Coef*(1-exp(-b*t/m))

c... Elegxos gia to an exoume ftasei stin megisti xroniki stigmi
         if (t.gt.tmax) doit = .false.
      enddo
 20   format(1x,f5.3,2(2x,f7.5))
      close(20)
      end

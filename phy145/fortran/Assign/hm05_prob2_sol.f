c==========================================
      program damped_oscillator
c==========================================
c Lusi exiswsis armonikou talantwti me 
c aposbesi me tin voitheia twn methodwn
c Euler kai taxutitas-Verlet.
c Apo ta grafimata paratiroume oti i 
c methodos Euler den perigrafei tin kinisi
c efoson emfanizetai kai pali ayksisi tou
c platous tis talantwsis meta tin parodo 
c kapoiwn periodwn mia kai i methodos den 
c diatirei tin energeia opws exoyme pei 
c enw i methodos tis taxutitas Verlet 
c perigrafei tin kinisi arketa ikanopoiitika
c sugkrinomeni me tin analytiki lysi 
c=========================================
      implicit none
      real kspring, mass, bdamp
      real t0, time, dt, tmax
      real accel, accel_1, accel_2
      real x_eu, x_o, v_eu, v_o, x_an
      real x_ver, v_ver, v_pr

      open(unit=60,file='hm05_prob2.dat',status='unknown')
      kspring = 1.
      mass    = 1.
      bdamp   = 0.1
      tmax    = 25
      t0      = 0
      time    = t0
      dt      = 0.25

      v_o     = 0.0
      v_eu    = v_o
      v_ver   = v_o

      x_o     = 1.0
      x_eu    = x_o
      x_ver   = x_o
      x_an    = 1.00125*exp(-0.05*time)*cos(0.0500209-0.998749*time)
      do while (time.le.tmax)
         write(60,10)time,x_eu,v_eu,x_an,x_ver,v_ver
         accel   = -kspring/mass*x_eu-bdamp*v_eu/mass
         x_eu    = x_eu + v_eu*dt
         v_eu    = v_eu + accel*dt

c... Stin periptwsi ayti i epitaxunsi exei grammiki eksartisi apo tin taxutita
c... Epomenws gia na efarmosoume tin methodo taxytitas-Verlet xreiazetai na 
c... gnwrizoume tin taxytita sto telos tou diastimatos gia na ypologisoume tin
c... epitaxynsi sto telos tou diastimatos. Gia to logo ayto ypologizoume tin 
c... epitaxynsi sto telos tou diastimatos xrisimopoiontas san taxytita sto 
c... telos tou diastimatos ayti pou prokuptei an kanoume ena vima Euler apo 
c... tin arxi sto telos tou xronikou diastimatos 
         accel_1 = -kspring/mass*x_ver-bdamp*v_ver/mass
         x_ver   = x_ver + v_ver*dt + 0.5*accel_1*dt**2
         v_pr    = v_ver + accel_1*dt     ! Vima Euler gia na vroume tin 
                                          ! taxytita sto telos tou diastimatos 
                                          ! wste na upologisoume tin epitax.
                  
         accel_2 = -kspring/mass*x_ver-bdamp*v_pr/mass
         v_ver   = v_ver+(accel_2+accel_1)*dt/2.
         time    = time + dt
         x_an    = 1.00125*exp(-0.05*time)*cos(0.0500209-0.998749*time)
      enddo
 10   Format(1x,f5.2,5(2x,F6.3))
      close(60)
      end

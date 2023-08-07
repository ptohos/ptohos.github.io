c=========================================================
      Program oscillator
c=========================================================
c... To programma ayto lynei tis eksiswseis
c... kinisis tou aplou armonikou talantwnti
c... xrisimopoiwntas ti methodo
c...
c... Taxytitas Verlet
c...
c... Gia na kratisw ton idio sumbolismo opws kai stin 
c... askisi 5 thewrw pinakes xi(2) kai yi(2) stous 
c... opoious to prwto stoixeio twn pinakwn, i.e. xi(1),
c... antistoixei sti thesi tou swmatos enw to 2o stoixeio
c... antistoixei sti taxutita tou swmatos. 
c... Analoga isxuoun kai gia to pinaka xf pou krata ti
c... thesi kai taxutita tou sustimatos sto telos tou 
c... xronikou diastimatos dt. 
c... Gia ti periptwsi tou armonikou talantwti, i kinisi
c... einai se 1 diastasi opote oi pinakes yi(2) kai yf(2)
c... den periexoun tipota endiaferon kai mporoun na 
c... midenistoun. 
c=========================================================
      implicit none
      logical first
      Integer i, ioption
      Integer nperiods, nsteps
      Real*8 t0, x0, v0
      Real*8 Ei, Ef
      Real*8 ti, xi(2), yi(2)
      Real*8 tf, xf(2), yf(2)
      Real*8 dt, tmax, k, m
      Real*8 period
      Common/const/k,m       ! H stathera elatiriou kai i maza tou talantoti

      real*8 d1x, d2x        ! Oi sunartiseis twn paragwgwn tis thesis (d1x)
                             ! kai taxytitas dv/dt=d2x/dt2 = accel 
                             ! Gia geniko provlima oi paragwgoi aytes mporoun
                             ! na eksartwntai apo xrono, thesi kai taxytita

c... Oi parametres pou kathorizoun to talantwti
      print *,'Eisagete ti stathera tou elatiriou [k]'
      read *, k
      print *,'Eisagete ti maza tou swmatos [m]'
      read *, m

c... Oi arxikes synthikes tou problimatos 
      print *,'Eisagete tin arxiki xroniki stigmi [t0]'
      read *, t0
      print *,'Eisagete tin arxiki thesi tou talantwti [x0]'
      read *, x0
      print *,'Eisagetw tin arxiki taxytita toy systimatos [v0]'
      read *, v0

c... Xroniko vima kai megisti xroniki diarkeia gia ekseliksi systimatos
      print *,'Eisagete ton arithmo ton xronikwn vimatwn'
      read *, nsteps
      print *,'Megisto xroniko diastima [Arithmos periodwn]'
      read *, nperiods

      open(unit=10,file='oscillator_velverlet.dat',status='unknown')
      print *,'Methodos Velocity-Verlet'

c... Proetoimasia gia ti xrisi twn methodwn.
c... Antigrafi twn stoixeiwn stous pinakes xi, yi
      ti = t0
      xi(1) = x0    ! thesi sto 1-o stoixeio tou pinaka
      xi(2) = v0    ! taxytita sto 2-o stoixeio tou pinaka
      yi(1) = 0.0   ! O pinakas yi den xrisimopoieitai (1-d provlima)
      yi(2) = 0.0

c... H energeia tou systimatos (dunamiki+kinitiki) 
c... Tha prepei na diatireitai
      Ei = 0.5 * K * xi(1)**2 + 0.5 * m * xi(2)**2

      period = 2.*acos(-1.)*sqrt(m/k)
      tmax   = nperiods * period
      dt     = tmax/nsteps

c... Arxi tis xronikis ekseliksis tou systimatos
      do while(ti.le.tmax)
         tf = ti + dt

         call velocity_verlet(ti,xi,yi,tf,xf,yf)
         Ef = 0.5*m*xf(2)**2 + 0.5*k*xf(1)**2

         write(10,100)tf,xf(1),xf(2),Ef,Ef/Ei,0.5*m*xf(2), 0.5*k*xf(1)

c... Epomeno xroniko vima. -- 
c... Oi times pou vrikame ginontai arxikes gia to epomeno vima
         ti = tf
         xi(1) = xf(1)
         xi(2) = xf(2)
      end do

 100  format(7(1x,F12.4))
      close(10)
      End

c==============================================
	Double Precision Function d1x(t,x,y)
c==============================================
c function dx/dt = v_x
c==============================================
        implicit none
	Real*8 t, x(2), y(2)
        d1x = x(2)
	return
	end

c==============================================
	Double Precision Function d2x(t,x,y)
c==============================================
c function d2x/dt2 = dv/dt = accel 
c==============================================
	Real*8 t, x(2), y(2)
        Real*8 k, m
	Common/const/k,m
        d2x = (-1.0*k/m)*x(1)
	return
        end

c==============================================
	Double Precision Function d1y(t,x,y)
c==============================================
c function dx/dt = v_y
c Den orizontai stin periptwsi ayti
c==============================================
        implicit none
	Real*8 t, x(2), y(2)
        d1y = 0
	return
	end

c==============================================
	Double Precision Function d2y(t,x,y)
c==============================================
c function d2x/dt2 = dv/dt = accel_y
c Den orizetai stin periptwsi ayti
c==============================================
	Real*8 t, x(2), y(2)
        Real*8 k, m
	Common/const/k,m
        d2y = 0.0
	return
        end

c============================================================
      Subroutine Velocity_Verlet(ti,xi,yi,tf,xf,yf)
c============================================================
c... Subroutine gia ti lusi twn eksiswsewn kinisis me ti 
c... me tin apli methodo tou Euler. 
c... Lusi tis 2-is taksis diaforikis eksiswsis se 1-d
c============================================================
c... Input ...
c ti     - Arxiki xroniki stigmi
c xi(1)  - thesi ti xroniki stigmi ti
c xi(2)  - taxytita ti xroniki stigmi ti
c tf     - xroniki stigmi gia tin opoia zitame ti lusi
c
c output ...
c xf(1)  - solution ti xroniki tf = ti + dt
c xf(2)  - velocity ti xroniki tf = ti + dt
c
c...Oi sunartiseis twn paragwgwn prepei na dinontai
c.. d1x(t,x,y)- function dx/dt   (taxutita)
c.. d2x(t,x,y)- function d2x/dt2 (acceleration)
c============================================================
      implicit none
      Real*8 d1x,d2x
      Real*8 ti, xi(2), yi(2)
      Real*8 tf, xf(2), yf(2)
      Real*8 x(2), y(2)
      Real*8 dt, hdt, t

      dt  = tf - ti
      hdt = dt/2.0
      xf(2) = xi(2) + d2x(t,xi,yi)*hdt   ! Miso vima Euler gia tin taxytita
      x(1)  = xi(1)                      ! thesi sto ti
      x(2)  = xf(2)                      ! Taxytita sto meso ti+dt/2
      y(1)  = yi(1)
      y(2)  = yf(2)
      xf(1) = xi(1) + d1x(t,x,y)*dt      ! ousiastika xf=xi+v_i+1/2 * dt
                                         ! diladi h paragwgos sto meso * dt
      x(1)  = xf(1)
      y(1)  = yf(1)
      xf(2) = x(2) + d2x(t,x,y)*hdt      ! uf = u_i+1/2 + a_f*dt/2
      
      Return
      End


c========================================
      program velocity_verlet
c========================================
c...To programma vriskei tis eksiswseis
c...kinisis enos vlimatos xrisimipoiontas
c...ti methodo velocity_verlet
c...
c...Symfwna me ti methodo ayti tha prepei
c...na lusoume tis eksiswseis:
c... u_n+1 = u_n + dt/2*(a_n + a_n+1)
c... r_n+1 = r_n + dt*u_n + a_n*dt**2/2 
c... Sti periptwsi tou provlimatos mas
c... H epitaxynsi sti y dieythynsi einai
c... pantote statheri kai isi me g
c... epomenws ay_n = ay_n+1 = g
c... Sti dieythunsi x den yparxei 
c... epitaxynsi opote oi eksiswseis 
c... aplopoiountai
c========================================
      implicit none
      real v0, t0, angle, t, dt
      real x, y, ux, uy, ax, ay
      real x0, y0, g
      real x_old, y_old
      real ux_old, uy_old
      real ax_old, ay_old
      reaL vx_half, vy_half
c
      real accel
c
      parameter(g=-9.81)
      logical doit

      open(unit=10,file='verlet_vel.dat',status='unknown')
      open(unit=11,file='euler.dat',status='unknown')

      call initialize(dt,v0,t0,x0,y0,angle)
      ux = v0 * cos(angle)
      uy = v0 * sin(angle)
      x  = x0
      y  = y0
      ax = 0
      ay = g
      t  = t0
      doit = .true.
      do while (doit) 
         write(10,20)t,x,y,ux,uy
         y_old  = y
         x_old  = x
         uy_old = uy
         ux_old = ux
         ax_old = ax
         ay_old = ay

         y  = y + uy_old*dt + ay_old*(dt*dt)/2.
         x  = x + ux_old*dt + ax_old*(dt*dt)/2.

         ax = accel(1,x,y,t+dt)   ! Upologismos tis epitaxynsis sti 
         ay = accel(2,x,y,t+dt)   ! thesi t+dt [a_n+1] apo ti dunami
                                  ! i opoia eksartatai apo x kai y thesi

         uy = uy + 0.5*(ay_old + ay)*dt
         ux = ux + 0.5*(ax_old + ax)*dt
         
         t  = t + dt
         if (y.le.0.) doit = .false.
      enddo
      close(20)                   ! kanonika mporoume na efarmosoume linear
                                  ! interpolation gia na broume tis swstes
                                  ! thesi toy x

 20   format(1x,f6.2,4(2x,f10.4))
c
c=====================================================================
c Enas diaforetikos tropos gia na grapsoume ti lusi einai o akoloythos
c=====================================================================
      open(unit=21,file='verlet_mod.dat',status='unknown')
      x   = x0
      y   = y0
      ux  = v0*cos(angle)
      uy  = v0*sin(angle)
      t   = t0
      doit = .true.
      do while (doit)
         write(21,30) t, x, y
         ax = accel(1,x,y,t)
         ay = accel(2,x,y,t)
         vx_half = ux + 0.5*dt*ax    ! Miso vima Euler
         vy_half = uy + 0.5*dt*ay
         x = x + dt * vx_half        ! Xrisimopoioume ti taxytita sto meso
         y = y + dt * vy_half        ! gia na vroume ti teliki thesi
         ax = accel(1,x,y,t+dt)      ! h epitaxunsi sti teliki thesi
         ay = accel(2,x,y,t+dt)     
         ux = vx_half + 0.5*dt*ax    ! Miso vima Euler gia ti taxutita gia 
         uy = vy_half + 0.5*dt*ay    ! thn teliki thesi
c
         t  = t + dt
         if (y.le.0) doit = .false.
      enddo
 30   format(1x,f6.2,2(2x,f10.4))
      close(21)
      end

c================================================
      Real function accel(option,x,y,time)
c================================================
c... Edw ousiastika prepei na exoume ti morfi tis
c... dunamis pou prokalei ti synistwsa epitaxunsi
c... se kathe dieythynsi. 
c... H dunami ayti den einai aparaitita statheri
c... alla mporei na metabaletai analoga me ti 
c... thesi kai ti xroniki stigmi. 
c... H epitaxunsi vrisketai profanws diairwntas 
c... ti dynami me ti maza toy systimatos 
c================================================= 
      implicit none
      real x, y, time
      integer option
      if (option.eq.1) accel = 0.    ! Epitaxunsi sti x-dieythinsi
      if (option.eq.2) accel = -9.81 ! mono i dunami tis barititas
      return
      end

c=================================================
      subroutine initialize(dt,v0,t0,x0,y0,angle)
c=================================================
      implicit none
      real dt, v0, t0
      real x0, y0, angle
      real pi

      print *,'Dwste tin arxiki taxytita tou vlimatos [V0]'
      read *, v0
      print *,'Dwste tin gwnia ripsis [degrees]'
      read *, angle
      print *,'Dwste tis arxikes syntetagmenes tou vlimatos [x/y]'
      read *, x0,y0
      print *,'Dwste tin arxiki xroniki stigmi'
      read *, t0
      print *,'Dwste to xroniko vima'
      read *,dt
c...
c... Metatropi tis gwnias apo moires se aktinia
c...
      pi = acos(-1.)
      angle = angle*pi/360.
c
      return
      end

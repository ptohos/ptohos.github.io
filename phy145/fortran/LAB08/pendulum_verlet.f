c=========================================================
c Programma gia upologismo tis kinisis aplou ekkremous
c xrisimopoiontas tis methodous tou Euler kai Verlet
c=========================================================
      program pendul
      integer*4 MAXnStep
      parameter( MAXnStep = 100000 )
      integer*4 method, irev, iStep, nStep, nPeriod, i
      real*8 theta0, pi, theta, omega, g_over_L, time, time_old
      real*8 tau, accel, theta_old, theta_new, AvePeriod, ErrorBar
      real*8 t_plot(MAXnStep), th_plot(MAXnStep), period(MAXnStep)
c========================
c Epilogi tis methodou 
c========================
      write(*,*) 'Epilekte tin methodo 1) Euler, 2) Verlet: '
      read(*,*) method
c===================================
c Arxikes synthikes gia ti
c thesi kai taxytita toy ekkremoys
c===================================
      write(*,*) 'Dwste arxiki gwnia (se degrees): '
      read(*,*) theta0
      pi = 3.141592654
      theta = theta0*pi/180   ! Metatropi gwnias se aktinia
      omega = 0.0             ! Arxiki taxutita
c===========================
c Statheres tou problimatos
c===========================
      g_over_L = 1.0          ! g/L (monades wste g=l=1)
      time = 0.0              ! arxiki xroniki stigmi 
      irev = 0                ! Plithos perasmatwn apo thesi isorropias
      write(*,*) 'Dwste to xroniko vima: '
      read(*,*) tau
c=========================================================
c Ena vima pisw gia na ksekinisoume ti methodo tou VERLET
c==========================================================
      accel = -g_over_L*sin(theta)    ! epitaxynsi tis varytitas
      theta_old = theta - omega*tau + 0.5*tau**2*accel
c========================
c Efarmogi twn methodwn
c=========================
      write(*,*) 'Dwste to plithos twn xronikwn vimatwn: '
      read(*,*) nStep
      do iStep=1, nStep
c============================================
c Kratame ti gwnia kai xrono gia ti grafiki
c=============================================
        t_plot(iStep) = time
        th_plot(iStep) = theta*180/pi   ! Metatropi aktiniwn se degrees
        time = time + tau
c============================================
c Ypologismos neas thesis kai taxytitas
c symfwna me ti methodo toy Euler i Verlet
c============================================
        accel = -g_over_L*sin(theta)      ! Nea epitaxynsi barytitas
        if( method .eq. 1 ) then
          theta_old = theta               ! Kratame tin proigoumeni thesi
          theta = theta + tau*omega       ! Methodos Euler
          omega = omega + tau*accel
        else
          theta_new = 2*theta - theta_old + accel*tau**2
          theta_old = theta        ! Methodos Verlet
          theta = theta_new
        endif
c====================================================
c Ejetazoume an to ekkremes perase apo ti thesi 
c theta=0. An nai xrisimopoioyme to xrono gia na 
c upologisoume tin periodo
c===================================================
        if( theta*theta_old .lt. 0 ) then   ! eksetasi allagis prosimou
          write(*,*) 'Allagi thesis to xrono  t = ', time
          if( irev .eq. 0 ) then     ! An einai i prwti fora poy perna,
            time_old = time          ! kratame to xrono
          else
            period(irev) = 2*(time - time_old)
            time_old = time
          endif
          irev = irev+1       ! Ayksisi tou arithmou tvn perasmatwn
        endif

      enddo
      nPeriod = irev-1        ! Synolikos arithmos enallagwn 
c========================
c Ypologismos periodou
c========================
      AvePeriod = 0.0
      ErrorBar = 0.0
      do i=1,nPeriod
        AvePeriod = AvePeriod + period(i)
      enddo
      AvePeriod = AvePeriod/nPeriod
      do i=1,nPeriod
        ErrorBar = ErrorBar + (period(i) - AvePeriod)**2
      enddo
      ErrorBar = sqrt(ErrorBar/(nPeriod*(nPeriod-1)))
      write(*,*) 'Average period = ', AvePeriod, ' +/- ', ErrorBar

c============================
c Output twn apotelesmatwn
c============================
c      open(11,file='t_plot.txt',status='unknown')
c      open(12,file='th_plot.txt',status='unknown')
      open(13,file='pendul.dat',status='unknown')
      do i=1,nStep
        write(13,*) t_plot(i),' ',th_plot(i)
      enddo
      stop
      end

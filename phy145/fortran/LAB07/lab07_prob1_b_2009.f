c=======================================
	program lab06_prob3_b
c=======================================
	implicit none
	integer option
	real*8 T0, V0, X0, K, Dt
	real*8 E0, DE, DE_Max, TMax
	real*8 xprev, tprev, vprev
	real*8 pi, xtheory, x_isor
	real*8 x, v, t, Period
	logical first
c
	real*8 energy, accel    ! Synartiseis energeias kai epitaxunsis
	real*8 xanalytic        ! analytiki lusi
	real*8 interpolate 

	call initialize(t0,x0,v0,K,dt)

	first = .true.
	do while (v0.le.8)
	   x_isor  = 0.d0
	   pi      = acos(-1.)
	   Tmax    = 2.0*pi
	   t       = t0
	   x       = x0
	   v       = v0
	   DE_max  = 0.d0
	   DE      = 0.d0
	   E0      = energy(K, x, v)
	   xtheory = xanalytic(K, v, t)

	   xprev   = x
	   tprev   = t
	   vprev   = v
	   
	   option  = 1
	   call printout(t, x, xtheory, dE, option)
	   option = 0
	   
	   do while (.not.(xprev .lt. x_isor .and. x .ge. x_isor))
	      xprev = x
	      tprev = t
	      vprev = v
	      call take_a_step(K,x,v,t,dt)
	      DE = energy(K,x,v) - E0
	      if (dabs(DE) .gt. DE_Max) DE_Max = dabs(DE)
	      xtheory = xanalytic(K, v0, t)
	      call printout(t, x, xtheory, dE, option)
	   enddo
c       
c Kaloume ti synartisi interpolate gia na broume tin periodo
c=============================================================
	   Period = interpolate(tprev, t, xprev, x, x_isor)
	   
	   if (first) then
	      open(unit=30,file='lab06_prob3_periodvsV0.dat',
     &             status='unknown')
	      first = .false.
	   endif
	   write(30,10)V0, Period
 10	   format(1x,f5.2,2x,f7.4)
	   
c=========
c Auksanoume tin arxiki taxytita
c=========
           v0 = 2.*v0 
	enddo
	close(30)
	end

c=================================================
	subroutine initialize(t0,x0,v0,K,dt)
c=================================================
	implicit none
	real*8  T0, X0, V0, K, Dt

	T0 = 0.0d0
	X0 = 0.0d0
	V0 = 0.25d0
	K  = 4.0d0
	dt = 0.0008d0
	print *,' Dwse to xroniko vima'
	read*,dt
	return
	end

c=================================================
	subroutine take_a_step(K,x,v,t,dt)
c=================================================
	implicit none
	real*8 x, v, t, dt
	real*8 a, K
	real*8 accel    ! H synartisi tis epitaxunsis

	a = accel(K,x,v)
	x = x + v*dt + 0.5*a*dt*dt
	v = v + a*dt
        t = t + dt
	return
	end

c====================================================
	subroutine printout(t, x, xtrue, de, option)
c====================================================
	implicit none
	integer option
	real*8 T, X, dE
	real*8 xtrue

	if (option.eq.1) then 
	   open(unit=20,file='lab06_prob3_b.dat',status='unknown')
	endif

	write(20,10)t, x, de
 10	format(1x,f8.5,2x,f8.5,2x,f10.7)
	return
	end

c=================================================
	double precision function accel(k,x,v)
c=================================================
	implicit none
	real*8   K, x, v

	accel = -K*x
	return
	end

c=================================================
	double precision function energy(k,x,v)
c=================================================
	implicit none
	real*8  K, x, v

	energy = 0.5*K*x*x + 0.5*v*v
	return
	end


c=====================================================
	double precision function xanalytic(K,V0,T)
c=====================================================
	implicit none
	real*8  K, V0, T
	real*8  w

        w = dsqrt(K)
	xanalytic = V0*sin(w*t)/w      ! Analytiki lusi einai x=x0*sin(wt)
                                       ! w = sqrt(k/m) alla m = 1
                                       ! Kseroume akoma oti:
                                       ! 0.5*k*x0**2 = 0.5*m*v0**2=>
                                       ! x0=v0/sqrt(m/k)=> x0=v0/w
	return
	end


c==============================================================
        double precision function interpolate(x0,x1,y0,y1,yfin)
c==============================================================
        implicit none
        real*8 x0, x1, y0, y1, xfin, yfin

        xfin = x0 + (x1 - x0)*(yfin-y0)/(y1 - y0)

        interpolate = xfin
        return
        end

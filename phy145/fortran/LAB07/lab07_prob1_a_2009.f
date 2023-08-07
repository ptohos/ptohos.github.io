c=======================================
	program lab06_prob3_a
c=======================================
	implicit none
	integer option
	real*8 T0, V0, X0, K, Dt
	real*8 E0, DE, DE_Max, TMax
	real*8 pi, xtheory
	real*8 x, v, t
c
	real*8 energy, accel    ! Synartiseis energeias kai epitaxunsis
	real*8 xanalytic        ! analytiki lusi

	call initialize(t0,x0,v0,K,dt)
	pi      = acos(-1.)
	Tmax    = 2.0*pi
	t       = t0
	x       = x0
	v       = v0
	DE_max  = 0.d0
	DE      = 0.d0
	E0      = energy(K, x, v)
	xtheory = xanalytic(K, v, t)
	option  = 1

	call printout(t, x, xtheory, dE, option)
	option = 0

	do while (t .le. tmax) 
	   call take_a_step(K,x,v,t,dt)
	   DE = energy(K,x,v) - E0
	   if (dabs(DE) .gt. DE_Max) DE_Max = dabs(DE)
	   xtheory = xanalytic(K, v0, t)
	   call printout(t, x, xtheory, dE, option)
	enddo

	write(6,10)V0, dt, DE_Max/E0
 10	format(1x,'V0 = ',f8.5,1x,'Dt = ',f8.5,1x,'De_max/E0 = ',f8.5)

	end

c=================================================
	subroutine initialize(t0,x0,v0,K,dt)
c=================================================
	implicit none
	real*8  T0, X0, V0, K, Dt

	T0 = 0.0d0
	X0 = 0.0d0
	V0 = 1.0d0
	K  = 4.0d0
	dt = 0.05d0
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
	   open(unit=20,file='lab06_prob3_a.dat',status='unknown')
	endif

	write(20,10)t, x, xtrue, de
 10	format(1x,f8.5,2x,f8.5,2x,f8.5,2x,f8.5)
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



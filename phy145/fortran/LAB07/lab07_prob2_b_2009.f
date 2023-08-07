c=======================================
	program lab06_prob4_b
c=======================================
	implicit none
	logical first
	integer option
	real*8 x, t, v, xprev, tprev, vprev
	real*8 T0, V0, X0, K, Dt
	real*8 E0, DE, DE_Max, TMax
	real*8 pi, v0_max, period

	real*8 energy, accel    ! Synartiseis energeias kai epitaxunsis
	real*8 interpolate

	call initialize(t0,x0,v0,K,dt)
	pi     = acos(-1.)
	v0_max = 8.d0
	first  = .true.
	do while (v0 .le. v0_max)
	   Tmax   = 100.d0
	   t      = t0
	   x      = x0
	   v      = v0
	   DE_max = 0.d0
	   DE     = 0.d0
	   E0     = energy(K,x,v)
	   tprev = t
	   xprev = x
	   vprev = v
	   
	   if (first) then 
	      option = 1
	      first  = .false.
	   endif
	   call printout(t,x,de,option)
	   option = 0
	   
	   do while (t.le.tmax.and.(.not.(xprev.lt.0..and.x.ge.0.)))
	      tprev = t
	      xprev = x
	      vprev = v
	      call take_a_step(K,x,v,t,dt)
	      DE = energy(K,x,v) - E0
	      if (dabs(DE) .gt. DE_Max) DE_Max = dabs(DE)
	      call printout(t,x,de,option)
	   enddo

	   period = 0.d0
	   if (t .lt. tmax)period = interpolate(tprev, t, xprev, x, 0.d0)
	   write(6,10)V0, dt, DE_Max/E0, period
 10	   format(1x,'V0 = ',f8.5,1x,'Dt = ',f8.5,
     &            1x,'De_max/E0 = ',f9.7,2x,'Period=',1x,f8.5)

	   v0 = 2.0*v0
	enddo
	end

c=================================================
	subroutine initialize(t0,x0,v0,K,dt)
c=================================================
	implicit none
	real*8  T0, X0, V0, K, Dt

	T0 = 0.0d0
	X0 = 0.0d0
	V0 = 0.25d0     ! Ayti ti fora i taxytita tha metavaletai
    	K  = 4.0d0
	dt = 0.0004d0  ! H kaluteri epilogi gia dt apo to (a) erwtima
	print *,' Dwse to xroniko vima'
	read*,dt
	return
	end

c=================================================
	subroutine take_a_step(k, x, v, t, dt)
c=================================================
	implicit none
	real*8 k, x, v, t, dt
	real*8 a
	real*8 accel    ! H synartisi tis epitaxunsis

	a = accel(k,x,v)
	x = x + v*dt + 0.5*a*dt*dt
	v = v + a*dt
        t = t + dt
	return
	end

c=================================================
	subroutine printout(t, x, dE, option)
c=================================================
	implicit none
	integer option
	real*8 t, x, dE

	if (option.eq.1) then 
	   open(unit=20,file='lab06_prob4_b.dat',status='unknown')
	endif

	write(20,10)t, x, de
 10	format(1x,f8.5,2x,f8.5,2x,f8.5)
	return
	end

c===============================================================
	double precision function interpolate(x0,x1,y0,y1,yfin)
c===============================================================
	implicit none
	real*8  x0, y0, x1, y1, yfin
	interpolate = x0 + (yfin - y0)*(x0 - x1)/(y1 - y0)
	return
	end

c=================================================
	double precision function accel(k,x,v)
c=================================================
	implicit none
	real*8   K, x, v

	accel = -K*sin(x)
	return
	end

c=================================================
	double precision function energy(k,x,v)
c=================================================
	implicit none
	real*8  K, x, v

	energy = K*(1-cos(x)) + 0.5*v*v
	return
	end


c=================================================
	double precision function xanalytic(K,v0,t)
c=================================================
	implicit none
	real*8  K, V0, t
	real*8  f

        f = sqrt(K)
	xanalytic = V0*sin(f*t)/f
	return
	end



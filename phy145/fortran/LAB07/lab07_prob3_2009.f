c=======================================
	program lab06_prob5
c=======================================
	implicit none
	real*8 T, X, V
	real*8 T0, V0, X0, K, Dt, Dt_Min
	real*8 E0, DE, DE_Max, TMax
	real*8 pi, V0_max, period
	logical first
c
c Functions
c===========
	real*8 energy, accel    ! Synartiseis energeias kai epitaxunsis
	real*8 interpolate

	call initialize(t0,x0,v0,K,dt)
	pi     = acos(-1.0)
	Tmax   = 4.0*pi
	Dt_min = 1.d-4
c========================
c Loop ws pros taxytites
c========================	
	first = .true.
	do while (dt .ge. DT_Min)
	   t      = t0
	   x      = x0
	   v      = v0
	   DE_max = 0
	   DE     = 0
	   E0     = energy(K,x,v)
c======================
c Ektelesi diadikasias
c======================
	   do while (t .le. TMax)
	      call take_a_step(K,x,v,t,dt)
	      DE = energy(K,x,v) - E0
	      if (dabs(DE) .gt. DE_Max) DE_Max = dabs(DE)
	   enddo
	   if (first) then
	     open(unit=30,file='lab07_prob3.dat',status='unknown')
	  endif
	  write(30,10)log10(dt), log10(DE_Max)
	  write(6,10)log10(dt), log10(DE_Max)

	  dt     = dt/2.d0      ! Miso vima

	enddo
 10	format(1x,f8.5,2x,f8.5)
	close(30)
	end

c=================================================
	subroutine initialize(t0,x0,v0,K,dt)
c=================================================
	implicit none
	real*8  X0, V0, K, T0, Dt

	T0 = 0.0d0
	X0 = 0.0d0
	V0 = 1.0d0
    	K  = 4.0d0
	dt = 0.5D0

	return
	end

c=================================================
	subroutine take_a_step(k,x,v,t,dt)
c=================================================
	implicit none
	real*8 x, v, t, dt, k
	real*8 a
	real*8 accel    ! H synartisi tis epitaxunsis

	a = accel(k,x,v)
	x = x + v*dt + 0.5*a*dt*dt
	v = v + a*dt
        t = t + dt
	return
	end

c=================================================
	subroutine printout(t, x, de, option)
c=================================================
	implicit none
	integer option
	real*8 t, x, de

	if (option.eq.1) then 
	   open(unit=20,file='lab07_prob3.dat',status='unknown')
	endif
	write(20,10)t, x, de

 10	format(1x,f8.5,2x,f8.5,2x,f8.5)
	return
	end

c================================================================
	double precision function interpolate(x0,x1,y0,y1,yfin)
c================================================================
	implicit none
	real*8  x0, y0, x1, y1, yfin
	interpolate = x0 + (x1 - x0)*(yfin - y0)/(y1 - y0)
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



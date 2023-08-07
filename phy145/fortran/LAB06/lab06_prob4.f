c=======================================
	program lab06_prob2
c=======================================
	implicit none
	integer option
	real*8 T0, V0, X0, Dt
	real*8 xfinal, tfinal
	real*8 xtheory, tfinal_theory
	real*8 xprev, vprev, tprev
	real*8 x, v, t, a
c
	real*8 energy, accel    ! Synartiseis energeias kai epitaxunsis
	real*8 xanalytic        ! analytiki lusi
	real*8 interpolate

	call initialize(t0,x0,v0,dt)
	xfinal  = 0.d0
	t       = t0
	x       = x0
	v       = v0
	xtheory = xanalytic(x, v, t)
	option  = 1

	call printout(t, x, xtheory, option)
	option = 0

	do while (x .ge. xfinal) 
	   xprev = x
	   tprev = t
	   vprev = v
	   call take_a_step(x,v,t,dt)
	   xtheory = xanalytic(x0, v0, t)
	   call printout(t, x, xtheory, option)
	enddo

	a = accel(x0,v0,t)
	tfinal_theory = (-v0 - sqrt(v0*v0 - 2.*a*x0))/a

	tfinal = interpolate(tprev,t,xprev,x,xfinal)
	write(6,12)xfinal, tfinal, tfinal_theory
 12	format(1x,'To svma perna apo ti thesi x =',1x,F5.2,1x,
     &         'otan t_interp = ',f7.4,/,
     &         1x,'O anamenomenos theoritika xronos einai:',1x,f7.4)

	end

c=================================================
	subroutine initialize(t0,x0,v0,dt)
c=================================================
	implicit none
	real*8  T0, X0, V0, K, Dt

	T0 = 0.0d0
	X0 = 1.0d0
	V0 = 4.0d0
	dt = 0.1d0
	print *,' Dwse to xroniko vima'
	read*,dt
	return
	end

c=================================================
	subroutine take_a_step(x,v,t,dt)
c=================================================
	implicit none
	real*8 x, v, t, dt
	real*8 a
	real*8 accel    ! H synartisi tis epitaxunsis

	a = accel(x,v,t)
	x = x + v*dt + 0.5*a*dt*dt
	v = v + a*dt
        t = t + dt
	return
	end

c====================================================
	subroutine printout(t, x, xtrue, option)
c====================================================
	implicit none
	integer option
	real*8 T, X
	real*8 xtrue

	if (option.eq.1) then 
	   open(unit=20,file='lab06_prob4.dat',status='unknown')
	endif

	write(20,10)t, x, xtrue
 10	format(1x,f8.5,2x,f8.5,2x,f8.5)
	return
	end

c=================================================
	double precision function accel(x, v, t)
c=================================================
	implicit none
	real*8   x, v, t

	accel = -0.5d0     ! Statheri epitaxynsi
	return
	end

c=====================================================
	double precision function xanalytic(X0, V0, T)
c=====================================================
	implicit none
	real*8  V0, X0, T
	real*8  accel  ! Synartisi epitaxynsis

	xanalytic = x0 + V0*T + 0.5*accel(x0,v0,t)*T**2

	return
	end


c==============================================================
	double precision function interpolate(x0,x1,y0,y1,yfin)
c==============================================================
c  Dinontas tis suntetagmenes 2 simeiwn A(x0,y0) kai B(x1,y1)
c  xrisimopoioume tin eksiswsi tis eytheias pou perna apo ta 
c  2 gia na broume tin x i tin y syntetagmeni enos tritou 
c  simeiou tou opoiou kseroume tin mia apo tis 2 syntetagmenes
c===============================================================
c  Stin prokeimeni periptwsi h sunartisi pou exoume einai x=x(t)
c  Epomenws to rolo twn x's paizoun oi xronoi t kai to rolo twn
c  y's i thesi tou swmatos. 
c  H timi pou epithymoume einai o xronos otan to yfin=xfin=0
c==============================================================
	implicit none
	real*8 x0, x1, y0, y1, xfin, yfin

	xfin = x0 + (x1 - x0)*(yfin-y0)/(y1 - y0)

	interpolate = xfin
	return
	end

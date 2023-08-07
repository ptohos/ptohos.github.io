c==========================================
      program pendulum
c==========================================
c motion of a simple pendulum   
c theta() = pendulum angle   
c omega() = pendulum angular velocity
c t()     = time
c length  = length of string
c dt      = time step
c==========================================
      integer nsteps
      real theta(5000), omega(5000), t(5000)
      real length, dt
c
      call initialize(theta,omega,t,length,dt)
      call calculate(theta,omega,t,nsteps,length,dt)
c
      end
c====================================================
      subroutine initialize(theta,omega,t,length,dt)
c====================================================
c initialize variables
c theta = pendulum angle  
c omega = pendulum angular velocity
c====================================================
      implicit none
      real   theta(5000), omega(5000), t(5000)
      real   length, dt
      real   pi
      parameter(pi=3.141592654)
c
      print *, 'initial pendulum angle (in degrees)'
      read(5,*) theta(1)
      theta(1) = theta(1)*pi/180.  ! metatropi se rad
      print *, 'initial angular velocity of pendulum (in radians/s)'
      read(5,*) omega(1)
      t(1) = 0.
      print *,'length of pendulum (in m)'
      read(5,*) length
      print *,'time step'
      read(5,*) dt
      return
      end

c===========================================================
      subroutine calculate(theta,omega,t,nsteps,length,dt)
c==========================================================
      implicit none
      integer i, nsteps
      real theta(5000),omega(5000),t(5000)
      real dt, length, period
      real pi, g
      parameter(pi = 3.141592654)
      parameter(g  = 9.8)
c
      i = 0
      period = 2. * pi /sqrt(g/length) ! periodos toy ekkremous
 20   i = i + 1
      t(i+1) = t(i) + dt
      omega(i+1) = omega(i) - (g/length) * theta(i) * dt ! Euler method
      theta(i+1) = theta(i) + omega(i) * dt
      if (t(i+1).le.5.*period) goto 20  ! 5 periodoys
      nsteps = i
      do i = 1, nsteps
         theta(i) = theta(i)*180./pi
      enddo
      return
      end
c


      

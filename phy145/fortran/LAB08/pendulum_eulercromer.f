      program linear_pendulum
c====================================================
c Kinisi aplou ekkremoys me ti methodo Euler-Cromer
c theta = pendulum angle,   
c omega = pendulum angular velocity, 
c time = time 
c length = length of string
c dt = time step
c=====================================================
      implicit none 
      integer j, nmax
      parameter(nmax=5000)
      
      double precision dt, length
      double precision theta(nmax),omega(nmax)
      double precision time(nmax),energy(nmax)

      open(unit=10,file='theta_vs_time_ec.dat',status='unknown')
      open(unit=12,file='omega_vs_time_ec.dat',status='unknown')
      open(unit=14,file='omega_vs_theta_ec.dat',status='unknown')
      open(unit=16,file='full_energy_ec.dat',status='unknown')
 
      call initialize(theta,omega,time,length,dt)
      call calculate_euler(theta,omega,energy,time,length,dt)
   
      do j = 1, nmax
         if ((j.gt.1).and.(time(j).eq.0.0)) then
           goto 100
        else 
           write(10,*) time(j),theta(j)
           write(12,*) time(j),omega(j)
           write(14,*) theta(j),omega(j)
           write(16,*) time(j),energy(j)
        end if
      end do
 100  continue
      end

c===========================================================
      subroutine initialize(theta,omega,time,length,dt)
c===========================================================
      implicit none
      integer nmax
      parameter(nmax=5000)
      real pi
      parameter(pi=3.141592654)
      double precision length,dt
      double precision theta(nmax),omega(nmax),time(nmax)

      print *,'initial pendulum angle (in degrees)' 
      read (5,*) theta(1)
      theta(1) = theta(1)*pi/180.
      print *,'initial angular velocity of pendulum (in radians/s)'
      read (5,*) omega(1)
      time(1)=0.0d0
      print *,'length of pendulum (in m)' 
      read (5,*) length
      print *,'time step'
      read(5,*) dt
      return
      end

c=====================================================================
      subroutine calculate_euler(theta,omega,energy,time,length,dt)
c=====================================================================
      implicit none
      integer j
      integer nmax
      parameter(nmax=5000)
      double precision g, pi
      parameter(g=9.81,pi=3.14159265)
      double precision period,no_periods
      double precision kinetic_energy, potential_energy
      double precision length,dt
      double precision theta(nmax),omega(nmax)
      double precision time(nmax),energy(nmax)
  
      period = 2.0*pi/sqrt(g/length)  ! period of pendulum
      no_periods=5.*period            ! akolouthia gia five periods

      j = 0
      do while (time(j+1) .lt. no_periods)
         j=j+1
         time(j+1)  = time(j) + dt
         omega(j+1) = omega(j)-(g/length)*theta(j)*dt  ! Euler method
         theta(j+1) = theta(j)+omega(j+1)*dt
c=====================================================================
c  H allagi ayti, i xrisimopoiisi toy neou omega gia to
c  ilopologismo tou neou theta apotelei ti methodo tou Euler-Cromer
c=====================================================================
         kinetic_energy   = 0.5*length**2 * omega(j)**2
         potential_energy = g*length*(1-cos(theta(j)))
         energy(j) = kinetic_energy + potential_energy   
      enddo

      return
      end

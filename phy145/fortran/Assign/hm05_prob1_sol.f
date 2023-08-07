c=====================================
      program podilato
c=====================================
c Lysi toy problimatos kinisis 
c podilati me statheri isxy me 
c i xvris antistasi aera me tin
c methodo tou Euler
c H isxus dinetai apo P = dE/dt
c => P = d(mu^2/2)/dt
c Paragwgizontas P = m*u*(du/dt)=>
c accel = du/dt = P/(m*u)
c Stin periptwsi kinisis me antistasi
c Tha exoume: accel = P/(m*u)-Fact*u**2
c opou o b'oros einai i epivradynsi
c logw tou aera 
c=====================================
      implicit none
      real*8 u, uA, u0, P
      real*8 accel, t, t0
      real*8 dt, tmax, mass
      real*8 C, A, rho, fact

      Print *, 'Poios o suntelestis antistasis'
      read*, C
      Print *, 'Poia i diatomi tou swmatos?'
      read*,A
      Print *, 'Poia i puknotita tou aera?'
      read*,rho
      print *, 'Poia i isxus pou katanalwnei o podilatis'
      read*,P
      Print *, 'Poia i arxiki taxutita tou podilati'
      read*,u0
      Print *, 'Poia i maza tou sustimatos'
      read*,mass
      Print *, 'Poia i arxiki xroniki stigmi'
      read*,t0
      Print*, 'Poio to xroniko diastima tis kinisis'
      read*,tmax
      Print*, 'Poio to xroniko vima'
      read*,dt

      open(unit=60,file='bicycle.dat',status='unknown')
      Fact = 0.5*C*rho*A
      t = t0
      u = u0
      uA = u0
      Do while (t.le.tmax) 
         write(60,*)t, u, uA
         accel = P/(mass*u)
         u  = u + accel*dt

         accel = P/(mass*uA) - 0.5*Fact*uA**2
         uA = uA + accel*dt
         t = t + dt
      enddo
      close(60)
      end

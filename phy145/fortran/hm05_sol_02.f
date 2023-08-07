c====================================================
      program straight_wire
c====================================================
c... To programma ayto briskei to magnitiko 
c... pedio pou dimiourgeitai apo ena eythugrammo
c... agwgo pou diarreetai apo reuma I 
c... xrisimopoiwntas ti methodo oloklirwsis 
c... Simpson. 
c... B = mu*I/(4*pi) * (x*dz)/(z^2+x^2)^3/2
c... H ologklirwsi symfvna me ti methodo Simpson
c... tha dwsei:
c... B + muo*I*x*dz/[3*(4*pi)] * [f(-L/2)+4*f(-L/2+dz)+2f(-L/2+2*dz)+...+f(L/2)}
c=====================================================
      implicit none
      Integer I, J, K, nsteps
      Integer ngrid, ngridmax, ninter
      Parameter(ngridmax=5000)
      Real*8  R(ngridmax), BField(ngridmax)
      Real*8  Length, zvalue, dz
      Real*8  Sum, Sumold, epsi, diff
      parameter(epsi=1E-2)
      real*8  theory

      print *,'Dwste ton arithmo twn simeiwn ston x-aksona'
      read *, ngrid 
      print *,'Dwste ta vimata 2**Nsteps gia oloklirwsi [Nsteps<20]'
      read *, ninter
      print *,'Dwste to mikos tou agwgou'
      read *, Length

      open(unit=40,file='bfield.dat',status='unknown')
      do i = 1, Ngrid
c... Xvrismos tou syrmatos me to 0 sto meso. Opote exoume -L se L
         zvalue = -Length/2. 
         R(i)   = Dfloat(i)/Ngrid   ! apostaseis x
         Sum    = 0.0
         Sumold = 0.0

c... Efarmogi Simpson
c... suneisfora twn akrwn toy agwgou
         nsteps = 2
         do k = 1, ninter
            dz = Length/nsteps 
            Sum = (dz/3.0) * 2 /(zvalue**2 + r(i)**2)**3./2. 
            do j = 1, nsteps-2, 2
               zvalue = zvalue + dz
               Sum = Sum + 4*dz/(3*(zvalue**2 + r(i)**2)**3./2.)
               zvalue = zvalue + dz
               Sum = Sum + 2*dz/(3*(zvalue**2 + r(i)**2)**3./2.)
            enddo
            zvalue = zvalue + dz
            Sum = Sum + 4*dz/(3*(zvalue**2 + r(i)**2)**3./2.)
            diff = abs(Sum - Sumold)/Sum
            if (diff.lt.epsi) goto 20
            Sumold = Sum 
            nsteps = 2.*nsteps
         enddo
 20      call calculate_field(BField(I), r(i), Length,dz)

c... Ypologismos toy pediou symfqna me to nomo toy Ampere
         theory = 2. / r(i)

         write(40,30)r(i),sum,bfield(i),theory
      enddo
 30   format(4(2x,F12.8))
      end


c========================================================
      Subroutine calculate_field(By, x, Length,dz)
c========================================================
c... Ypologismos tou magnitikou pediou gia sygkekrimeni 
c... apostasi sti x-dieythynsi kai gia dz kata mikos tou
c... surmatos
c... H subroutine efarmozei to athroisma Sum dz*x/r^3 
c... r=sqrt(z_i^2+x^2)  opou z_i apo to -L sto L
c========================================================
      implicit none
      Integer Ngrid
      Real*8 By, x, Length
      Real*8 dz, z, r

      By = 0.0
      z = -Length
      Do while (abs(z) .le. Length)
         r  = sqrt(x**2 + z**2)
         By = By + dz * x / r**3
         z  = z + dz
      enddo
      return
      end

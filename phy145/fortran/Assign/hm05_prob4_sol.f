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
      Real*8  Length, zvalue, dz, x
      Real*8  Sum, Sumold, epsi, diff
      parameter(epsi=1D-10)
      real*8  theory

 10   print *,'Dwste ton arithmo twn simeiwn ston x-aksona'
      read *, ngrid 
      if (ngrid.gt.ngridmax) then 
         print *,'Dwste mikrotero arithmo simeio [max = 5000]'
         goto 10
      endif
      print *,'Dwste to mikos tou agwgou'
      read *, Length

      open(unit=40,file='bfield.dat',status='unknown')
      do i = 1, Ngrid
c... Xvrismos tou syrmatos me to 0 sto meso. Opote exoume -L se L
         zvalue = -Length/2. 
         r(i)   = dfloat(i)/Ngrid   ! apostaseis x
         Sumold = 0.0
         x      = r(i)
c... Efarmogi Simpson - xrisimopoiisi mikroterou vimatos 
c... ews otou exoume sxetiki metavoli mikroteri apo 1D-10
         nsteps = 2
         diff   = 1.D0
         do while (diff .gt. epsi) 
            zvalue = -Length/2.
            dz = Length/nsteps 
            Sum = 0.0
            do j = 0, nsteps-1, 2
               Sum =  Sum + x/((zvalue**2. + x**2.)**(3./2.)) 
               zvalue = zvalue + dz
               Sum = Sum + 4D0 * x/((zvalue**2. + x**2.)**(3./2.))
               zvalue = zvalue + dz
               Sum = Sum + x/((zvalue**2. + x**2.)**(3./2.))
            enddo
            Sum = Sum * dz /3.0D0
            diff = abs(Sum - Sumold)/Sum
            if (diff.lt.epsi) goto 20
            Sumold = Sum 
            nsteps = 2.*nsteps
         enddo
 20      call calculate_field(BField(I), x, Length,dz)

c... Ypologismos toy pediou symfwna me to nomo toy Ampere
         theory = 2. / x

         write(40,30)x,sum,bfield(i),theory
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
c... r=sqrt(z_i^2+x^2)  opou z_i apo to -L/2 sto L/2
c========================================================
      implicit none
      Integer Ngrid
      Real*8 By, x, Length
      Real*8 dz, z, r

      By = 0.0
      z = -Length/2.
      Do while (z .le. Length/2.)
         r  = sqrt(x**2 + z**2)
         By = By + dz * x / r**3
         z  = z + dz
      enddo
      return
      end

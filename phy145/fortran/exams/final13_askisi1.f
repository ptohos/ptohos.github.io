c=============================================================
      program lagrangepoint
c=============================================================
c H eyresi tou simeiou lagrange metaksu Gis-Selinis wste na
c exoume sto simeio ayto tin idia periodo peristrofis me 
c ayti ti Selinis vrisketai me to na lusoume tin eksiswsi
c pou dinetai stin askisi. Ayti einai mia eksiswsi 5ou
c bathmou. Epomenws mporoume na xrisimopoiisoume mia apo
c tis methodous euresis rizas (newton,bisection)
c=============================================================
      implicit none
      real*8 error, func, deriv
      real*8 R, precision
      parameter(precision=1D-4)
      real*8 G, Rgs, Mgis, Msel, omega
      real*8 GMg, GMs

      G    = 6.674D-11
      Mgis = 5.974D24
      Msel = 7.348D22
      omega= 2.662D-6
      Rgs  = 3.844D8
      GMg  = G*Mgis
      GMs  = G*Msel

      R = Rgs/2D0       ! Arxiki epilogi gia lusi tis eksiswsis

      error = func(R,GMg,GMs,Rgs,omega)/deriv(R,GMg,GMs,Rgs,omega)
      do while (abs(error).gt.precision) 
         R = R - error
         error = func(R,GMg,GMs,Rgs,omega)/deriv(R,GMg,GMs,Rgs,omega)
      enddo
      write(6,10)R
 10   format(1x,'To simeio Lagrange vrisketai se apostasi',1x,E10.4,1x,
     &       'm apo to kentro tis Gis')
      end

c===============================================
      real*8 function func(R,GMg,GMs,Rgs,omega)
c===============================================
      implicit none
      real*8 R
      real*8 GMg, GMs, Rgs, omega

      func = GMg/(R*R) - GMs/(Rgs-R)**2 - R*omega*omega

      return
      end

c================================================
      real*8 function deriv(R,GMg,GMs,Rgs,omega)
c================================================
      implicit none
      real*8 R
      real*8 GMg, GMs, Rgs, omega

      deriv = -2D0*GMg/(R*R*R) - 2D0*GMs/(Rgs-R)**3 - omega*omega

      return
      end

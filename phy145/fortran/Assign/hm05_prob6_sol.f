      program nonlinear_oscillator
c==============================================================================
c To programma ayto apanta sta mporei na xrisimopoiithei gia ta 
c 4 erwtimata tis askisis me ti xrisi diaforwn epilogwn: 
c Oi allages me tin proigoumeni askisi einai stis sunartiseis
c pou upologizoun tin epitaxunsi kai energeia
c Episis den upologizetai i analutiki lusi i opoia eksartatai
c apo to platos tis talantwsis
c Oi epiloges einai idies me tin askisi 1 
c Option 0:  erwtimata 1-4 gia dt = 0.05
c Option 1:  erwtimata 1-4 gia veltisto xroniko vima opoy Delta(amp2/amp1)<1%
c Option 2:  erwtimata 5-6 gia veltisto xroniko vima opws vrethike sto 3
c==============================================================================
      implicit none
      integer ioption
      real tstep, tstep_opt, v0, vmax
      real tmax, time, x, x0, v
      real tprev, xprev, vprev
      real Ene0, Ediff, xtheory, K, mass
      real amp1, amp2
      real period
      real pi, a
      parameter(pi=acos(-1.))
c...Sunartiseis 
      real interpolate, acc, energy

      tstep  = 0.05
      x0     = 0.0
      k      = 4.0
      mass   = 1.0
      v0     = 1.0
      vmax   = v0

 50   print *,'Epilogi gia ta erwtimata '
      print *,'Epiloges [0:Erwtima 1, 1:Erwtima 2-4, 2:Erwtima 5&6]'
      read *,ioption
      if (ioption.lt.0.or.ioption.gt.2) then 
         print *,'H epilogi',ioption,' den uparxei'
         print *,'Epilekste ena noumero metaksu 0 kai 2'
         goto 50
      endif

      if (ioption.ge.1) then 
         print *,'Prosdiorismos tou veltistou xronikou vimatos dt'
         call optimum_tstep(k,mass,tstep,x0,v0,amp1,amp2,tstep_opt)
         print *,'Veltisto xroniko vima dt = ', tstep_opt
         print *,'1o megisto = ',amp1
         print *,'2o megisto = ',amp2
         print *,'% allagi   = ',(amp2/amp1-1)*100,' %'
         tstep = tstep_opt
      endif


      if (ioption.le.1) then
         if (ioption.eq.0) then 
            open(unit=20,file='nonlinear_oscil.dat',status='unknown')
         else if (ioption.eq.1) then 
            open(unit=20,file='nonlinear_oscil_opt.dat',
     &           status='unknown')
         endif
      endif

      if (ioption.eq.2) then 
         open(unit=21,file='period_vs_energy_nonlinear.dat',
     &        status='unknown')
         v0 = 0.25
         vmax = 8.0
      endif

      do while (v0 .le. vmax)
         time = 0
         x    = x0
         xprev= x
         v    = v0
         tmax = 4*pi

         Ene0  = energy(k,mass,x,v)

c...Ektypwsi gia tis arxikes synthikes
         if (ioption .le. 1) then 
            Ediff   = energy(k,mass,x,v)-Ene0
            write(20,60)time, x, Ediff
         endif

         do while ((ioption.le.1 .and. time.lt.tmax) .or.
     &             (ioption.eq.2 .and. .not.(xprev.lt.0. .and. x.ge.0)))
                    
c...Diatiroume tis proigoumenes times gia grammiki paremvoli
            tprev = time
            xprev = x
            vprev = v
c...Epitaxunsi
            a = acc(k,mass,x,v)
c...Oloklirwsi
            x = x + v*tstep + 0.5*a*tstep*tstep
            v = v + a*tstep
            time = time + tstep
            Ediff = energy(k,mass,x,v) - Ene0
            if (ioption.le.1) then 
               write(20,60)time, x, Ediff
            endif
         enddo
         if (ioption.eq.2) then 
            period = interpolate(xprev,x,tprev,time,0.)
            write(21,61)0.5*mass*v0*v0, log10(0.5*mass*v0*v0),period 
         endif
         v0 = 2.0*v0     ! Nea arxiki taxytita (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
      enddo
 60   Format(1x,f6.2,2x,f6.2,2x,f7.3)
 61   Format(1x,F7.3,2x,F7.3,2x,F6.3)
      if (ioption.eq.1) close(20)
      if (ioption.eq.2) close(21)
      end


c======================================================
      real function interpolate(x0,x1,y0,y1,x)
c========================================================
      implicit none
      real x0, x1, y0, y1, x

      interpolate = y0 + (y1-y0)*(x-x0)/(x1-x0)

      return
      end

c======================================================
      real function acc(k,m,x,v)
c========================================================
      implicit none
      real x, v, k, m

      acc = -K/m*x**3
      return
      end

c=======================================================
      real function energy(K,m,x,v)
c========================================================
      implicit none
      real x, v, K, m

      energy = 0.25*k*x**4 + 0.5*m*v*v

      return
      end

c=========================================================
      subroutine optimum_tstep(k,mass,tstep_init,x0,v0,
     &                         amp1,amp2,tstep_opt)
c=========================================================
      implicit none
      real k, mass
      real x0, v0
      real tstep, tstep_init, tstep_opt 
      real time, tmax, x, v
      real tprev, xprev, vprev
      real amp, amp1, amp2
      real fract_change
      real pi
      parameter(pi=acos(-1.))
      real precision
      parameter(precision=0.01)
c...
      real a, acc


      tstep = tstep_init
      tmax = 4.0*pi

 50   x = x0
      v = v0
      time = 0.0
      amp1 = 0.0
      amp2 = 0.0

      do while (time .le. tmax)
         tprev = time
         xprev = x
         vprev = v
         a = acc(k,mass,x,v)
         x = x + v*tstep + 0.5*a*tstep*tstep
         v = v + a*tstep
         time = time + tstep

c... Elegxoume an i taxutita allazei prosimo. 
c... Ayto simatodotei to perasma apo akrotato kinisis
         if (vprev .ge. 0.0 .and. v.le.0.0) then
            amp = xprev
            if (x .gt. amp) amp = x
            if (amp1 .eq. 0.0) then 
               amp1 = amp       ! To prwto akrotato
            else if (amp2 .eq. 0.0) then 
               amp2 = amp       ! To deytero akrotato
               goto 100         ! Den xreiazetai na eksetastei peretairw kinisi
            endif
         endif
      enddo

 100  fract_change = amp2/amp1 - 1.
      if (fract_change.gt.precision) then 
         tstep = tstep/2.
         goto 50
      endif
      tstep_opt = tstep

      return
      end

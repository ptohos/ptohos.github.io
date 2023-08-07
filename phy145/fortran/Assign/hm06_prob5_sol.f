c===============================================================
      program mc_radioactive_decay
c===============================================================
c... To programma ayto prosomoiwnei ti radienergo
c... diaspasi duo radienergwn pyrinwn o enas apo
c... tous opoious apotelei proion tou allou. 
c... H theoritiki lusi einai:
c...
c...  NA(t) = NA(t=0) * exp(-L_A*t)    L_A = wmega_A = 1/tau
c...  NB(t) =  [NA(t=0)*L_A/(L_B - L_A)]*[exp(-L_A*t)-exp(-L_B*t)]
c            + NB(t=0)exp(-L_B*t)
c...
c... Prosoxi i prosomoiwsi douleuei mono otan wmega*t << 1
c...
c... Paradeigma:
c...            wmega_x = 0.01
c...            wmega_y = wmega_x/5=0.002  O xronos zwis Y einai 5fores tou X
c...            Nx      = 1000
c...            Ny      =    0
c...            tmax    = 1000
c...            dt      =    1
c...            Ntries  = 1000
c...
c... H diadikasia ekteleitai Ntries wste na paroume mesi timi
c... apo polla peiramata kai na exoume kalytero deigma kai na 
c... apofeyxthoyn oi statistikes diakymanseis
c===============================================================
      implicit none
      logical doit
      integer iseed, i, j, k
      integer ntries
      integer nmax
      parameter (nmax = 10000)             ! megistos aritmos xronikwn vimatwn
      integer ntot_x(nmax), ntot_y(nmax)

      integer Nx_th(nmax), NY_th(nmax)
      integer NX_left, NY_left
      integer NX0, NY0
      integer NX, NY
      real    wmega_x, wmega_y            ! 1/tau statheres diaspaseis
      real    R, t, dt, tmax
      real    coeff, term

c...Arxikes times tou problimatos

      print *,'Dwste ton arxiko arithmo purinwn X'
      read *, NX0
      print *,'Dwste ton arxiko arithmo purinwn Y'
      read *, NY0
      print *,'Dwste ti stathera diaspasis toy X [1/lifetime]'
      read *, wmega_x
      print *,'Dwste ti stathera diaspasis toy Y [1/lifetime]'
      read *, wmega_y
 10   print *,'Dwste ton oliko xrono meletis tmax'
      read *, tmax
      print *,'Dwste to xroniko vima dt'
      read *, dt
      if (tmax/dt.gt.nmax) then 
         print *,'Ariumos xronikwn vimatwn megaluteros apo Nmax'
         print *,'Diorthwste to vima sas i to tmax'
         goto 10
      endif
      print *,'Dwste to synoliko arithmo Monte Carlo peiramatwn'
      read *, ntries


      open(unit=10,file='radioactive_decay.dat',status='unknown')
      iseed = 123456
      call srand(iseed)

      do j=1, nmax
         ntot_x(j) = 0
         ntot_y(j) = 0
         nx_th(j) = 0
         ny_th(j) = 0
      enddo

      do j = 1, Ntries
c... Gia kathe prospatheia MC ksekiname apo tin arxi
         NX_left = NX0     
         NY_left = NY0
         t = 0.
         k = 1
         doit = .true.
         ntot_x(k) = ntot_x(k) + Nx_left   ! Kratame to athroisma
         ntot_y(k) = ntot_y(k) + Ny_left
         Nx_th(1)  = NX0
         Ny_th(1)  = NY0
c...H diadiakasia tis prosarmogis gia to xroniko diastima pou theloume
         do while (doit)
            k = k + 1
            t = t + dt

c... Theoritikos ypologismos -- 1 fora mono
            if (j.eq.1) then
               Nx_th(k)= NINT( NX0 * exp(-wmega_x * t) )
               Coeff   = NX0 * wmega_x/(wmega_y - wmega_x)
               term    = exp(-wmega_x*t) - exp(-wmega_y*t)
               Ny_th(k)= NINT( Coeff*term + NY0 * exp(-wmega_y*t) )
            endif

c...Gia kathe xroniko vima elegxoume kathe purina an mporei na diaspastei
            nx = nx_left
            do i = 1, NX 
               R = rand()
               if (R .le. wmega_x) then    ! Apofasi an o pyrinas X diaspatai
                  NX_left = NX_left - 1    ! Elatwnoume tous purines X kata 1
                  NY_left = NY_left + 1    ! Auksanoume tous pyrines Y kata 1
               endif
            enddo

c...Gia to idio ayto vima elegxoume posoi apo tous purines Y diaspwntai
            NY = NY_left
            do i = 1, NY 
               R = rand()
               if (R.le.wmega_y) then 
                  NY_left = NY_left - 1       
               endif
            enddo

c...Apothikeysi apotelesmatwn gia to xroniko ayto vima
            ntot_x(k) = ntot_x(k) + NX_left
            ntot_y(k) = ntot_y(k) + NY_left

c...Elegxos an ftasame sto xroniko orio
            if (t.ge.tmax) doit = .false.
         enddo
      enddo

c...Apotlesmata
      do j=1, k
         Write(10,20)(j-1)*dt, nx_th(j), NINT(Ntot_x(j)/float(ntries)), 
     &               ny_th(j), NINT(Ntot_y(j)/float(ntries))
      enddo
 20   format(1x,f7.3,4(2x,I8))
      end

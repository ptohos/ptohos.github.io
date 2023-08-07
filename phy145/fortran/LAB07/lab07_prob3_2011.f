c==========================================================================
      program rad_decay
c==========================================================================
c  Ayto poy prospathoyme na lusoume einai
c
c    dN(t)
c   ------ = - N(t)/tau 
c    dt 
c To opoio mporoume na grapsoume ws
c
c   N(t+Dt) - N(t) 
c  ---------------- = -N(t)/tau =>
c        Dt
c
c   N(t+Dt) = N(t) - N(t)*Dt/tau  i diaforetika 
c
c   N(i+1) = N(i) - N(i)*Dt/tau
c
c=============
c Gia to fit
c============= 
c Otan theloyme na kanoume prosarmogi twn simeiwn tis 
c methodou tote xreiazetai na grapsoume tis akoloythes 
c entoles sto gnuplot:
c f(x) = a*exp(b*t)     ! opou a einai i mia parametros tis prosarmogis
c                       ! kai b einai i deyteri parametros tis prosarmogis
c                       ! Ayto einai to theoritiko montelo tis radienergous
c                       ! diaspasis N = N0 exp (-t/tau) kai to rolo tou N0
c                       ! pezei i metavliti a kai tou -1/tau to b
c H prosarmogi (fit) ginetai ws eksis:
c a = 80                ! Aytes oi duo times dinontai gia na boithisoume 
c b = -0.5              ! ti prosarmogi. Sto telos tha breite tis kaluteres
c                       ! times pou perigrafoun ta dedomena sas
c fit f(x) "filename.dat" via a,b  ! Ayto leei sto gnuplot na kanei prosarmogi
c                                  ! ta dedomena sto "filename.dat" me ti
c                                  ! synartisi f(x) pou exei fit parametrous 
c                                  ! tis a kai b. Sto telos tou fit tha parete
c                                  ! tis times tou a kai b kai ta sfalmata tous
c                                  ! opws episis kai to syntelesti susxetisis
c                                  ! Ayta prepei na sumpiptoun me tis times pou
c                                  ! exete dwsei gia ta a=N0 kai b=-1/tau sto 
c                                  ! problima sas. 
c                                  ! Apo ti stigmi pou ta a kai b exoun 
c                                  ! kathoristei mporeite na kanete to grafima
c                                  ! tis f(x) 
c plot "filename.dat"
c replot f(x)
c 
c==========================================================================
      implicit none
      real*8   tau               ! Real*8 einai isodunamo me double precision
      real*8   time, t0
      real*8   NA0, NA, NAlim, Nth
      integer  j, ncases
      parameter(ncases=6)
      real*8   dt(ncases)
      data dt/1.0, 0.5, 0.2, 0.1, 0.05, 0.005/

      print *, ' Dwste ton arxiko arithmo purinwn'
      read *, NA0
      print *,' Dwste ti stathera diaspasis'
      read *, tau
      print *, 'Dwste to epithumito teliko pososto [%]'
      read *, NAlim
      print *,' Dwste tin arxiki xroniki stigmi [t0]'
      read *, t0

      do j = 1, ncases
         if (j.eq.1) open(unit=20,file='decay_1.dat',status='unknown')
         if (j.eq.2) open(unit=20,file='decay_05.dat',status='unknown')
         if (j.eq.3) open(unit=20,file='decay_02.dat',status='unknown')
         if (j.eq.4) open(unit=20,file='decay_01.dat',status='unknown')
         if (j.eq.5) open(unit=20,file='decay_005.dat',status='unknown')
         if (j.eq.6) open(unit=20,file='decay_0005.dat',status='unknown')
         time = t0                ! Arxiki xroniki stigmi
         NA  = NA0                ! Arxikoi purines A
         NAlim = NA0 * NAlim/100. ! telikos arithmos purinwn

         do while (NA.ge.NAlim)
            Nth = NA0*exp(-time/tau)       ! H theoretiki timi
            write(20,30)time, NA, Nth
            NA  = NA - dt(j) * NA/tau      ! H methodos Euler

            time = time + dt(j)
         enddo
         close(20)
      enddo
 30   format(1x,f7.5,2(2x,f9.5))
      end




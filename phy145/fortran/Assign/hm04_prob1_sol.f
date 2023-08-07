      program cooling
c=========================================================================
c To programma upologizei ti thermokrasia 
c mias sfairas pou psuxetai ksekinontas 
c apo mia thermokrasia Temp0, se mia 
c thermokrasia TempFinal. 
c H eksiswsi pou perigrafei tin thermotima
c pou xanetai mesw aktinovolias einai:
c   dTemp/dt = -2.2067x10^-12(Temp^4 - 81x10^8)
c H analytiki lusi prokuptei apo oloklirwsi 
c tis parapanw eksiswsis kai einai: 
c   dTemp/[A(Temp^4 - B)] = dt =>
c t = -[2*arctan(Temp/B^0.25)+ln(B^0.25+Temp)-ln(Temp-B^0.25)]/(4*A*B^(3/4))
c  opou A=-2.2067x10^-12 kai B = 81x10^8
c H lisi gia t=480sec dinei Temp = 647.55
c
c Apo to grafima paratiroume oti i methodos Euler 
c einai proseggistiki kai oti to sfalma ellatwnetai 
c kata ena paragonta 2 kathws to vima elattwnetai 
c kata ena paragonta 2. Wstoso opws exoume deiksei 
c apo to anaptugma Taylor to sfalma pou kanoume se
c kathe vima einai analogo tou tetragwnou tou vimatos
c opote tha eprepe na meiwnetai kata 1/4. Stin 
c pragmatikotika omws to sfalma einai athroistiko 
c gia ta vimata pou kanoume kai epomenws sunolika to
c sfalma einai analogo tou vimatos.  
c=========================================================================
      implicit none
      integer Itemp, nsteps
      parameter(nsteps = 6)
      real Temp0, TempFinal, Temp(nsteps)
      real Time0, TimeFinal, dt, Time(nsteps)
      real Timeprev, Tempprev, TimeTemp
      real timestep(nsteps), dTempdt
      data timestep/15,30,60,120,240,480/
      real A, B
      parameter(A=-2.2067E-12, B=81E8)
      real TempTrue, error, percenterror
      parameter(TempTrue=647.55)   !<< Thermokrasia se t=480sec analytika      
      real interpolate             !<< Sunartisi
      
      Temp0 = 1200.0    !<< Arxiki thermokrasia
      Time0 = 0.0       !<< arxiki xroniki stigmi
      TimeFinal = 480.0 !<< Teliki xroniki stigmi
      TempFinal = 320.0 !<< Epithumiti teliki thermokrasia

      open(unit=60,file='hm04_prob1.dat',status='unknown')

      do Itemp = 1, 6
         Time(Itemp) = Time0
         Temp(Itemp) = Temp0
         dt = timestep(Itemp)
         do while(Time(Itemp).lt.TimeFinal)
            dTempdt = A*(Temp(Itemp)**4 - B)
            Temp(Itemp) = Temp(Itemp)+dt*dTempdt
            Time(Itemp) = Time(Itemp)+dt
         enddo
         error = TempTrue - Temp(Itemp)
         percenterror = 100*error/TempTrue
         write(60,30)int(dt), Temp(Itemp), error, percenterror !<< Erwtisi (c)
c
c... Erwtisi (a) and (b)
c========================
         if (Itemp .eq. 2) then 
            write(6,40)int(TimeFinal),int(dt),Temp(Itemp)      !<< Erwtisi (a)
            do while(Temp(Itemp).gt.TempFinal)
               Timeprev = Time(Itemp)
               Tempprev = Temp(Itemp)
               dTempdt = A*(Temp(Itemp)**4 - B)
               Temp(Itemp) = Temp(Itemp)+dt*dTempdt
               Time(Itemp) = Time(Itemp)+dt
            enddo
            if (Temp(Itemp).eq.TempFinal) then 
               TimeTemp = Time(Itemp) 
            else
               TimeTemp = interpolate(Timeprev,Tempprev,Time(Itemp),
     &                                Temp(Itemp),TempFinal)
            endif                
            write(6,45)int(dt), int(TempFinal),TimeTemp
         endif
      enddo

      close(60)
 30   Format(1x,i3,2x,F8.2,2x,F6.1,2x,F6.2)
 40   Format(1x,65('='),/,1x,'Tin xroniki stigmi t = ',I3,'sec',1x,
     &       'kai gia xroniko vima dt = ',I2,'sec,',/,1x
     &       'i sfaira exei thermokrasia Temp = ',F6.2,'K',/,1x,65('='))
 45   Format(/,1x,65('='),/,1x,'Me vima dt = ',I3,'sec',1x,
     &       'i sfaira apokta thermokrasia Temp = ',I3,'K,',/,
     &       1x,'se xrono t = ',F7.2,'sec',/,1x,65('='))
      end

c=================================================
      real function interpolate(x0,y0,x1,y1,y)
c=================================================
c H sunartisi kanei grammiki paremvoli metaksu twn 
c simeiwn (x0,y0) kai (x1,y1) gia na vrei tin timi 
c tou x otan kseroume tin timi tou y.
c Stin periptwsi mas to rolo tis aneksartitis metavlitis
c paizei o xronos kai tis eksartwmenis i thermokrasia
c======================================================
      implicit none
      real x0, y0, x1, y1, y, x
      real slope

      slope = (y1 - y0)/(x1 - x0)
      x = x0 + (y - y0)/slope
      interpolate = x
      return
      end

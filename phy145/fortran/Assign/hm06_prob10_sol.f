c=============================================================================
      program rungekutta4
c=============================================================================
c... Efarmogi tis methodou Runge-Kutta 4-is taksis gia tin perigrafi tis
c... kinisis enos swmatos se reusto katw apo tin epidrasi mias dunamis 
c... antistasis analogis tis taxutitas tou swnatos se kapoia dynami. 
c... Efarmogi tis methodou gia tin periptwsi tis katakoryfis volis enos
c... swmatos.  
c...
c... To programma perissotero deixnei to tropo xrisis tis methodou 
c... Runge-Kutta kai ta diafora vimata pou prepei na kanete
c...
c... To systima perigrafetai apo 2 diaforikes eksiswseis 1-is taksis
c... (gia taxutita kai thesi) sti y-dieythinsi. An eixame kinisi se 
c... 2-diastaseis (p.x. plagia voli) tha eixame 4 diaforikes eksiswseis.
c... Epomenws kathe fora prepei na ypologisoume 2 paragwgous.
c... H mia einai i epitaxunsi kai epireazei tin ekseliksi tis taxutitas 
c... kai i alli einai i taxutita pou epireazei tin ekseliksi tis thesis.
c...
c... Arxika as doume theoretika to xrono anodou kai kathodou
c... katw apo tin epidrasi tis dunamis tis antistasis:

c... Stin periptwsi ayti i mixaniki energeia toy swmatos den diatireitai
c... logw tis antistasis toy aera. Wstoso i dynamiki energeia einai i idia
c... se kathe simeio tis troxias (eite to swma anevainei eite katevainei). 
c... Alla i kinitiki tou energeia einai megaluteri kathws anevainei se sxesi
c... me ayti poy exei sto idio upsos otan katevainei. Ayto symvainei epeidi
c... i antistasi tou aera exei energisei megalytero diastima:

c... DeltaE_mix = -E_kin^an - E_dyn^an + E_kin^kat + E_dyn^kat = -W_aera =>
c... W_aera = 0.5*m*(u_kat^2 - u_an^2) => u_kat - u_an < 0 => u_kat < u_an

c... opou E_kin^an, E_kin^kat, E_dyn^an, Edyn^kat einai oi kinitiki kai
c... dynamiki energeia tou swmatos otan anevainei kai otan katevainei. 

c... H taxytika me tin opoia katebainei to swma einai se kathe simeio tis
c... troxias mikroteri apo tin taxytita tou swmatos sto antistoixo simeio
c... otan to swma anevainei. Etsi otan to swma ftasei sto edafos tha exei
c... mikroteri taxytita apo tin taxytita pou eixe otan ektokseythike.
c... H mesi taxytita anodou einai:   <u>^an = hmax/t_an
c... H mesi taxytita kathodoy einai: <u>^kat = hmax/t_kat
c... H taxytita stin anodo metavaletai apo u0 -> 0 enw stin kathodo apo 0->u0'
c... opou u0' < u0 symfwna me ta parapanw. Epomenws kai <u>^kat < <u>^an. 
c... Afou to hmax einai idio kai stis 2 periptwseis tote
c... 1/t_an > 1/t_kat => t_kat > t_an.

c... Enas diaforetikos sulogismos einai me vasi tis dynameis. Kathws to swma
c... anevainei dexetai synoliki dunami 
c... Fol_an  = F_var + F_ant enw otan katevainei i dynami 
c... Fol_kat = F_var - F_ant. 
c... Epomenws to swma dexetai megalyteri epitaxynsi otan anevainei apo otan
c... katevainei kai ara stamata pio grigora. 
c...
c... Epomenws perimenoume lunontas to provlima na vroume oti o xronos kathodou
c... einai megalyteros apo ton xrono anodou. 
c==============================================================================
      implicit none
      logical doit
      real*8  t_in, t_fin
      real*8  y_in(2), y_fin(2)
      real*8  t_prev, y_prev
      real*8  g, v0, y0, dt, D, M_swm
      real*8  E, E0, F, h_mx
      real*8  t_an, t_kat, t_ol
      common/const/D, g

c... Oi sunartiseis twn paragwgwn
      real*8  d1y, d2y

c... H synartisi tis grammikis paremvolis
      real*8  interpolate

c... Arxikes synthikes tou problimatos
      print *,'Dwste tin arxiki thesi tou swmatos'
      read *, y_in(1)
      print *,'Dwste tin arxiki taxytita tou swmatos'
      read *,v0
      print *,'Dwste tin maza toy swmatos M'
      read *,M_swm
      print *,'Dwste ti stathera antistasis D'
      read *,D
      print *,'Dwste to xroniko vima (dt)'
      read *,dt
c
      open(unit=10,file='stone_rk4.dat',status='unknown')

      g        = 9.81D0
      t_in     = 0.0
      t_fin    = 0.0
      y0       = y_in(1)
      y_in(2)  = v0     ! H 2-i thesi tou pinaka exei taxutita
      y_fin(1) = y_in(1)
      y_fin(2) = y_in(2)

c... H arxiki energeia tou vlimatos E0 (isws uparxei kai arxiko upsos)
      E0 = M_swm * g * y_in(1) + 0.5 * M_swm * y_in(2)**2

c... H dunami pou dexetai arxika to swma
      F = -M_swm * (g + D * y_in(2) * abs(y_in(2)))

      write(10,20)t_in, y_in(1), y_in(2), E0/E0, F

c... Epanalipsi twn xronikwn vimatwn mexri to blima na xtupisei sto edafos
      doit = .true.
      Do while (doit) 

c... Epomeno vima 
         t_in = t_fin
         y_in(1) = y_fin(1)
         y_in(2) = y_fin(2)

         t_fin = t_in + dt

c... Klisi tis subroutine rk4 gia ti methodo Runge-Kutta 4ou bathmou 
c... gia systima diaforikwn eksiswsewn se 1 diastasi

         call rk4(t_in,t_fin,y_in,y_fin)

c... Ypologismos energeias kai apothikeusi apotelesmatwn
         E = M_swm * g * y_fin(1) + 0.5 * M_swm * y_fin(2)**2
         E = E/E0        ! Kanonika i energeia prepei na diatireitai

         F = -M_swm * (g + D * y_fin(2) * abs(y_fin(2))) 

         write(10,20)t_fin, y_fin(1), y_fin(2), E, F

c... Elegxos gia to an to swma eftase sto megisto upsos
         if (y_in(2)*y_fin(2).lt.0) then   ! H taxutita allazei prosimo
            t_an = interpolate(t_in, t_fin, y_in(2), y_fin(2),0d0)
            h_mx = interpolate(y_in(1), y_fin(1), y_in(2), y_fin(2),0d0)
         endif

c... Elegxos gia to an to vlima epestrepse sto arxiko upsos
         if (y_fin(1).lt.y0) doit = .false.
      enddo
      close(10)

c... Telika apotelesmata
      open(unit=10,file='stone.dat',status='unknown')
      t_ol  = interpolate(t_in,t_fin,y_in(1),y_fin(1),0.d0)
      t_kat = t_ol - t_an
      write(10,30)t_an, t_kat, h_mx
      write(6,30)t_an, t_kat, h_mx        ! Kai stin othono

 20   format(1x,f10.3,2(2x,f12.3),2x,F8.6,2x,F8.4)
 30   format(1x,'O xronos anodou einai:  ',1x,F8.4,/,
     &       1x,'O xronos kathodou einai:',1x,F8.4,/,
     &       1x,'Megisto upsos einai:    ',1x,F8.4)


      end


c==============================================
      double precision function d1y(t,y)
c==============================================
c   H paragwgos dy/dt = v_y
c==============================================
      implicit none
      Real*8 t, y(2)
      d1y = y(2)  
      return
      end

c==============================================
      double precision function d2y(t,y)
c==============================================
c   H paragwgos d^2y/dt^2 = dv_y/dt = accel_y
c
c H parakatw periptwsi einai gia F_ant =-Dv^2
c Gia F_ant = -Dv 
c        d2y = -1.0 * ( g + D * y(2) )
c Gia F_ant = -Dv^3
c        d2y = -1.0 * ( g + D * v^2 * y(2) )
c==============================================
      implicit none
      Real*8 t, y(2), D, g, v
      common/const/D, g

      v = abs(y(2))                    ! Metro tis taxutitas
      d2y = -g - D * v * y(2) 

      return
      end


c==========================================================
      Subroutine rk4(ti,tf,yi,yf)
c==========================================================
c     Runge-Kutta 4th-order
c----------------------------------------------------------
c... Orismata eisagwgis
c
c ti 	- arxikos xronos
c tf    - telikos xronos meta to vima t_in + dt
c yi(2) - arxiki thesi (1) kai taxytita (2) sti y-dieythynsi
c
c Orismata Epistrofis ...
c yf(2) - H lusi sti y-dieythynsi (1)-thesi (2)-taxytita
c
c... Aparaitito na ypologistoun oi synartiseis twn paragwgwn
c d1y(t,x,y)- synartisi dy/dt
c d2y(t,x,y)- synartisi d2y/dt2
c==========================================================
      implicit none
      Real*8 yi(2), yf(2)
      Real*8 h, hh, t, y(2)
      Real*8 k1y(2), k2y(2), k3y(2), k4y(2)    ! K's gia thesi kai taxytita

c... Oi synartiseis twn paragwgwn
      Real*8 d1y, d2y, ti, tf 

      h  = tf-ti   ! vima 
      hh = h/2.0   ! miso vima
      t  = ti

c...Ypologismos tou k1
      k1y(1) = d1y(t,yi)      ! Paragwgoi thesis kai taxutitas stin 
      k1y(2) = d2y(t,yi)      ! arxi tou diastimatos

c... Ypologismos tou k2
      y(1)   = yi(1)+k1y(1)*h/2.0  ! H taxytita kai thesi sti mesi 
      y(2)   = yi(2)+k1y(2)*h/2.0  ! tou diastimatos me vima Euler sto meso
      
      k2y(1) = d1y(t+hh,y)    ! Paragwgoi thesis kai taxutitas sto 
      k2y(2) = d2y(t+hh,y)    ! meso tou diastimatos
      
c... Ypologismos tou k3
      y(1)   = yi(1)+k2y(1)*h/2.0  ! H taxytita kai thesi sti mesi tou 
      y(2)   = yi(2)+k2y(2)*h/2.0  ! diastimatos me vima Euler sto meso. Ayti 
                                   ! ti fora xrisimopoioume ti paragwgo pou 
                                   ! upologisame sto meso symfvna me to k2
      
      k3y(1) = d1y(t+hh,y)   ! Paragwgoi thesis kai taxutitas sto meso 
      k3y(2) = d2y(t+hh,y)   ! tou diastimatos. To y_1/2 den einai idio me 
                             ! ayto pou pirame ston ypologismo tou k2
      
c...Ypologismos tou k4
      y(1)   = yi(1)+k3y(1)*h      ! H taxytita kai thesi sto telos tou 
      y(2)   = yi(2)+k3y(2)*h      ! diastimatos (oloklirwro vima)
                                   ! xrisimopoiontas tin paragwgo sto meso 
                                   ! tou diastimatos apo to k3
      
      k4y(1) = d1y(t+h,y)     ! Paragwgoi thesis kai taxytitas sto telos
      k4y(2) = d2y(t+h,y)     ! diastimatos 
      
c... Telika apotelesmata efarmogis tis methodou
      yf(1) = yi(1)+(k1y(1) + 2*k2y(1) + 2*k3y(1) + k4y(1))*h/6.0
      yf(2) = yi(2)+(k1y(2) + 2*k2y(2) + 2*k3y(2) + k4y(2))*h/6.0
      
      Return
      End


c===============================================================
      real*8 function interpolate(x0,x1,y0,y1,yfin)
c==============================================================
c  Dinontas tis suntetagmenes 2 simeiwn A(x0,y0) kai B(x1,y1)
c  xrisimopoioume tin eksiswsi tis eytheias pou perna apo ta 
c  2 simeia gia na broume tin x i tin y syntetagmeni enos tritou 
c  simeiou pou vrisketai stin eytheia kai tou opoiou kseroume
c  tin mia apo tis 2 syntetagmenes
c===============================================================
c  Stin prokeimeni periptwsi xrisimopoioume ti grammiki paremvoli
c  gia 2 periptwseis. Gia na vroume to xrono anodou/kathodou me 
c  vasi tin taxutita kai gia na vroume to megisto upsos me vasi
c  tin taxytita. Epomenws ta simeia mas tha exoun suntetagmenes
c  t kai u stin 1-i periptwsi kai h kai u sti 2-i periptwsi.
c  Epomenws to rolo tis x metavlitis paizei o xronos t
c  kai to rolo tis y metavlitis i taxytita tou swmatos (1-periptwsi)
c  enw to rolo tis x metavlitis sti 2-i periptwsi paizei 
c  i thesi tou swmatos kai tis y metavlitis i taxytita.  
c==============================================================
      implicit none
      real*8 x0, x1, y0, y1, xfin, yfin
      
      xfin = x0 + (x1 - x0)*(yfin-y0)/(y1 - y0)
      
      interpolate = xfin
      
      return
      end
      

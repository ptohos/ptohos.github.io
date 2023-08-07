      program bouncingballs
c===========================================
c To programma ayto meleta tin kinisi
c 2 mpalwn pou kinountai stin katakoryfi
c dieythunsi kai erxontai se sygkrousi
c metaksu tous i me to edafos. 
c Arxika i mia mpala brisketai se 
c megalutero upsos apo tin alli
c kai afinontai na kinithoun pros to 
c edafos
c Analoga me to logo mazwn twn 2 swmatwn
c i kinisi pou ekteloun oi mpales mporei 
c na ginei xaotiki. 
c H eksiswseis kinisis twn duo swmatwn 
c lunontai me tin methodo Verlet-taxytitas
c========================================== 
      implicit none
      real*8 m1, m2, g, t, tmax, dt
      real*8 r1, r2
      real*8 x1, x2, v1, v2
      real*8 x1_new, x2_new, t_new
      real*8 x1_prev, x2_prev, t_prev
      real*8 v1_prev, v2_prev
      real*8 v1_new, v2_new
      real*8 v1_n, v2_n
      real*8 xkr, tkr, dtnew
      real*8 deltax0, deltax
      real*8 A1, A2, A3
      real*8 fraction, distance
      real*8 interpolate
      character*30 filename
      parameter(g=9.81D0)

      print*,'Dwse tis mazes twn 2 swmatwn'
      read*,m1, m2
      print*,'Dwse tis aktines twn 2 swmatwn'
      read*,r1, r2
      print*,'Dwse tis arxikes taxytites twn 2 swmatwn'
      read*,v1,v2
      print*,'Dwse tis arxika upsi twn 2 swmatwn'
      read*,x1,x2
      print*,'Dwse to xroniko diastima meletis tis kinisis'
      read*,tmax
      print*,'Dwse to xroniko vima gia tin kinisi twn swmatwn'
      read*,dt

      write(6,30)r1,r2,m1,m2,v1,v2,x1,x2,tmax,dt
 30   format(1x,40('='),/,1x,'Arxikes sunthikes gia tin kinisi',/,
     &       3x,'Mpala 1', 8x,'Mpala 2',/,
     &       1x,'aktina:',F4.1,6x,'aktina:',F4.1,/,
     &       1x,'maza:  ',F4.1,6x,'maza:  ',F4.1,/,
     &       1x,'u0:    ',F4.1,6x,'u0:    ',F4.1,/,
     &       1x,'x0:    ',F4.1,6x,'x0:    ',F4.1,/,1x,
     &       'Xroniko diastima:[0,',F4.0,']sec',1x,'dt= ',F5.3,'sec',/,
     &       1x,40('='),/)

      filename = 'hm04_prob3_case2.dat'
      if (m1/m2 .eq. 1) filename='hm04_prob3_case1.dat'
      open(unit=60,file=filename,status='unknown')
c
c....Suntelestes gia tis krouseis
c
      A1 = (m1-m2)/(m1+m2)
      A2 = 2.0D0*m2/(m1+m2)
      A3 = 2.0D0*m1/(m1+m2)

      t  = 0.0D0
 20   format(1x,f7.3,2(2x,f7.5),2(2x,f8.5))
      do while (t.le.tmax)
         write(60,20)t, x1, x2, v1, v2
         x1_prev = x1
         x2_prev = x2
         v1_prev = v1
         v2_prev = v2
         t_prev  = t
c... H methodos Verlet-taxutitas me statheri epitaxunsi einai apli
         x1_new = x1 + v1*dt - 0.5*g*dt**2
         x2_new = x2 + v2*dt - 0.5*g*dt**2
         v1_new = v1 - g*dt
         v2_new = v2 - g*dt
         t_new  = t + dt
c...Elegxos krousis tis xamiloteris mpalas me to edafos
         if (x1_new.le.r1) then
            xkr = r1
            tkr = interpolate(x1_prev,t_prev,x1_new,t_new,xkr)
            x1_new = xkr
            x1_prev= xkr
            dtnew  = tkr - t_prev   !<< Tropopoiisi tou xronikou vimatos
            v1_new = v1 -g*dtnew    !<< wste to x1_new na antistoixei
            v1_new = -v1_new        !<< sto simeio krousis. Allagi taxutitas
            v1_prev= v1_new
            x2_new = x2 + v2*dtnew - 0.5*g*dtnew**2
            v2_new = v2 - g*dtnew
            t_new  = t + dtnew
         endif
c...Elegxos krousis metaksu twn duo swmatwn
         if ((x2_new - x1_new) .le. (r1+r2)) then
            distance = x2_new - x1_new
            fraction = ((r1+r2)-distance)/distance
            x1       = x1_new - (1d0-m1/(m1+m2))*fraction*distance
            x2       = x1_new + (r1+r2)
            if (x1.lt.r1) then 
               x1 = r1
               x2 = r1+r2
            endif
            tkr = interpolate(x1_prev,t_prev,x1_new,t_new,x1)
            dtnew = tkr - t_prev
            v1_new = v1_prev - g*dtnew
            tkr = interpolate(x2_prev,t_prev,x2_new,t_new,x2)
            dtnew = tkr - t_prev
            v2_new = v2_prev - g*dtnew
            v1     = A1*v1_new + A2*v2_new
            v2     = A3*v1_new - A1*v2_new
            v1_new = v1
            v2_new = v2
            x1_new = x1
            x2_new = x2
         endif
         x1 = x1_new
         x2 = x2_new
         v1 = v1_new
         v2 = v2_new
         t  = t_new
      enddo
      end

      real*8 function interpolate(x0,t0,x,t,xpref)
      real*8 x0,t0,x,t,xpref
      real*8 slope
      slope = (x-x0)/(t-t0)
      if (slope .eq. 0) then 
         interpolate = t
      else
         interpolate = t0 + (xpref-x0)/slope
      endif
      return
      end

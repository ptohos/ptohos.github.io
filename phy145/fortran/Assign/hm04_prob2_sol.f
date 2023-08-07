c==================================================================
      program population
c==================================================================
c Lusi gia to provlima ayksisis enos pluthismou ston 
c opoio periexetai enas oros meiwsis tou upsomenos sto 
c tetragwno. 
c dN/dt = a*N - b*N^2
c
c H arithmitiki lusi tou provlimatos ginetai me ti methodo tou
c endiamesou simeiou
c
c H analutiki lusi tou provlimatos einai 
c N(t) = N0 * a * exp(a*t)/{a - b * N0 + b * N0 * exp(at)}
c
c To programma dexetai san parametrous eisagwgis 
c  1) To stathero oro a
c  2) To stathero oro b
c  3) Ton arxiko plithysmo N0
c  4) To xroniko vima dt
c  5) To megisto xroniko diastima tmax
c
c To apotelesma twn upologismwn dinontai sto file 'plithismos.dat'
c To executable tha prepei na to treksete 2 fores 
c gia tis 2 diaforetikes periptwseis twn timwn a kai b
c  A) Periptwsi:  A = 10, B=3, N0 = 10, dt = 0.001mines, tmax = 12mines
c  B) Periptwsi:  A = 10, B=0.01, N0 = 1000, dt=0.001mines tmax = 12mines
c===================================================================
      implicit none

      Logical doit, first
      Real afac, bfac, N0
      Real dt, t, t0, tmax 
      Real t_in, t_fin
      Real N_mid, N_in, N_fin
      Real theory
      common/const/afac,bfac,N0
c
      real theoretical     ! Function gia ti theoretiki lusi
c
      Print *,' Dwste to max xroniko diastima [tmax]'
      Read *,tmax
      Print *,' Dwste to xroniko vima [dt]'
      Read *, dt
      Print *,' Dwste tin arxiki xroniki stigmi'
      Read *, t0
      Print *,' Dwste tin timi tis statheras a'
      Read *, afac
      Print *,' Dwste tin timi tis statheras b'
      Read *, bfac
      Print *,' Dwste ton arxiko plithismo N(t=0)'
      Read *, N0

      t_in   = t0     ! Arxiki xroniki stigmi
      N_in   = N0
      theory = theoretical(t_in)
      N_mid  = N_in
      
      doit   = .true.
      open(unit=10,file='hm04_prob2.dat',status='unknown')

      do while (doit) 

c... Ektupwsi apotelesmatwn tis proigoumenis xronikis stigmis
         write(10,20)t_in, N_mid, theory

c... Klisi tis subroutine rk4 gia efarmogi tis methodou R-K
         t_fin = t_in + dt
         call midpoint(t_in, t_fin, N_in, N_fin)

c... Epomeno vima 
         t_in   = t_fin
         N_in   = N_fin
         theory = theoretical(t_in)
         N_mid  = N_in

c... Elegxos an ftasame sti megisti epitrepomeni stigmi
         if (t_in.gt.tmax.or.theory.lt.0) doit = .false.
      enddo
 20   Format(1x,f7.5,2(2x,F10.5))
      close(20)
      end


c==============================================
      real function dNdt(t,N)
c==============================================
c   H paragwgos dN/dt = a*N - b*N*N
c==============================================
      implicit none
      Real N, t
      real afac, bfac, N0
      common/const/afac,bfac,N0

      dNdt = afac*N - bfac*N*N

      return
      end

c==========================================================
      Subroutine midpoint(ti,tf,yi,yf)
c==========================================================
c     I methodos tou endiamesou simeiou
c==========================================================
c... Parametroi eisagwgis
c
c     1) ti    - arxikos xronos
c     2) tf    - telikos xronos meta to vima t_in + dt
c     3) yi    - arxikos plythismos ti xroniki stigmi ti
c
c... Parametros epistrofis
c        yf    - telikos plythismos ti xroniki stigmi tf
c
c... Aparaitito na ypologistei i synartisi tis paragwgou
c    dNdt(t,y) - synartisi dN/dt = dy/dt
c==========================================================
      implicit none
      Real ti, tf 
      Real yi, yf, y
      Real dt, t
      Real k1, k2

c... H synartisi tis paragwgou
      Real dNdt

      dt  = tf-ti             ! vima 
      t   = ti

      k1  = dNdt(t,yi)        ! H paragwgos sto simeio (ti,yi)
      y   = yi + dt*k1        ! Vima euler sto telos tou diastimatos 
                              ! y = plithismos ti stigmi 

      k2 = dNdt(t+dt,y)       ! H paragwgos sto simeio (ti+dt,y)

      yf = yi + (k1+k2)*dt/2  ! Vima euler xrisimopoiontas ti mesi timi twn
                              ! twn 2 paragwgwn sto (ti,yi) kai (ti+dt,yi+1)
      
      Return
      End

c===========================================================
      real function theoretical(time)
c===========================================================
      implicit none
      real     time
      real     afac, bfac, N0
      common/const/afac,bfac,N0

      theoretical = N0*afac*exp(afac*time)
      theoretical = theoretical/(afac-bfac*N0+N0*bfac*exp(afac*time))

      return
      end

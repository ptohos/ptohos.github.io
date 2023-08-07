c-------------------------------------------------
      program efaptomeni
c-------------------------------------------------
c To problima einai kai pali euresis tis rizas
c mias eksiswsis kai mporeite na xrisimopoiisete
c mia apo tis duo methodous pou kserete. 
c H dyskolia tis askisis einai na vroume tin 
c eksiswsi pou tha prepei na lusoume.
c Apo to provlima kseroume oti i efaptomeni tis 
c elleipsis sto simeio pou psaxnoume (xo,yo) perna
c kai apo to simeio A me suntetagmenes (xA,yB). 
c Epomenws i eksiswsi tis eutheias tis efaptomenis
c grafetai ws: 
c     klisi = (yo-yA)/(xo-xA)                    (1)
c H klisi omws tis efaptomenis einai isi me tin 
c paragwgo tis eksiswsis tis elleipsis sto simeio (xo,yo) 
c H eksiswsi tis elleipsis einai x^2/a + y^2/b = 1 opote
c kai i paragwgos tis einai 
c     y' = -(b/a)(x/y)  
c kai sto (xo,yo) tha einai y'=-(b/a)(xo/yo)     (2)
c Apo (1) kai (2) exoume:
c     -(b/a)(xo/yo) = (yo-yA)/(xo-xA)            (3)
c To simeio ayto ikanopoiei kai tin eksiswsi tis elleipsis
c      yo^2/b = 1 - xo^2/a => bxo^2+ayo^2 = ab   (4)
c Kanontans tis prakseis stin (3) kai antikathistontas tin (4) 
c tha paroume:
c      ayoyA + bxoxA = ab                        (5)
c Epomenws exoume to systima:
c      (ayo)yA + (bxo)xA = ab=> (bxo)xA = ab - (ayo)yA
c kai  bxo^2 + ayo^2 = ab => bxo^2 = ab - ayo^2
c Ypswnoume tin 1-i eksiswsi sto tetragwno
c  (bxo)^2xA^2 = (ab)^2+(ayo)^2yA^2 - 2(a^2byo)yA =>
c  (bxo^2)bxA^2 = (ab)^2+(ayo)^2yA^2 - 2(a^2byo)yA 
c Antikathistoume to bxo^2 apo tin eksiswsi tis ellipsis 
c (2-i eksiswsi tou sustimatos)
c  (bxA^2)(ab-ayo^2) = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo =>
c  ab^2xA^2 - (abxA^2)yo^2 = (ab)^2+(ayA)^2yo^2 - 2(a^2byA)yo =>
c  Meta apo algebrikes prakseis kataligoume:
c
c  yo^2(bxA^2+ayA^2) - (2abyA)yo + b^2(a-xA^2) = 0
c
c Alla xA = -8, yA = -1 enw a=25 kai b=16. Antikatastasi dinei:
c      1049yo^2 + 800yo - 9984                   (6)
c Theloume epomenws na vroume tis rizes tis eksiswsis aytis
c me ti methodo tou Newton i me ti methodo tis dixotomisis
c Analytika oi rizes tis eksiswsis aytis einai:
c   yo(1) = +2.727227
c   yo(2) = -3.489858
c Kai profanws theloume ti thetiki riza opws zita i askisi.
c Kserontas to yo mporoume na broume to xo apo tin (5)
c   xo = (ab - ayAyo)/(bxA) = (400 + 25*2.727227)/(-8*16) = -3.6576615 
c Enw i klisi tis efaptomenis sto simeio ayto tha einai:
c   y' = -(16/25)(-3.6576615/2.727227) = 0.85834563
c Epomenws i eksiswsi tis eytheias tha einai:
c   y = 0.85834563*(x+8) - 1
c================================================================
      implicit none
      integer niter, icase
      Double precision  x1, x2, toler
      Double precision  sol, xcoord
      
      Print *, ' Give the interval that brackets the root [y1,y2]'
      Print *, ' The above interval refers to the value of y'
      Read *, x1, x2
      Write(6,20) x1,x2
 20   Format(1x,'Eyresi tis lusis tis eksiswsis sto diastima [',E15.8,
     &       1x,',',E15.8,']')
      Print *, ' Dwste tin epithimiti akriveia tis lusis'
      Read *, toler

      call rtnewt(x1,x2,toler,sol,niter,icase)
      If (ICASE.eq.0) then 
         Write(6,30) sol, niter, xcoord(sol),sol 
      ELSE IF (ICASE.eq.1) then 
         WRITE(6,31)
      ELSE IF (ICASE.eq.2) then
         WRITE(6,32) niter
      ENDIF
 30   Format(1x,' H riza tis eksiswsis einai :',E20.10,/,
     &       1x,' Xreiastikan',1x,I2,1x,'epanalipseis',/,
     &       1x,' Oi suntetagmenes tou simeioy epafis einai:('
     &            E18.11,',',E18.11,')')
 31   Format(1x,' Provlimata stin euresi tis lusis :',/,
     &          ' x pire times eksw apo to arxiko diastima')
 32   Format(1x,' Den Uparxei sygklisi tis methodou !',/,
     &          ' Meta apo',1x,i2,'epanalipseis')
      end
c=================================================
      DOUBLE PRECISION FUNCTION XCOORD(sol)
c=================================================
      implicit none
      double precision sol
      xcoord = (400d0 + 25D0*sol)/(-8d0*16d0)
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION FUNC(x)
c=================================================
c H synartisi ti lusi tis opoias epithimoume
c=================================================
      implicit none
      double precision x
      func = 1049*x**2 + 800*x - 9984     ! H sunartisi pou theloume
      return
      end

c=================================================
      DOUBLE PRECISION FUNCTION DERIVFUNC(x)
c=================================================
c H paragwgos tis synartisis
c=================================================
      implicit none
      double precision x
      derivfunc = 2098*x + 800       ! H paragwgos tis sunartisis
      return
      end

c==================================================================
      SUBROUTINE RTNEWT(X1,X2,TOL,SOLUTION,NITER,ICASE)
c==================================================================
c H subroutine pou periexei ti methodo Newton-Rapshon
c H riza tha prepei na brisketai sto diastima [x1,x2]
c kai tha prepei na exei akriveia +-Tol
c==================================================================
c  Input arguments:  X1,X2: lower(upper) edges 
c                    tou diastimatos pou periexei ti lusi
c                    TOL: akriveia tis epithymitis lusis
c  Output arguments:
c                    NITER: Arithmos epanalipsewn
c                    SOLUTION: Lusi tis eksiswsis
c                    CASE: Periptwsi tou ti sunevei
c                          0 i lusi brethike kanonika
c                          1 pidigma eksw apo to arxiko diastima
c                          2 mi sugklisi. Arithmos epanalipsewn 
c                            megaluteros apo epitrepto orio. 
c==================================================================
      implicit none
      INTEGER          J, ICASE
      INTEGER          NITER, NITERMAX
      DOUBLE PRECISION SOLUTION, X
      DOUBLE PRECISION X1, X2, TOL
      DOUBLE PRECISION FUNC, DERIVFUNC ! H synartisi kai i paragwgos tis
      PARAMETER(NITERMAX=30)           ! megistos arithmos epanalipsewn
      DOUBLE PRECISION DX

      NITER    = 0
      x = 0.5*(x1 + x2)              ! Theoroume to meso to diastimatos 
                                     ! [x1,x2] sa lusi tis eksiswsis

      DO 100 J = 1, NITERMAX
         NITER = NITER + 1
         DX = FUNC(x)/DERIVFUNC(x)   ! Efarmogi: X_(k+1) = X_k - F(x)/F'(x)
         x = x - dx                  ! opote X_(k+1) - X_k = -F(x)/F'(x) =>
                                     ! X_k - X_(k+1) = F(x)/F'(x) = DX
                                     ! DX = X_(k) - X_(k+1)=> X_(k+1)=X_k-dx
                                     ! DX antiproswpeuei ti diafora metaksu
                                     ! tis lisis kata tin epanalipsi k (X_k)
                                     ! kai amesws epomeni epanalipsi k+1
         if ((x - x2) * (x1 - x).lt.0.D0) then
            Print *,' H lysi pidikse eksw apo to arxiko diastima'
            ICASE = 1
            solution = x
            RETURN
         ENDIF
         IF (abs(DX).LT.TOL) THEN         ! Lusi me epithimiti akribeia
            ICASE = 0 
            solution = x
            RETURN
         ENDIF
 100  CONTINUE
c
c An ftasoume sto simeio ayto simenei oti kseperasame to megisto
c arithmo epanalipsewn tis methodou opote tupwnoume kapoio minima
c
      ICASE = 2
      solution = x
      RETURN
      END

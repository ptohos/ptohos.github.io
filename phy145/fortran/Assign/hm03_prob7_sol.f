c-------------------------------------------------
      program solution
c-------------------------------------------------
c--------------------------------------------------
      implicit none
      integer niter, icase
      Double precision  x1, x2, toler
      Double precision  sol
      
      Print *, ' Give the interval that brackets the root [x1,x2]'
      Read *, x1, x2
      Write(6,20) x1,x2
 20   Format(1x,'Eyresi tis lusis tis eksiswsis sto diastima [',E15.8,
     &       1x,',',E15.8,']')
      Print *, ' Dwste tin epithimiti akriveia tis lusis'
      Read *, toler

      call rtnewt(x1,x2,toler,sol,niter,icase)
      If (ICASE.eq.0) then 
         Write(6,30) sol, niter
      ELSE IF (ICASE.eq.1) then 
         WRITE(6,31)
      ELSE IF (ICASE.eq.2) then
         WRITE(6,32) niter
      ENDIF
 30   Format(1x,' H riza tis eksiswsis einai :',E15.8,/,
     &       1x,' Xreiastikan',1x,I2,1x,'epanalipseis')
 31   Format(1x,' Provlimata stin euresi tis lusis :',/,
     &          ' x pire times eksw apo to arxiko diastima')
 32   Format(1x,' Den Uparxei sygklisi tis methodou !',/,
     &          ' Meta apo',1x,i2,'epanalipseis')
      end

c=================================================
      DOUBLE PRECISION FUNCTION FUNC(x)
c=================================================
c H synartisi ti lusi tis opoias epithimoume
c=================================================
      implicit none
      double precision x
      double precision func1, func2
      func = func1(x) - func2(x)  ! H sunartisi pou theloume
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION FUNC1(X)
c=================================================
      implicit none
      double precision x
      func1 = 4*exp(-2*x)
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION FUNC2(X)
c=================================================
      implicit none
      double precision x
      func2 = 0.5*x**2
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION DERIVFUNC(x)
c=================================================
c H paragwgos tis synartisis
c=================================================
      implicit none
      double precision x
      double precision derivfunc1, derivfunc2
      derivfunc = derivfunc1(x) - derivfunc2(x) ! H paragwgos
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION DERIVFUNC1(x)
c=================================================
      implicit none
      double precision x
      derivfunc1 = -8*exp(-2*x)
      return
      end
c=================================================
      DOUBLE PRECISION FUNCTION DERIVFUNC2(x)
c=================================================
      implicit none
      double precision x
      derivfunc2 = x
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

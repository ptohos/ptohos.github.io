      program root_newton_general
      implicit none
      INTEGER niter, icase
      Double precision  x1, x2, tol
      Double precision  sol
      
      Print *, ' Give the interval that brackets the root [x1,x2]'
      Read *, x1, x2
      Write(6,20) x1,x2
 20   Format(1x,'Eyresi tis lusis tis eksiswsis sto diastima [',E15.8,
     &       1x,',',E15.8,']')
      Print *, ' Dwste tin epithimiti akriveia tis lusis'
      Read *, tol

      call newton_general(x1,x2,tol,sol,niter,icase)
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
     &          ' H lusi den perikleietai sto diastima')
 32   Format(1x,' Den Uparxei sygklisi tis methodou !',/,
     &          ' Meta apo',1x,i2,'epanalipseis')
      
      END
c============================================================
      DOUBLE PRECISION FUNCTION FUNC(X)
c============================================================
      IMPLICIT NONE
      DOUBLE PRECISION X
      FUNC = cos(x)-x
      RETURN
      END

c============================================================
      DOUBLE PRECISION FUNCTION DERIVFUNC(X)
c============================================================
      IMPLICIT NONE
      DOUBLE PRECISION X
      DERIVFUNC = -(sin(x)+1d0)
      RETURN
      END


c============================================================
      SUBROUTINE newton_general(x1,x2,tol,solution, niter, icase)
c============================================================
c Ayti i subroutine upologizei ti riza mias 
c eksiswsis (synartisis) me ti methodo tou 
c Newton-Raphson.
c Otan i euresi tis lusis den sugklinei arketa
c grigora eksaitias tis klisis tis synartisis 
c i otan i euresi ksefeugei apo ta oria tote 
c i bisection methodos xrisimopoieitai
c============================================================
      implicit none
      
      INTEGER MAXIT
      PARAMETER(MAXIT = 100)            ! megistos arithmos epanalipsewn
      INTEGER ICASE, J
      INTEGER NITER
      DOUBLE PRECISION X1, X2, TOL      ! Ta oria tou diastimatos pou periexei
                                        ! ti lysi kai i epithimiti arkiveia
      DOUBLE PRECISION SOLUTION
      DOUBLE PRECISION FUNC, DERIVFUNC  ! H synartisi kai i paragwgos tis

      DOUBLE PRECISION FL, FH, F, DFL, DFH, DF
      DOUBLE PRECISION X, XL, XH, SWAP, TEMP
      DOUBLE PRECISION DX, DXOLD
      
      FL  = FUNC(X1)                 ! H timi tis synartisis sto X1
      DFL = DERIVFUNC(X1)            ! kai tis paragwgou tis
      FH  = FUNC(X2)                 ! H timi tis synartisis sto X2
      DFH = DERIVFUNC(X2)            ! kai tis paragwgou tis
      
      IF( FL*FH.GE.0.D0) THEN
         ICASE = 1                   ! H lusi den periexetai sto diastima
         RETURN 
      ENDIF

      IF(FL.LT.0.)THEN               ! To x1 einai to katw orio tou 
        XL=X1                        ! diastimatos afou f(x1)<0
        XH=X2
      ELSE                           ! Diaforetika to katw orio prepei 
        XH=X1                        ! na einai to x2 kai xreiazetai 
        XL=X2                        ! na enallaksoume ta simeia X1 kai X2
        SWAP=FL                      ! etsi wste F(XL)<0 
        FL=FH
        FH=SWAP
      ENDIF

      X     = 0.5*(X1+X2)            ! Arxiki ypothetiki lysi sto meso
      DXOLD = ABS(X2-X1)             ! H timi toy eurous tou diastimatos
                                     ! prin vrethei to neo diastima
      DX    = DXOLD                  ! kai i nea timi tou eurous tou diastimatos
      F     = FUNC(X)                ! H timi tis synartisis sti riza
      DF    = DERIVFUNC(X)           ! kai tis paragwgou tis

      DO 11 J=1,MAXIT
        IF( ((X - XH)*DF - F) * ((X - XL)*DF - F).GE.0.   ! Xrisimopoiisi tis
     &      .OR. ABS(2. * F) .GT. ABS( DXOLD*DF ) ) THEN  ! bisection methodou
                                                          ! an i methodos Newton
                                                          ! dwsei "lysi" eksw
                                                          ! apo to diastima i
                                                          ! an den sygklinei 
                                                          ! grigora
          DXOLD  = DX
          DX     = 0.5*(XH-XL)
          X      = XL + DX
          IF(XL .EQ. X) THEN           ! H allagi sti timi tis rizas einai  
             SOLUTION = X              ! polu mikri 
             ICASE    = 0
             RETURN
          ENDIF
        ELSE                           ! Diaforetika to vima tis methodou
          DXOLD  = DX                  ! Newton einai epitrepto kai to 
          DX     = F/DF                ! xrisimopoioume sumfvna me ti methodo
          TEMP   = X
          X      = X - DX
          IF(TEMP.EQ.X ) THEN 
             SOLUTION = X
             ICASE = 0
             RETURN
          ENDIF
        ENDIF
        IF ( ABS(DX) .LT. TOL) THEN    ! Epithymiti akriveia epiteyxthike
           SOLUTION = X 
           ICASE    = 0
           RETURN
        ENDIF 

        F  = FUNC(X)
        DF = DERIVFUNC(X)
        NITER = NITER + 1

        IF( F .LT. 0.) THEN            ! H timi tis synartisis sti lusi aytis
          XL = X                       ! tis epanalipsis einai arnitiki opote
          FL = F                       ! ayto apotelei to aristero diastima
        ELSE
          XH = X                       ! Diaforetika apotelei to anwtero 
          FH = F                       ! orio tou diastimatos
        ENDIF                          ! Kratame etsi ti lusi panta se ena
                                       ! diastima
11    CONTINUE
      ICASE = 2                        ! megistos arithmos epanalipsewn
      RETURN
      END

c===================================
      program PoissonNumbers
c===================================
c Gia ti periptwsi tis mesis timis 1.69
c 10 bins einai arketa enw gia ti mesi
c timi 11.48 xrisimopoioume 25 bins
c trexontas gia 10000 prospatheies.
c Me to tropo ayto ta simeia ston ajona
c x fainontai na einai akeraia. 
c===================================
      implicit none
      real xmean, xsigma
      integer nshots, nmax
      integer inumb, ierror
      parameter(nmax=100000)
      real x(nmax)
      integer j, nbins, nbinsmax
      parameter(nbinsmax=100)
      integer freq(nbinsmax)
      real    xval(nbinsmax)
      integer iseed
      data iseed/12345/

 30   print *,'Prosdioriste ton arithmo twn peiramatwn'
      read *,nshots
      if (nshots.gt.nmax) then
         print *,'Dwste mikrotero arithmo peiramatwn'
         print *,'diaforetika allakste to megethos tou pinaka'
         goto 30
      endif
      print *,'Dwste ti mesi timi tis Poisson katanomis'
      read *,xmean
      print *,'Dwste ton arithmo twn bins'
      read *,nbins

      call srand(iseed)
      open(unit=20,file='poisson.dat',status='unknown')
      do j =1, nshots
         call PoissDev(xmean,inumb,ierror)
         if (ierror.eq.0) then 
            x(j) = float(inumb)
         endif
      enddo
      call histogram(x,nshots,nbins,freq,xval)
      do j = 1, nbins
         write(20,100)xval(j)-0.5,freq(j)
      enddo
 100  format(1x,f8.5,2x,I6)
      close(20)
      end

c====================================================
      SUBROUTINE POISSDEV(AMU, N, IERROR)
c====================================================
c Subroutine gia dimiourgia enos tyxaiou akeraiou 
c arithmou N>0 symfvna me thn Poissonian katanomi:
c Prob(N) = exp(-amu) * amu**N / N!
c opoy amu > 0 i mesi timi tis katanomis kai dinetai
c apo to xristi. 
c
c An den uparxei problima IERROR = 0
c diaforetika epistrefei IERROR = 1 an AMU<=0
c================================================
      IMPLICIT NONE
      INTEGER N
      INTEGER IERROR
      REAL AMU, AMUOL, AMAX
      REAL EXPMA, XRAN
      REAL RAND, PIR
      DATA AMUOL/-1./
      DATA AMAX/100./
      IF (AMU .GT. AMAX)  GOTO 500
      IF (AMU .EQ. AMUOL) GOTO 200
      IF (AMU .GT. 0.)    GOTO 100
c
c... H mesi timi prepei na einai thetiki
      IERROR = 1
      N = 0
      RETURN

c...Apothikeysi toy ekthetikou gia peretairw kliseis
 100  IERROR = 0
      AMUOL  = AMU
      EXPMA  = EXP(-AMU)
 200  PIR    = 1.
      N = -1
 300  N = N + 1
      PIR = PIR * RAND()
      IF (PIR .GT. EXPMA) GOTO 300
      RETURN

c...Proseggisi me gaussian katanomi an AMU > AMAX
 500  XRAN = RAND()
      N = XRAN*SQRT(AMU) + AMU + 0.5
      RETURN

c...An o xristis thelei na thesei ti timi AMAX gia gaussian proseggisi
c.. gia na ginei xreiazetai na kalesei kaneis to entry point: CALL POISET(VAL)
      ENTRY POISET(AMU)
      AMAX = AMU 
      RETURN
      END

c------------------------------------------------------------
      SUBROUTINE Histogram(X,N,BINS,H,XVAL)
!------------------------------------------------------------
! Ayti i subroutine sas boitha na dimioyrgisete ena pinaka
! ston opoio apouhkeyete ti syxnotita me tin opoia emfanizontai
! oi tyxaioi arithmoi X. Xwrizei kapoio diastima [xmin,xmax]
! se isa ypodiastimata (bins) me eyros binw. An o arithmos 
! einai metaksy enos ypodiastimatos [x_i,x_i+1] tote ayksanoume
! to plithos twn tyxaivn arithmvn sto ypodiastima ayto kata 1 
! Epistrefei to pinaka H pou exei ti syxnotita emfanisis twn X
! kathws kai to pinaka twn timwn twn upodiastimatwn tou X (sto XVAL) 
!------------------------------------------------------------
  	IMPLICIT NONE
  	INTEGER  N
	INTEGER BINS
  	REAL X(N), XVAL(BINS)
  	REAL   MIN, MAX, BINWIDTH
	REAL   MINVA, MAXVA
	INTEGER H(BINS),BIN,I,J,K,MaxH

	DO I = 1, BINS
	   H(I)=0
	ENDDO
	MIN = MINVA(X,N)
  	MAX = MAXVA(X,N)
  	BINWIDTH=(MAX-MIN)/REAL(BINS)
  	DO I=1,N
    	  BIN=1+(X(I)-MIN)/BINWIDTH       ! Briskoume se poio diastima 
                                          ! anikei i timi x(i) 
	  IF ( BIN .LT. 1 ) BIN=1         ! Check for underflows
	  IF ( BIN .GT. BINS ) BIN=BINS   ! Check for overflows
	  H(BIN) = H(BIN)+1               ! Ayksanoume ton arithmo sto 
                                          ! sygkekrimeno diastima
	  XVAL(BIN) = MIN+BINWIDTH/2+(BIN-1)*BINWIDTH ! To meso tou diastimatos [x_i,x_i+1]
	END DO
	RETURN
	END

	REAL FUNCTION MINVA(X,N)
	IMPLICIT NONE
	INTEGER I, N
	REAL   MIN, X(N)
	MIN = X(1)
	DO I = 1, N
	   IF (X(I).LT.MIN) THEN
           MIN = X(I)
	   ENDIF
	ENDDO
	MINVA = MIN
	RETURN
	END

	REAL FUNCTION MAXVA(X,N)
	IMPLICIT NONE
	INTEGER I,  N
	REAL   MAX, X(N)
	MAX = X(1)
	DO I = 1, N
	   IF (X(I).GT.MAX) THEN
           MAX = X(I)
	   ENDIF
	ENDDO
	MAXVA = MAX
	RETURN
	END

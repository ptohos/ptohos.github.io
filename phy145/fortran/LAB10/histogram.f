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

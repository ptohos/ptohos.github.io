c=========================================================
	PROGRAM mc_rejection
c=========================================================
c... Methodos Monte Carlo aporripsis gia na paroume
c....tyxaious arithmous me katanomi Py(y) = exp(-y**2).
c=========================================================
	IMPLICIT NONE
	INTEGER I, N, ISEED, M
	PARAMETER(N=10000000)
	REAL    Z(N)
	REAL    X, Y, Ptest
	REAL    PY_MAX, YMIN, YMAX
c...Metavlites gia t
	integer nbins
	parameter(nbins=100)    ! 100 diastimata epomenws to kathena tha 
                                ! exei euros 20/100 = 0.2 afou to diastima
                                ! twn timwn toy y einai [-10,10]->Dy=20
	real yval(nbins)
	integer freq(nbins)

	REAL    PY		! H epithymiti synartisi katanomis Py

	ISEED  = 123456		! Timi seed toy gennitora
	call srand(iseed)

	M      = 0		! Arxiki timi metriti gia dektes times tou y
	Py_max = 1		! Megisti timi tis Py [dP/dy=0 gia y=0]
	YMIN   =-10.0		! Eyros timwn y [-10,10]
	YMAX   = 10.0

	open(unit=20,file='mc_rejection.dat',status='unknown')
	DO I = 1, N
	   x = rand()
	   y = rand()
	   y = ymin + (ymax - ymin)*y   ! Metatropi sto diastima [-10,10]
	   Ptest = x*Py_max	! tuxaia metavliti Ptest sto [0,Py_max]
	   IF ( Py(y) > Ptest) THEN
	      M=M+1		! H timi y perase to test
	      Z(M)=y		! kai tin kratame sto z(m)
	   END IF
	END DO
	print *,'Dokimasame ',N,' times apo tis opoies perasane ',M
	print *,'Apodotikotita = ',M*100./N,'%'
	call histogram(z,m,nbins,freq,yval)
	do i = 1, nbins
	   write(20,*)yval(i), freq(i)
	enddo
	close(20)
	END
	
c================================================
 	REAL FUNCTION Py(y)
c================================================
c....H epithumiti synartisi katanomis
c================================================
	REAL Y
	Py = exp(-y**2)
	RETURN
	END

c===========================================================
	SUBROUTINE Histogram(X,N,BINS,H,XVAL)
c===========================================================
c Ayti i subroutine sas boitha na dimioyrgisete ena pinaka
c ston opoio apouhkeyete ti syxnotita me tin opoia emfanizontai
c oi tyxaioi arithmoi X. Xwrizei kapoio diastima [xmin,xmax]
c se isa ypodiastimata (bins) me eyros binw. An o arithmos 
c einai metaksy enos ypodiastimatos [x_i,x_i+1] tote ayksanoume
c to plithos twn tyxaivn arithmvn sto ypodiastima ayto kata 1 
c Epistrefei to pinaka H pou exei ti syxnotita emfanisis twn X
c kathws kai to pinaka twn timwn twn upodiastimatwn tou X (sto XVAL) 
c===========================================================
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

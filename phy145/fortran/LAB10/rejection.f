	PROGRAM Rejection
!--------------------------------------------------------
! Paradeigma tis methodou aporripsis
! gia ti synartisi Py(y) = y**2*exp(-y).
!--------------------------------------------------------
	IMPLICIT NONE
	INTEGER I, N, ISEED, M
	PARAMETER(N=40000)
	REAL    X(N), Y(N), Z(N), Ptest
	REAL    PY_MAX, YMIN, YMAX
	REAL    PY		! H synartisi Py

	ISEED  = 123456		! Timi seed toy gennitora
	call srand(iseed)
	M      = 0		! Arxiki timi metriti
	Py_max = 0.541		! Megisti timi tis Py [dP/dy=0 gia y=2]
	YMIN   = 0.0		! Eyros timwn y [0,10]
	YMAX   =10.0
	
	DO I = 1, N		! Dimiourgia zeugwn (X,Y) omoiomorfa 
	   X(I) = RAND()	! katanemimena metaksu [0,1]. 
	   Y(I) = RAND()	! Katopin metatropi twn Y metaksu [0,10]
	   Y(I) = YMIN + (YMAX - YMIN)*Y(I)
	ENDDO
	
	DO I = 1, N
	   Ptest=Py_max*X(I)	! tuxaia metavliti Ptest sto [0,Py_max]
	   IF ( Py( Y(I) ) > Ptest) THEN
	      M=M+1		! H y(i) perase to test
	      Z(M)=Y(I)		! kai tin kratame sto z(m)
	   END IF
	END DO
	END
	
 	REAL FUNCTION Py(y)
!-------------------------------------
!       H epithumiti synartisi katanomis
!-------------------------------------
	REAL Y
	Py = y**2*exp(-y)
	RETURN
	END

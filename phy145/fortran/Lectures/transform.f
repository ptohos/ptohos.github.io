	PROGRAM Transform
!--------------------------------------------------------
! Paradeigma tis methodou metasximatismou 
! gia tin synartisi Py(y) = y.
! H synartisi metasximatismou einai: sqrt(2x)
!--------------------------------------------------------
  	IMPLICIT NONE
  	INTEGER  N, ISEED
	PARAMETER(N=20000)
  	REAL R
	REAL RAN		! H synartisi tuxaiwn arithmwn
	
	OPEN(Unit=10,FILE="transform.data",status="unknown")
  	ISEED = 123456		! Arxiki timi seed 
	call srand(iseed)       ! Ksekinima akouthias tyxaiwn arithmwn
	DO I = 1, N		! Plithos tyxaiwn arithmwn 
	   X = RAND()	        ! Tyxaia timi
	   R = SQRT(2.0*X)
	   WRITE(10,*)X,R
	ENDDO
	END
	

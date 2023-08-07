	PROGRAM Minimal
!----------------------------------------------------------
!
!----------------------------------------------------------
	IMPLICIT NONE
	INTEGER I,ISEED
	REAL    R,RAN
	
  	ISEED=314159265		! Arxiko seed
	call srand(iseed)
  	DO I=1,10
	   R=RAND()		! RAN() einai mia sunartisi
	   PRINT *, R		! pou epistrefei ena random number.
	END DO
	
	END

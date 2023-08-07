	PROGRAM Minimal
!----------------------------------------------------------
! Gia ti dedomeni seed to programma epistrefei
! tin akolouthia:
!
!  0.1144350
!  0.9160240
!  0.8661048
!  0.9990742
!  0.0614151
!  0.8844953
!  0.2043324
!  0.0372450
!  0.4818531
!  0.1137583
!
!----------------------------------------------------------
	IMPLICIT NONE
	INTEGER I,ISEED
	REAL    R,RAN
	
  	ISEED=314159265		! Arxiko seed
  	DO I=1,10
	   R=RAN(ISEED)		! RAN() einai mia sunartisi
	   PRINT *, R		! pou epistrefei ena random number.
	END DO
	
	END

	REAL FUNCTION RAN(ISEED)
!--------------------------------------------------------------
! Epistrefei mia omoiomorfa tyxaia apoklisi metaksu 0.0 and 1.0.
! Symfwna me: Park and Miller's "Minimal Standard" random number
!           generator (Comm. ACM, 31, 1192, 1988)
!--------------------------------------------------------------
    	IMPLICIT NONE
    	INTEGER  ISEED
 	INTEGER IM, IA, IQ, IR
	REAL    AM
	PARAMETER(IM=2147483647, IA=16807, IQ=127773, IR= 2836)
	PARAMETER(AM=128.0/IM)
    	INTEGER K
    	K = ISEED/IQ
    	ISEED = IA*(ISEED-K*IQ) - IR*K
    	IF (ISEED .LT. 0) ISEED = ISEED+IM
    	RAN = AM*(ISEED/128)
	RETURN
	END

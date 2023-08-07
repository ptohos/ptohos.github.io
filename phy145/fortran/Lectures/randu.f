	PROGRAM IBM_RANDU
!----------------------------------------------------------
! Gia ti dedomeni timi seed to programma
! epistrefei tous parakatw tyxaious arithmous
!
!  0.0616391
!  0.7949819
!  0.6759571
!  0.8528126
!  0.6640903
!  0.6891235
!  0.5779092
!  0.9748247
!  0.8704975
!  0.4042856
!
!----------------------------------------------------------
	IMPLICIT NONE
	INTEGER I,ISEED
	REAL    R,RANDU
	
  	ISEED=314159265		! Arxiki timi gia seed
 
  	DO I=1,10		! 10 tyxaious arithmous
	   R=RANDU(ISEED)	! RANDU() synartisi pou
	   PRINT *, R		! epistrefei ena tyxaio arithmo
  	END DO

	END

	REAL FUNCTION RANDU(ISEED)
!---------------------------------------------
! RANDU dianemithike apo tin IBM to 1960 
! me ton akoloutho algorithmo:
!
!    X_(n+1) = ( 69539 x_n ) mod 2**31-1
!
! kai argotera (kalyteros)
!
!    X_(n+1) = ( 69069 X_n ) mod 2**31-1
!---------------------------------------------
	IMPLICIT NONE
	INTEGER  ISEED
	INTEGER  A, M
	PARAMETER(A=65069,M=2147483647)
	
  	ISEED = MOD(ISEED*A,M)
  	IF (ISEED.LT.0) ISEED = ISEED+M
  	RANDU = REAL(ISEED)/M
	RETURN
	END

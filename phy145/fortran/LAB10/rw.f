	PROGRAM Random_Walk
    	IMPLICIT NONE 
    	INTEGER I,J,N,X,Step,Sum,A
    	REAL  R,AvrS
	PRINT *, "Dwse to A"
	READ *,A
	call srand(12345)
    	DO I=1,8
	   
	   N    = 10**I		! Number of Experiment
	   Sum  = 0		! Sum of steps

	   DO J=1,N
	      Step = 0		! step counter
	      X    = 0		! current location of the walker
	      
				!-- Do an experiment -----!
	      DO WHILE (ABS(X).LE.A) !
				!
		 R = RAND()	! Generate a random number
				!
		 IF(R<0.5) THEN	!
		    X=X-1	! Left step
		 ELSE		!
		    X=X+1	! Right step
		 END IF		!
				!
		 Step = Step + 1 ! Increment the step
				!
		 IF( ABS(x) .GT. A ) THEN ! Is the walker outside?
		    Sum = Sum + Step ! Sum the steps
		    EXIT	!from the current do while loop
		 END IF		!
				!
	      END DO		!
				!--------------------------!
	      
	   END DO
	      
	   AvrS = REAL(Sum)/N	! Average number of steps
	   PRINT '(I15,1x,F10.6)',N,AvrS ! output N vs Avrs
	      
	END DO

	END

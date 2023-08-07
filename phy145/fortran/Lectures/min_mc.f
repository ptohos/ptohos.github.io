	PROGRAM Minima
!--------------------------------------------------------------
! MC methodos anazitisis elaxistou mias synartisis 
!
! H methodos epanalambanei synexws ton ypologismo tis F(x),
! se tyxaia epilegmena simeia tis aneksartitis metablitis x
! se ena diastima [A,B]. An ektelesoume ti diadikasia arketes
! fores tote the exei entopistei to elaxisto, fmin, sto xmin.
!
! To programma xrisimopoiei tin synartisi F(x) = x^2 - 6x + 5
! poy parousiazei elaxisto gia x = xmin = 3.0 kai fmax = -4.0
!--------------------------------------------------------------
	IMPLICIT NONE
	INTEGER ISEED
	REAL    X, XMIN, FMIN, R, A, B
	INTEGER I, J, N
	REAL    F		! H synartisi mas
	
	ISEED = 123456
	call srand(iseed)       ! Ksekinima akoloythias tyxaiwn arithmwn
	A    = 1.0
	B    = 5.0
	fmin = 9.0E9		! poly megali arxiki timi gia elaxisto
	
 	DO I = 1, 5
	   N = 10**I		    ! arithmos peiramatwn (dokimwn)
	   DO J=1,N		    ! i pragmatiki anazitisi
	      X = A + (B -A)*RAND() ! x omoiomorfa katanemimeno
                		    ! sto diastima [A,B]
	      IF ( F(x) .lt. fmin ) THEN	! Sygkrisi F(x) kai fmin
		 fmin = F(x)
		 xmin = x
	      END IF
	   ENDDO
	   PRINT *,N,xmin,fmin
	ENDDO
 	END

	REAL FUNCTION F(x)
	REAL X
   	F = X**2 - 6*X + 5	! the function F(x)
	RETURN
	END
	

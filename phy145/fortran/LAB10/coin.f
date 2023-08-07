	PROGRAM Head_Tail
!------------------------------------------------------------
! Monte Carlo gia tin proseggisi tis ripsis enos nomismatos
!
! To programma ypologizei tin pithanotita na paroyme tin 
! panw opsi tou nomismatos xrisimopoiontas ti methodo tou 
! Monte Carlo gia diaforetiko plithos ripsewn tou nomismatos 
!------------------------------------------------------------
	IMPLICIT NONE
	INTEGER I, J, N, Head
	INTEGER ISEED
	REAL    P, R

	ISEED = 123456
	call srand(iseed)
	DO I=1, 9

   	  N    = 10**I   ! Plithos peiramatwn
          Head = 0       ! Arxiki timi metriti

   	  DO J=1,N
          R = RAND()
          IF(R .lt. 0.5) Head = Head + 1
   	  END DO   
   	  P = REAL(Head)/N  ! Pithanotita gia heads
          PRINT *,N,Head,P  ! Oso megalei o arithmos
                            ! twn peiramatwn N, i timi
                            ! ayti tha plisiazei stin 
                            ! theoritiki pithanotita 1/2
	END DO
	END

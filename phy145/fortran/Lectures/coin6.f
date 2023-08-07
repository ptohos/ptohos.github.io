      PROGRAM Coin6
!------------------------------------------------------------
! Monte Carlo gia proseggisi tis ripsis toy nomismatos 6 fores
!
! To nomisma rixnetai 6 fores. 
! To programma upologizei tin pithanotita na paroume:
!
!  (a)   akribws 4 fores heads
!  (b)   toulaxiston 4 fores heads 
!
! xrisimopoiei ti Methodo Monte Carlo gia difforetiko plithos
! prospatheiwn. Ta analytika apotelesmata einai:
!
!  (a) 0.234375
!  (b) 0.34375
!
!------------------------------------------------------------
      IMPLICIT NONE
      INTEGER  I,J,K,N
      INTEGER  Head,E4H,AL4H
      REAL     R
      INTEGER  ISEED

      ISEED = 123456
      call srand(iseed)         ! Ksekinima akolouthias tyxaiwn arithmwn
      DO I=1,9
         N    = 10**I           ! Plithos prospatheiwn
         E4H  = 0               ! Akribws 4 Heads
         AL4H = 0               ! Toylaxiston 4 Heads

         DO J=1, N

            Head = 0
            DO K = 1,6
               R = RAND()
               IF(R .GE. 0.5 ) Head  = Head  + 1
            END DO
            IF(Head.EQ.4) E4H  = E4H  + 1
            IF(Head.GE.4) AL4H = AL4H + 1
         END DO
         PRINT *,N,REAL(E4H)/N,REAL(AL4H)/N
      END DO
      END


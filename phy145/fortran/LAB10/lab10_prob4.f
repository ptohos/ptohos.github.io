      PROGRAM ZARI
!------------------------------------------------------------
! Monte Carlo gia proseggisi tis pithanotitas na paroume 
! sugkekrimeno arithmo kata ti ripsi enos zariou: (i.e. 6)
!
! H pithanotita einai 1/6 afou to zari exei 6 noumera kai 
! epomenws i pithanotita na paroume opoiodipote noumero apo 1-6
! einai akrivws idia gia ola ta noumera
!
! Epomenws i theoretiki pithanotita einai 1/6
!
! Gia na lusoume to problima tha metatrepsoume tous tyxaious 
! arithmous kai anti na pernoun times sto diastima [0,1] tha 
! pairnoun akeraies tyxaies times apo 1 ews 6 afou ayta einai
! ta noumera pou mporoume na exoyme
!
! Tha xrisimopoiisoume ti Methodo Monte Carlo gia diafforetiko
! plithos prospatheiwn.
!------------------------------------------------------------
      IMPLICIT NONE
      INTEGER  I, J, N
      INTEGER  ZARIA, NZARIA, NZGOT
      INTEGER  ISEED
      REAL     R

      ISEED  = 123456
      ZARIA  = 6               ! Timi poy theloume
      call srand(iseed)
      DO I = 1, 9
         N    = 10**I          ! Plithos prospatheiwn
         NZARIA = 0            ! Metritis midenizetai gia kathe periptwsi

         DO J=1, N
            R = RAND()
            NZGOT = 1 + INT(6*R) ! Etsi tha paroume tyxaies 
                                 ! akeraies times apo 1 ews 6
            IF(NZGOT .EQ. ZARIA ) NZARIA  = NZARIA  + 1
         END DO
         IF (I.EQ.1) WRITE(6,10)
         WRITE(6,11)N, REAL(NZARIA)/N
      END DO
 10   FORMAT(1x,'Prospatheies',2x,'Pososto epituxias')
 11   FORMAT(2x,I10,7x,F9.7)

      END
      

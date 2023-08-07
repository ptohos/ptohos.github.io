c========================
      program bathologia
c========================
      CHARACTER*15 NAME
      REAL    GRADE
      REAL    AVE
      CHARACTER*6  PASSFAIL
      INTEGER NFAIL
      

      I = 0
 20   I = I + 1
      PRINT *,'Dwste to onoma tou',i,' foititi'
      READ *,NAME
      J = 0
      SUM = 0            ! To SUM gia to meso oro. Gia kathe foititi prepei
                         ! na ginetai 0. Opote mpainei meta to onoma kathe 
                         ! foititi. 
      NFAIL = 0          ! Mathimata poy apetyxe prepei ma midenizontai 
                         ! gia kathe foititi
 21   J = J +1
      PRINT *,'Dwste to bathmo tou',j,' mathimatos'
      READ *,GRADE
      SUM = SUM + GRADE
      IF (GRADE .LT. 5) NFAIL = NFAIL + 1
      IF (J .LT. 5) GOTO 21      ! Ksanagyrname na diavasoume to epomeno bathmo
      AVE = SUM/J                ! To J prepei na einai 5 opote pairnoume 
                                 ! to meso oro
      IF ((NFAIL .GT. 1) .OR. (AVE .LT. 6.0) ) THEN
         PASSFAIL = 'FAILED'
      ELSE
         PASSFAIL = 'PASSED'
      ENDIF
      PRINT *,' O/H Foititis ',name,' eixe meso oro ',ave,' kai ',
     *        PASSFAIL
c
      IF (I .LT. 6) GOTO 20      ! Epomenos foititis
      END 

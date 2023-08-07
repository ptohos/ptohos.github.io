c=============================
      program frequency
c=============================
c O idios kwdikas antistoixei
c kai sto problima 5
c=============================
      INTEGER I, J, NMAX, MYNUMB, NUMB
      INTEGER A(100), IMIN, IMAX
c
c Dinoume arxikes times stous pinakes
c======================================
      NMAX = 100         ! Megethos pinaka
      DO I = 1, NMAX
         A(I)   = 0
      ENDDO
c
      PRINT *,' Poio einai to euros twn timwn pou tha diabastoun?[1-30]'
      READ*, IMIN, IMAX
c
      OPEN(UNIT=30,FILE='inp_integers.dat',STATUS='OLD')
 25   READ(30,*,END=40)MYNUMB
      IF (MYNUMB .GT. IMAX .OR. MYNUMB .LT. IMIN) THEN
         PRINT *, ' O Arithmos',MYNUMB,' out of range'
         PRINT *, ' De tha kataxwrithei'
         GOTO 25
      ENDIF
      NUMB = MYNUMB - (IMIN - 1)
      A(NUMB) = A(NUMB) + 1       ! Afou oi times poy diavazoume briskontai
                                  ! sto diastima tou megethous tou pinaka A
                                  ! kathe thesi sto pinaka mporoume na 
                                  ! fantastoume oti antiproswpeuei ena arithmo.
                                  ! Epomenws mporoume apla na apothikeuoume sti
                                  ! sugkekrimeni thesi mia ayksitiki posotita
                                  ! pou deixnei poses fores ousiastika 
                                  ! xtypisame ti sygkekrimeni thesi tou pinaka
      GOTO 25
c
 40   CLOSE(30)
      OPEN(UNIT=30,FILE='frequency.dat',status='UNKNOWN')
      DO J = 1, (IMAX - IMIN)+1
         I = (IMIN - 1) + J
         PRINT *,'O akeraios',I, ' emfanizetai',A(I),' fores'
         WRITE(30,*) I, A(I)
      ENDDO
      CLOSE(30)
      END 

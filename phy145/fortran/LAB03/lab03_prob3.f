c=====================
      program average
c=====================
      REAL    A, SUM, AVE
      INTEGER I

      I = 0
 20   I = I + 1
      PRINT *, ' Dwse ton',i,' arithmo '
      READ *, A
      PRINT *, ' Edwses ton',i,' arithmo ',A
      sum = sum + A              ! Afou theloume to meso oro xreiazomaste to 
                                 ! athroisma tous kai meta prepei na 
                                 ! diairesoume me to plithos tous.
      IF (I.LT.10) GOTO 20       ! An exoume ligoterous apo 10 diavasoume to 
                                 ! epomeno ayksanontas to plithos tous kata 1
      AVE = SUM/I
      PRINT *,' O mesos oros twn ',I,' arithmwn einai:',ave
      END

c=====================
      program maxima
c=====================
      REAL    A, B, C
      REAL    maximum1, maximu2, maximu3
      REAL    GAS_USED

      PRINT *, ' Dwse toys arithmous A,B kai C'
      READ *, A, B, C

      MAXIMUM1 = A      ! Arxika upothetw oti oloi oi arithmoi einai 
      MAXIMUM2 = A      ! taksinomimenoi me to A
      MAXIMUM3 = A
c An to B einai megalutero apo to megisto tote ton bazw sti megisti thesi
      IF (B .GT. MAXIMUM1) THEN 
         MAXIMUM1 = B 
      ELSE
c Diaforetika oi 2 mikroteroi arithmoi tha nai o B 
         MAXIMUM2 = B
         MAXIMUM3 = B
      ENDIF
c
c An o C einai megaluteros apo to megalutero twn A,B tote mpainei sti 
c megisti thesi kai metatopizw ta alla 2 kata mia thesi pros ta katw
c 
      IF (C .GT. MAXIMUM1) THEN
         STORE    = MAXIMUM1
         MAXIMUM1 = C
         MAXIMUM3 = MAXIMUM2
         MAXIMUM2 = STORE
      ELSE IF (C.GT. MAXIMUM2) THEN
c Diaforetika eksetazw me to deutero megisto kai metatopisw ta 2 teleutaia 
c kata mia thesi
         STORE = MAXIMUM2 
         MAXIMUM2 = C
         MAXIMUM3 = STORE
      ELSE
c Diaforetika einai o mikroteros
         MAXIMUM3 = C
      ENDIF
      PRINT *,' H taksinomisi twn 3 arithmwn einai '
      PRINT *, MAXIMUM1, MAXIMUM2, MAXIMUM3
      END
      

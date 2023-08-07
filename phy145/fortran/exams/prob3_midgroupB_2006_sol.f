c==========================
      Program fibonnacci
c==========================
      INTEGER I, J, K, KMAX
      INTEGER NTERMS, FIBMAX, FIBF
      INTEGER FIB(30)

      WRITE(6,10)
 10   FORMAT(1x,'Dwste to prwto oro tis seiras')
      READ(5,*)I
      WRITE(6,20)
 20   FORMAT(1x,'Dvste to deytero oro tis seiras')
      READ(5,*)J
      WRITE(6,30)
 30   FORMAT(1x,'Dwste to plithos twn orwn gia ektypwsi [N <= 30]')
      READ(5,*)NTERMS
      WRITE(6,40)
 40   FORMAT(1x,'Dwste to megisto oro gia upologismo [FIBMAX <= 10000]')
      READ(5,*)FIBMAX

      DO K = 1, NTERMS
         FIB(K) = 0
      ENDDO

      FIB(1) = I
      FIB(2) = J
      K = 3
 50   L = I + J
      IF (K.LE.NTERMS) FIB(K) = L     ! Check an ftasasme sto max oro
      IF ((L+J).GT.FIBMAX) THEN       ! Check an o epomenos oros kseperna
         KMAX = K                     ! ti megisti timi. To L tha ginei o K-1
                                      ! kai o J o K-2 oros 
         FIBF = L                     ! teliki timi < FIBMAX
         GOTO 80
      ENDIF
      K = K + 1
      I = J
      J = L
      GOTO 50
c
 80   CONTINUE
      WRITE(6,100)
 100  FORMAT(1x,'Apotelesmata seiras Fibonnacci')
      WRITE(6,110)(FIB(K),k=1,MIN(KMAX,NTERMS))
 110  FORMAT(3(3x,I7))
      WRITE(6,120)KMAX,FIBF
 120  FORMAT(1x,'O oros',I3,1x,'exei timi',1x,I7)

      END

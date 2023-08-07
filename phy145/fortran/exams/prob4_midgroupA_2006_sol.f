c========================
      program bessel
c========================
      DOUBLE PRECISION X
      INTEGER M, N, J, K
      DOUBLE PRECISION BSL
      DOUBLE PRECISION PRECISION
      DOUBLE PRECISION RESULT
c
      WRITE(6,10)
      READ(5,*)M
      WRITE(6,30)
      READ(5,*)PRECISION
c
 10   FORMAT(1x,' Eisagete tin taksi tis synartisis [m]')
 20   FORMAT(1x,' Dwste to x gia upologismo tis synartisis')
 30   FORMAT(1x,' Ti akriveia ypologismou thelete')

      X = 0.0D0
 2    RESULT = BSL(M,X,PRECISION)
      IF (X.LE.10.0D0) THEN 
         WRITE(6,40) M,X,RESULT,PRECISION
         X = X + 0.5
         GOTO 2
      ENDIF
 40   FORMAT(1x,'H timi tis',1x,I2,'th taksis Bessel synartisis gia x=',
     &       1x,f4.1,1x,'einai J=',1x,F14.12,1x,' gia akriveia ',E13.8)
      END

c==============================================
      DOUBLE PRECISION FUNCTION BSL(M,X,TOL)
c==============================================
      INTEGER M, I, J
      DOUBLE PRECISION X, TOL, SUM, R, HALFX
c
      DOUBLE PRECISION TERMADD, FACT1, FACT2
      DOUBLE PRECISION FACTORIAL

c
      SUM = 0.0D0
      HALFX = X/2.
      J = 0
 2    FACT1 = FACTORIAL(J)
      FACT2 = FACTORIAL(J+M)
      TERMADD = ((-1.0)**J/(FACT1*FACT2))*HALFX**(2*J+M)
      IF (ABS(TERMADD) .LT. TOL) GOTO 10
      SUM = SUM + TERMADD
      J = J + 1
      GOTO 2
 10   BSL = SUM
      RETURN
      END

c==============================================
      DOUBLE PRECISION FUNCTION FACTORIAL(N)
c=============================================
      INTEGER N
      DOUBLE PRECISION R
      DOUBLE PRECISION PROD
c
      IF (N.LT.0) THEN
         PRINT *, ' Arnitikos arithmos sti synartisi paragontikou'
         PRINT *, ' Diakopi upologismwn'
         STOP
      ENDIF

      IF (N.GT.170) THEN
         PRINT *, ' Paragontiko toy',N,' de mporei na upologisthei'
         PRINT *, ' Diakopi upologismwn'
         STOP
      ENDIF

      PROD = 1.0D0
      DO J = 1, N
         PROD = PROD*J
      ENDDO
      FACTORIAL = PROD
      RETURN
      END

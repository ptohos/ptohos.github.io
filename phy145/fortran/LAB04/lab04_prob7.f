c======================
      program func
c======================
      REAL    X, XMIN, XMAX, DX
c
      OPEN(UNIT=40,file='function.dat',status='unknown')
      XMIN = -20.
      XMAX =  20.
      X    = XMIN
      DX   = 1.
      DO WHILE(X.LE.XMAX)
         Y = x**2 + 2*x + 1 
         WRITE(40,50)X,Y
         X = X + DX
      ENDDO
 50   FORMAT(1x,F5.1,2x,F5.1)
      CLOSE(40)
      END

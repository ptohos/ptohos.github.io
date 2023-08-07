c========================= 
     program products
c=========================
      INTEGER  J, N, NMAX
      REAL     X(100), Y(100)            ! Arxika orizoume to megethos twn X,Y
      REAL     SUM1, SUM2, SUM3, RATIO
      REAL     INNPRO
c
c     
      NMAX = 100
      DO J = 1, NMAX
         X(J) = J+2             ! Gemizw toys pinakes me tyxaia stoixeia
         Y(J) = J+1
      ENDDO
c
      SUM1 = INNPRO(X,X,NMAX)   ! Ypologizetai to x1*x1 + x2*x2 +...
      SUM2 = INNPRO(Y,Y,NMAX)   ! Ypologizetai to y1*y1 + y2*y2 +...
      SUM3 = INNPRO(X,Y,NMAX)   ! Ypologizetai to x1*y1 + x2*y2 +...
c
      SUM1 = SQRT(SUM1)
      SUM2 = SQRT(SUM2)
      SUM3 = SQRT(SUM3)
      RATIO = SUM1*SUM2/SUM3
      WRITE(6,10)RATIO
 10   FORMAT(1x,' To apotelesma tou ypologismoi einai:',1x,F10.5)
      END
c
c====================================
      REAL FUNCTION INNPRO(A,B,N)
c====================================
      INTEGER J, N
      REAL A(N), B(N), SUM
c
      SUM = 0
      DO J = 1, N
         SUM = SUM + A(J)*B(J)
      ENDDO
      INNPRO = SUM
      RETURN
      END

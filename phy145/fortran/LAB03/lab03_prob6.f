c========================
      program factorial
c========================
      INTEGER          N
      INTEGER          NFACT
      REAL             RFACT
      DOUBLE PRECISION DFACT
      INTEGER          J

c     
      PRINT *, ' Ypologismos paragontikou akeraiou'
 10   PRINT *, ' Dwse ena akeraio arithmo '
      READ *, N
      IF (N.LT.0) THEN
         PRINT *,' Den orizetai paragontikou arnitikou! Try again'
         GOTO 10
      ENDIF

c To paragontiko tou midenos einai 1 
      NFACT = 1
      RFACT = 1.
      DFACT = 1.
c To paragontiko enos arithmou einai N! = 1*2*3*4...*N
      DO J = 1, N
c Edw upologizw oles tis periptwseis apeikonisis: INTEGER,REAL, DOUBLE  
         NFACT = NFACT * J   ! Pol/smos INTEGER*INTEGER --> INTEGER
         RFACT = RFACT * J   ! Pol/smos REAL*INTEGER    --> REAL 
         DFACT = DFACT * J   ! Pol/mos  DOUBLE PRECISION*INTEGER --> DOUBLE
      ENDDO
      PRINT *,' Se INTEGER apeikoniki to paragontiko tou',N,' einai',
     &          NFACT 
      PRINT *,' Se REAL apeikoniki to paragontiko tou',N,' einai',
     &          RFACT
      PRINT *,' Se DOUBLE PRECISION apeikoniki to paragontiko tou',N,
     &         ' einai',DFACT 
      END

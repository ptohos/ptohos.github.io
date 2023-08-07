c========================
      program sorting
c========================
      IMPLICIT NONE
      INTEGER I, J, K, N
      INTEGER NMAX, NREAD
      INTEGER IMAX, AMAX
      INTEGER A(20)

      NMAX = 20
      DO I = 1, NMAX
         A(I) = 0
      ENDDO

      open(unit=99,file='lab04_prob1.dat',status='old',err=20)
      K = 0
      I = 1

 5    K = K + 1
      read(99,*,end=10,err=15) A(I)
      NRead = I

      I = I + 1
      if (I.LE.NMAX) then
         goto 5
      else
         write(6,3) NRead
         write(6,4)
 4       format(1x,'Afinoume ta ypoloipa stoixeia')
         goto 25
      endif
c=========================
 20   Print *,' To file lab04_prob1.dat den mporei na anoixthei'
      Print *,' check the file name - Stopping execution'
      Stop
c=========================
 15   write(6,2)K
 2    format(1x,'Lathos format record',1x,I3,1x,'tou file',/,
     &       1x,'parablepoume to record auto')
      goto 5
c=========================
 10   write(6,3) NREAD
 3    format(1x,'Diavasame',1x,I3,1x,'stoixeia apo to file')

 25   CLOSE(69)
c=========================
c
c Taksinomisi tou pinaka
c=========================
      N    = NRead
 21   AMAX = A(1)
      IMAX = 1
      DO I = 2, N
         IF (AMAX .LT. A(I)) THEN
            IMAX = I
            AMAX = A(I)
         ENDIF
      ENDDO
      A(IMAX) = A(N)
      A(N) = AMAX
      N = N - 1
      IF (N .GT. 1) GOTO 21
c 
c 1os tropos
c============
      DO I = 1, NRead, 5
         WRITE(6,50)(A(J), J=I, I+4)
      ENDDO
      Write(6,51)
 50   FORMAT(5(1x,I3))
 51   Format(1x,20('*'))

c
c 2os tropos
c=============
      WRITE(6,60)A       ! Olokliros o pinakas
 60   FORMAT(5(1x,I3))
      END

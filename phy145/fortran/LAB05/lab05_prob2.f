c=========================
      program pinakas
c=========================
c xrisi function
c=========================
      integer J, NMAX, NFILL
      real    A(100), minimo
      real    find_min

      NMAX = 100
      DO J = 1, NMAX
         A(J) = 0.0   ! Midenismos tou pinaka
      ENDDO
      
      PRINT *,'***************************'
      PRINT *,'Praktiki me xrisi functions'
      PRINT *,'***************************'

      open(unit=20,file='lab05_prob2.dat',status='old',err=80)
      goto 30

 80   print *,' Cannot open file '
      print *,' Stop program'
      stop

 30   continue
      DO J=1, NMAX
         READ(20,*,end=40)A(J)
      ENDDO

 40   NFILL = J - 1     ! Arithmos records poy diavastikan apo to file
      WRITE(6,45)NFILL
 45   FORMAT(1X,'Diavastikan',1x,I3,1x,'records apo to file')

c======
c Klisi tis synartisis 
c======
      MINIMO = FIND_MIN(A,NFILL)

      write(6,10)minimo
 10   FORMAT(1x,'To elaxisto stoixeio tou pinaka einai iso:',1x,F10.4)
      END

c===================================
      REAL FUNCTION FIND_MIN(A,NDim)
c===================================
      Implicit none
      INTEGER IMin, NDim
      INTEGER J, NP
      REAL A(NDim), Amin

      NP = NDim
      AMin = A(1)
      IMin = 1
      DO J = 2, NP
         IF (AMin.GT.A(J)) THEN
            AMin = A(J)
         ENDIF
      ENDDO
      FIND_Min = AMin

      RETURN
      END

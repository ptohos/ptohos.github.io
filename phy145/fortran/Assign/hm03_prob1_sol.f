c========================= 
      program median
c=========================
      INTEGER  J, N, NMAX, NREAD
      REAL     X(100), VALUE       !<< Arxika o pinakas orizetai me megethos 100
 
      REAL     MDIAN               !<< Synartisi MDIAN
c     
      NMAX = 100
      DO J = 1, NMAX
         X(J) = 0.0
      ENDDO
c
 2    PRINT *, 'Posa stoixeia exei o pinakas ?'
      READ *,NREAD
      IF (NREAD.GT.NMAX) THEN
         PRINT *,' Perissotera stoixeia apo to megethos tou pinaka'
         PRINT *,' Dwste mikrotero arithmo stoixeiwn'
         GOTO 2
      ENDIF
      DO J = 1, NREAD
         PRINT *,'Dwse to ',J,' stoixeio tou pinaka'
         READ *, X(J)
      ENDDO
c=========================================================
c Taksinomoyme to pinaka X kata ayksousa seira
c Ayto to kanoume me tin klisi mias subroutine SORT
c=========================================================
      CALL SORT(X,NREAD)
c========================================================
c Afou o pinakas mas einai taksinomimenos mporoume
c na broume ti mesaia timi or median value
c Tha to kanoume me klisi mias function median
c=========================================================
      VALUE = MDIAN(X,NREAD)
c=========================================================
      PRINT *,X
      WRITE(6,10)VALUE
 10   FORMAT(1x,'H mesaia timi toy pinaka einai:',F10.5)
      END

c=====================================
      SUBROUTINE SORT(A,N)
c=====================================
c Sas dinw ena diaforetiko algorithmo 
c taksinomisis se sxesi me ayto pou 
c exoume dei mexri twra
c======================================
      INTEGER N, J, I
      REAL A(N), AMAX

      DO 10 J = 2, N
         AMAX = A(J)
         DO 20 I = J-1, 1, -1
            IF (A(I).LE.AMAX) GOTO 30
            A(I+1) = A(I)
 20      CONTINUE
         I = 0
 30      A(I+1) = AMAX
 10   CONTINUE
      RETURN
      END

c=========================================
      REAL FUNCTION MDIAN(A,N)
c=========================================
C Dinetai enas pinakas A(N) taksinomimenos
c kai epistrefei ti median timi 
c==========================================
c Kapoios tha mporouse na kalesei ti
c subroutine sort sto meros ayto tou 
c programmatos.
c==========================================
      INTEGER N, NHALF
      REAL A(N), VALUE

c==============================================
c Edw kapoios tha mporouse na kalesei ti sort
c     call sort(X,N)
c==============================================
      NHALF = N/2
      IF ((NHALF * 2) .EQ. N) THEN     ! Exoume artio arithmo stoixeiwn
         VALUE = 0.5*(A(NHALF) + A(NHALF+1))  ! Mesos oros twn 2 mesaiwn
                                              ! stoixeiwn toy pinaka
      ELSE                             ! Perittos arithmos stoixeiwn
         VALUE = A(NHALF+1)
      ENDIF
      MDIAN = VALUE
      RETURN
      END

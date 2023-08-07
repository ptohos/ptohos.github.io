c=========================== 
      program matrixmanipul
c===========================
      INTEGER  J, K, L
      INTEGER  NREAD, NMAX
      INTEGER  ISSYM, SPACES
      REAL     X(100,100)
      REAL     Y(100,100)
      CHARACTER*40 form
      CHARACTER*1  frm
      character*2  spc
c
c     
      NMAX = 100
      DO J = 1, NMAX
         DO K = 1, NMAX
            X(J,K) = 0.
         ENDDO
      ENDDO
      PRINT *, ' Posa stoixeia tou pinaka the xrisimipoiisete?'
      READ*, NREAD
c
      DO J =1, NREAD
         DO K = 1, NREAD
            X(J,K) = J*K       ! Tyxaia stoixeia tou pinaka
         ENDDO
      ENDDO
c
      CALL SYM(X,NMAX,NREAD,ISSYM)
      IF (ISSYM.EQ.1) THEN 
         PRINT *,' O Pinakas EINAI symmetrikos'
      ELSE
         PRINT *,' O Pinakas DEN einai symmetrikos'
      ENDIF

      CALL TRANS(X,NMAX,NREAD,Y)
      WRITE(6,5) 
 5    FORMAT(11x,'O pinakas X',21x,'Kai o anastrofos tou')

c
c Xrisi metavlitou Format build on the fly
c==========================================
      write(frm,20)NREAD
 20   FORMAT(I1)
 21   FORMAT(I2)
      spaces = 42-nread*6       ! Format pinaka 2x,f4.0 synolika 6 theseis
      if (nread.gt.7) then 
         print *,'Cannot use right format'
         stop
      endif
      if (spaces.lt.10) then
         write(spc,20)spaces
      else if (spaces.lt.100) then
         write(spc,21)spaces
      endif
      form = '('//frm//'(2x,f4.0),'//spc//'x,'//frm//'(2x,f4.0))'

      DO J = 1, NREAD
         WRITE(6,form) (X(J,K),K=1,NREAD), (Y(J,K),K=1,NREAD)
      ENDDO

      END
c
c====================================
      SUBROUTINE SYM(A,N,L,IFLAG)
c====================================
      INTEGER J, K, N, L, IFLAG
      REAL A(N,N), SUM      ! PROSOXI: Gia dusdiastatoys pinakes den mporoume 
                            !          na exoume metavliti diastasi. Prepei na
                            !          toys orisoume akrivws opws kai sto main
                            !          programma. Ayto giati oi pinakes sti 
                            !          fortran kratountai se stiles. Epomenws
                            !          gia ena pinaka orismeno san A(10,10)
                            !          to stoixeio A(1,2) brisketai stin 11 
                            !          thesi. Dinontas metabliti diastasi
                            !          p.x. A(2,2) simenei oti tha exoume 
                            !          4 stoixeia apo ton arxiko pinaka. Etsi
                            !          stin uporoutina to A(1,2) tha einai to
                            !          3o stoixeio tou pinaka pou profanws den 
                            !          einai to 11o toy arxikou pinaka A
c
      IFLAG = 0             ! Arxiki timi ypothetoume oti den eini symmetrikos
      SUM = 0.
      DO 40 J = 1, L-1      ! Xreiazetai na koitaksoume mono ta stoixeia panw
        DO 30 K = J+1, L    ! apo ti diagvnio kai na ta sygkrinoume me ayta 
                            ! katw apo ti diagvnio
           SUM = SUM + ABS(A(J,K) - A(K,J)) ! Athroisma diaforvn tvn stoixeiwn
                            ! An to athroisma einai miden o pinakas einai 
                            ! symmetrikos 
 30     CONTINUE
 40   CONTINUE
      IF (SUM.EQ.0.) IFLAG = 1 
      RETURN
      END

c===================================
      SUBROUTINE TRANS(A,N,L,B)
c===================================
      REAL A(N,N), B(N,N)
      INTEGER J,K,N,L

      DO J = 1, L              ! Stoixeia tou pinaka panw apo ti diagwnio
         DO K = J+1, L
            B(J,K) = A(K,J)
            B(K,J) = A(J,K)
         ENDDO
         B(J,J) = A(J,J)
      ENDDO
      RETURN
      END

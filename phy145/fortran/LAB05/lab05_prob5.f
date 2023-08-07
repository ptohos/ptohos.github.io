c======================================================================
         program matrixpower
c======================================================================
c To programma upologizei to pinaka pou prokuptei an pollaplasiasoume 
c kapoio pinaka (N,N) me ton eauto tou K fores. Diladi an o pinakas 
c einai A(N,N) upologizoume to A^K
c=======================================================================
c O pollaplasiasmos 2 pinakwn A KxL kai B LxN einai enas pinakas C KxN
c      A[K,L]*B[L,N] = C[K,N]
c Ta stoixeia tou C dinontai apo Cij = SUM(A_ip * B_pj)  opou to 
c athroisma einai ws pros p=1,L
c=======================================================================
c Apo ti parapanw sxesi kai apo to gegonos oti o pinakas B=A gia to 
c problima mas xreiazomaste 2 epipleon pinakes gia ton upologismo. 
c Ena pinaka B o opoios arxika einai o monadiaios kai katopin ginetai
c isos me to ginomeno tou B*A. Xreiazomaste ena pinaka C pou einai to
c apotelesma kathe pol/smou. O Pinakas aytos tha antigrafetai sto 
c B opote sto epomeno vima tha exoume B*A = (A*A)*A   opou B=A*A
c=======================================================================
        INTEGER A(100,100), B(100,100), C(100,100)
        INTEGER I, J, K, M, N
        INTEGER NROW, NCOL, INDEX
        
        NROW   =  2
        NCOL   =  2
        INDEX  =  2
c
        A(1,1) =  1
        A(1,2) =  3
        A(2,1) = -1
        A(2,2) = -2

        DO I = 1, NROW                  ! Gia tin periptwsi pou oi pinakes
           DO J = 1, NCOL               ! den einai tetragwnikoi
              IF (I.EQ.J) THEN          ! Monadiaios 
                 B(I,J) = 1             !   1   0
              ELSE                      !   0   1
                 B(I,J) = 0  
              ENDIF
           ENDDO
        ENDDO
c               
        PRINT *,' Dwste ton ektheti tis dynamis'
        READ(5,10) N
 10     FORMAT(I5)

        DO K = 1, N                       ! Kanoume N pol/smous           
           call calc(A,B,NROW,INDEX,NCOL) ! o A paramenei idios pantote
        enddo                             ! enw o B periexei to apotelesma tou
                                          ! pol/smou
        DO I = 1, 2
           WRITE(6,20)(B(I,J),J=1, 2)
        ENDDO
 20     FORMAT(2(3x,I2))
        end

        subroutine calc(A,B,NROW,INDEX,NCOL)
        integer NROW, NCOL, INDEX
        integer I, J, M
        integer A(100,100), B(100,100), C(100,100)

        DO I = 1, NROW           ! C[Nrow,Ncol]= A[NRow,Index]*B[Index,Ncol]
           DO J = 1, NCOL           
              C(I,J) = 0
              DO M = 1, INDEX
                 C(I,J) = C(I,J) + B(I,M)*A(M,J)
              END DO
           ENDDO
        ENDDO
        DO I = 1, NROW         ! Brikame to ginomeno antikatastoume sto B 
           DO J = 1, NCOL
              B(I,J) = C(I,J)
           ENDDO
        ENDDO
        return
        END


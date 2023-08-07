c=======================================
      program triangle
c=======================================
      INTEGER J
      REAL VECA(3), VECB(3), VECC(3)
      REAL VEC_CM(3), VEC_CM_TIME(3)
      REAL TIME, DT
      REAL NORMA, RMAGN, RMAGMAX
      CHARACTER*1 XYZ(3),A
c
      xyz(1) = 'x'
      xyz(2) = 'y'
      xyz(3) = 'z'
      PRINT *, 'Poses diastaseis sto problima ? [max=3]'
      READ*, N
c
      DO J = 1, N
         a = xyz(j)
         PRINT*,'Poios o rytmos metabolis tis ',a,'-synistwsas toy A'
         READ *, VECA(J)
         PRINT*,'Poios o rytmos metabolis tis ',a,'-synistwsas toy B'
         READ *, VECB(J)
         PRINT*,'Poios o rytmos metabolis tis ',a,'-synistwsas toy C'
         READ *, VECC(J)
      ENDDO
      PRINT *,' Poio to megisto metro tou dianusmatos R_CM '
      READ *, RMAGMAX

      DT   = 1.0
      TIME = 0.
      CALL FINDCM(VECA,VECB,VECC,N,VEC_CM) ! Ayti i routina mas dinei tis 
                                           ! syntetagmenes toy CM anejartita
                                           ! tou xronou. Koinws mporei na 
                                           ! theorisoume oti mas dinei tin 
                                           ! synistwses tis taxutitas tou CM
 30   CONTINUE
      DO J =1, 3
         VEC_CM_TIME(J) = VEC_CM(J)*TIME   ! Metrepoume ti taxutita se apostasi
      ENDDO
      RMAGN = NORMA(VEC_CM_TIME,N)         ! Ypologismos tou metrou
      IF (RMAGN .LE. RMAGMAX) THEN
         WRITE(6,20)TIME, VEC_CM_TIME, RMAGN
         TIME = TIME + DT
         GOTO 30
      ENDIF
 20   FORMAT(1x,F4.0,2x,'(',3(F5.1,','),')',3x,F5.1)
      END

c========================================
      SUBROUTINE FINDCM(V1,V2,V3,N,VTOT)
c========================================
      REAL V1(N),V2(N),V3(N)
      REAL VTOT(N)

      DO J = 1, N
         VTOT(J) = V1(J) + V2(J) + V3(J)
         VTOT(J) = VTOT(J)/3.
      ENDDO
      RETURN
      END

c==========================================
      REAL FUNCTION NORMA(V,N)
c==========================================
c Ypologismos tou metrou tou dianysmatos V
c==========================================
      INTEGER J, N
      REAL V(N), NORM

      NORM = 0.
      DO J = 1, 3
         NORM = NORM + V(J)*V(J)         ! Athroisma tetragvnnv 
      ENDDO
      NORMA = SQRT(NORM)
      RETURN
      END
      

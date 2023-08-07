C================================
      PROGRAM PLANET
C================================
      IMPLICIT NONE
      INTEGER J, K
      INTEGER NSTEP, ALGORITHM
      INTEGER NMAX
      PARAMETER(NMAX=1000)
      REAL    RPLOT(NMAX), THPLOT(NMAX)
      REAL    KINETIC_ENERGY(NMAX)
      REAL    POTENTIAL_ENERGY(NMAX)
      REAL    TOT_ENERGY(NMAX)
      REAL    TIMEPLOT(NMAX)
c
      DOUBLE PRECISION    NORM    ! FUNCTION
      CHARACTER*6 FILETYP
c
      DOUBLE PRECISION ACCEL(2), ACCEL0(2), NORMA
      DOUBLE PRECISION GM, PLANET_MASS
      DOUBLE PRECISION R(2), V(2)
      DOUBLE PRECISION TIME, TIME_STEP
      DOUBLE PRECISION PI
      COMMON/PLANETCONSTS/PI,GM,PLANET_MASS
      COMMON/PLANETCOMMON/NSTEP, ALGORITHM, R, V, TIME, TIME_STEP

c
      CALL SETUP_SYSTEM
      IF (ALGORITHM.EQ.1) FILETYP ='eulers'
      IF (ALGORITHM.EQ.2) FILETYP ='cromer'
      IF (ALGORITHM.EQ.3) FILETYP ='verlet'
      OPEN(UNIT=10,FILE='theta_vs_pos_'//FILETYP//'.dat',
     >     status='unknown')
      OPEN(UNIT=11,FILE='energy_vs_time_'//FILETYP//'.dat',
     >     status='unknown')
c
      DO K = 1, NSTEP
         RPLOT(K)  = NORM(R)           ! Metro toy dianusmatos thesis
         THPLOT(K) = ATAN2(R(2),R(1))  ! Gwnia metaksy [-pi/2,pi/2]
         POTENTIAL_ENERGY(K) = -GM*PLANET_MASS/NORM(R)
         KINETIC_ENERGY(K)   = 0.5*PLANET_MASS*NORM(V)**2
         TOT_ENERGY(K)       = KINETIC_ENERGY(K)+POTENTIAL_ENERGY(K)
         TIMEPLOT(K)         = TIME
         if (k.eq.1) then
            print *, pi,planet_mass,gm,r(1),r(2),v(1),v(2)
            print *,kinetic_energy(K),potential_energy(k)
         endif
c
c Ypologismos tis neas thesis sumfwna me ton epilegmeno algorithmo
c==================================================================
         IF (ALGORITHM .EQ. 1) THEN
            NORMA = NORM(R)
            DO J = 1, 2
               ACCEL(J) = -GM*R(J)/NORMA**3
               R(J)     = R(J) + TIME_STEP*V(J)          ! Euler step
               V(J)     = V(J) + TIME_STEP*ACCEL(J)
            ENDDO
         ENDIF
c
         IF (ALGORITHM .EQ. 2) THEN    ! Euler-Cromer
            NORMA = NORM(R)
            DO J = 1, 2
               ACCEL(J) = -GM*R(J)/NORMA**3  ! dv/dt
               V(J)     = V(J) + TIME_STEP*ACCEL(J)
               R(J)     = R(J) + TIME_STEP*V(J)       ! Euler-Cromer step
            ENDDO
         ENDIF
c
         IF (ALGORITHM .EQ. 3) THEN    ! Verlet
            NORMA = NORM(R)
            DO J = 1, 2
               ACCEL0(J) = -GM*R(J)/NORMA**3  ! dv/dt
               R(J) = R(J) + TIME_STEP*V(J) + TIME_STEP**2*ACCEL0(J)/2.0
            ENDDO
            DO J = 1, 2
               ACCEL(J) = -GM*R(J)/NORM(R)**3
               V(J)     = V(J) + TIME_STEP*(ACCEL(J)+ACCEL0(J))/2.
            ENDDO
         ENDIF
c
         TIME = TIME + TIME_STEP     ! Ayksisi tou xronou
         
      ENDDO                          ! End of JSTEP loop 
      DO J =1, NSTEP
         WRITE(10,*)THPLOT(J),RPLOT(J)
         WRITE(11,*)TIMEPLOT(J), KINETIC_ENERGY(J)
      ENDDO
      DO J =1, NSTEP
         WRITE(11,*)TIMEPLOT(J),POTENTIAL_ENERGY(J)
      ENDDO
      DO J =1, NSTEP
         WRITE(11,*)TIMEPLOT(J),TOT_ENERGY(J)
      ENDDO
      close(10)
      close(11)
c=======
c DONE
c=======
      END

c================================
      SUBROUTINE SETUP_SYSTEM
c================================
      IMPLICIT NONE
      INTEGER NSTEP, ALGORITHM
      DOUBLE PRECISION TIME, TIME_STEP
      DOUBLE PRECISION R0, V0
      DOUBLE PRECISION R(2), V(2)
      DOUBLE PRECISION PI, GM, PLANET_MASS
      COMMON/PLANETCONSTS/PI,GM,PLANET_MASS
      COMMON/PLANETCOMMON/NSTEP, ALGORITHM, R, V, TIME, TIME_STEP

      
      PRINT *,'============================================'
      PRINT *,'     Arxikes synthikes toy problimatos      '
      PRINT *
      PRINT *,' Dwste tin arxiki aktiniki apostasi se A.U.'
      READ(5,*) R0
      PRINT *,' Dwste tin arxiki efaptomeniki taxytita AU/y'
      READ(5,*) V0
      PRINT *,' Dwste ti maza tou planiti ws pros ti maza tis gis'
      READ(5,*) PLANET_MASS
      PRINT *,' Dwste ton aritho tvn xronikvn vimatvn'
      READ(5,*) NSTEP
      PRINT *,' Dwste ton xroniko vima Dt (year)'
      READ(5,*) TIME_STEP
 10   PRINT *,' Epilekste ton algorithmo gia ton ypologismo'
      PRINT *,' Dektes epiloges einai:'
      PRINT *,' Aplos Euler  [1]'
      PRINT *,' Euler-Cromer [2]'
      PRINT *,' Verlet       [3]'
      READ(5,*) Algorithm
      IF (Algorithm .lt. 1 .or. Algorithm .gt. 3) THEN
         PRINT *,' Epilekte kapoio diathesimo algorithmo'
         PRINT *,' H epilogi ',Algorithm,' den isxuei'
         goto 10
      ENDIF
      PRINT *,'============================================'
      R(1) = R0
      R(2) = 0.
      V(1) = 0.
      V(2) = V0
c===========================
c Statheres tou provlimatos
c===========================
      PI = ACOS(-1.)


      GM = 4.*pi**2    ! Stathera tis barititas G x M (maza iliou)
                       ! Oi monades einai se AU^3/yr^2. Ayto giati 
                       ! G=6.67x10^(-11) m^3/(kg x sec^2). 
                       ! 1m = 6.6684x10^-12 AU (apostasi gis-iliou)
                       ! 1AU etos einai i periodos mia kuklikis troxias r=1AU
                       ! Maza iliou 1.99x10^30 kg

      TIME = 0.        ! Arxikos xronos
c

      RETURN
      END


c==============================================
      DOUBLE PRECISION FUNCTION NORM(VECTOR)
c==============================================
c Ayti i sunartisi epistrefei to metro 
c enos dianusmatos
c========================================
      IMPLICIT NONE
      INTEGER J
      DOUBLE PRECISION VECTOR(2)
c
      NORM = 0.
      DO J = 1, 2
         NORM = NORM + VECTOR(J)*VECTOR(J)
      ENDDO
      NORM = SQRT(NORM)
      RETURN
      END


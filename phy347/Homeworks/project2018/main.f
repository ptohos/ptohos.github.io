      program main
      implicit double precision(A-H,O-Z)
      implicit integer(I-N)
      lOGICAL  pass
      INTEGER  PIDSEL, NPASS, Event_Count
      INTEGER  MAX_NEV, GOOD_NEV
      INTEGER  DECAY_LIST, LIST_TYPE
      INTEGER  PYK, PYCHGE, PYCOMP
      DOUBLE PRECISION PTCut, PTPart
      COMMON/PYPARS/MSTP(200),PARP(200),MSTI(200),PARI(200) 
      COMMON/PYSUBS/MSEL,MSELPD,MSUB(500),KFIN(2,-40:40),CKIN(200)
      COMMON/PYJETS/N, NPAD, K(4000,5), P(4000,5), V(4000,5)
      COMMON/PYDAT2/KCHG(500,4),PMAS(500,4), PARF(2000), VCKM(4,4)
c
      CHARACTER FRAME*12, BEAM*12, TARGET*12, PARAM*100
      CHARACTER*50 OUTFILE
c
c...Read parameter of PYINIT call
      DECAY_LIST = 1
      LIST_TYPE  = 1
      READ(*,*)FRAME,BEAM,TARGET,ENERGY
c
c...Read number of events to generate and print
      READ(*,*)MAX_NEV, NPRT
      READ(*,*)OUTFILE
      READ(*,*)PIDSEL, PTCut, NMIN
      
      OPEN(UNIT=89,File=OUTFILE)
c
c...Read of settings and parameters
 100  READ(*,'(A)',END=200)PARAM
      CALL PYGIVE(PARAM)
      GOTO 100

 200  IF (DECAY_LIST.EQ.1) CALL PYLIST(12)
c
c..Initialize PYTHIA
      CALL PYINIT(FRAME,BEAM,TARGET,ENERGY)
      Event_Count = 0
      GOOD_NEV = 0
c     
c..Loop over the events to generate
      DO WHILE (GOOD_NEV .LT. MAX_NEV)
c
c..The event generation here
         CALL PYEVNT
c
c..Printout the status of the events 
         if (mod(Event_Count,1000).eq.0)
     &        print *,'Events/Good_Events=',EVENT_COUNT,GOOD_NEV
c
c..Check to see if the event pass the selection criteria
         PASS = .false.
         NPASS = 0              ! Events with photons above a cut
         DO I=1, N                      ! N generated particles on the event

c
c..   Select events that contain particles with Id=PIDSEL and
c..   they are stable KS=K(I,1)=1. 
c..   Request the selected particle to have pt>ptcut
            IF (ABS(K(I,2)).eq.PIDSEL .and. K(I,1).eq.1) THEN
              PTPart = dsqrt(P(I,1)**2+P(I,2)**2)
              if (PTPart .ge. PTCUT) THEN
                 NPASS = NPASS + 1
                 IF (NPASS.GE. NMIN) GOTO 400
              ENDIF
           ENDIF
        ENDDO
 400    CONTINUE

        EVENT_COUNT = EVENT_COUNT + 1
        IF (NPASS .GE. NMIN) THEN
           PASS = .true.
           GOOD_NEV = GOOD_NEV + 1
           DO I=1, N            ! N generated particles on the event
              WRITE(89,891)IEV,I,K(I,2),K(I,1),K(I,3),(P(I,J),J = 1, 5)
           ENDDO
        ENDIF
c     
c.. Print out few events on the screen
         IF (PASS .AND. GOOD_NEV.LE.NPRT) CALL PYLIST(LIST_TYPE)
      ENDDO

      WRITE(6,892) EVENT_COUNT, GOOD_NEV
      
 891  FORMAT(1x,I7,2x,I3,2x,I6,2x,I2,2x,i3,5(2x,F10.4))
 892  FORMAT(1X,'Events generated = ',1x,I8,/,
     &       1x,'Events wrote on file = ', 1x, I5)
      
      END

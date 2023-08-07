      program main
      implicit double precision(A-H,O-Z)
      implicit integer(I-N)
      INTEGER  PIDSEL, NPASS
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
      READ(*,*)NEV, NPRT
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
c
c..Loop over the events to generate
      DO 300 IEV=1, NEV
c
c..The event generation here
         CALL PYEVNT
c
c..Printout the status of the events 
         if (mod(iev,100).eq.0) print *,'Event= ',IEV
c
c..Check to see if the event pass the selection criteria
         NPASS = 0                      ! Events with photons above a cut
         DO I=1, N                      ! N generated particles on the event

c
c.. Select events that are photons and their parent is a photon that pass the pt
c.. (the check of the parent is needed because of event adjustment  
           IF (K(I,2).eq.PIDSEL .and.  K( K(I,3), 2) .eq. PIDSEL) THEN 
              PTPart = dsqrt(P(I,1)**2+P(I,2)**2)
              if (PTPart .ge. PTCUT) THEN
                 NPASS = NPASS + 1
                 IF (NPASS.GE. NMIN) GOTO 400
              ENDIF
           ENDIF
        ENDDO
 400    CONTINUE

        IF (NPASS .GE. NMIN) THEN
           DO I=1, N            ! N generated particles on the event
              WRITE(89,891)IEV,I,K(I,2),K(I,3),(P(I,J),J = 1, 5)
           ENDDO
        ENDIF
c     
c.. Print out few events on the screen
         IF (IEV.LE.NPRT) CALL PYLIST(LIST_TYPE)
 300  CONTINUE
 891  FORMAT(1x,I7,2x,I3,2x,I6,2x,i3,5(2x,F10.4))
      END

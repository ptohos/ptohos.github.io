      program main
      implicit double precision(A-H,O-Z)
      implicit integer(I-N)
      INTEGER  DECAY_LIST, LIST_TYPE
      INTEGER  PYK, PYCHGE, PYCOMP
      COMMON/PYPARS/MSTP(200),PARP(200),MSTI(200),PARI(200) 
      COMMON/PYSUBS/MSEL,MSELPD,MSUB(500),KFIN(2,-40:40),CKIN(200)
c
      CHARACTER FRAME*12, BEAM*12, TARGET*12, PARAM*100
c
c...Read parameter of PYINIT call
      DECAY_LIST = 0
      LIST_TYPE  = 1
      READ(*,*)FRAME,BEAM,TARGET,ENERGY
c
c...Read number of events to generate and print
      READ(*,*)NEV,NPRT
c
c...Read of settings and parameters
 100  READ(*,'(A)',END=200)PARAM
      CALL PYGIVE(PARAM)
      GOTO 100

 200  IF (DECAY_LIST.EQ.1) CALL PYLIST(12)
c
c..Initialize PYTHIA
      CALL PYINIT(FRAME,BEAM,TARGET,ENERGY)
 10   FORMAT(8(1x,'CKIN(',I2,')=',1x,F5.2),/)
      WRITE(6,10)(J,CKIN(J),J=1,80)
      DO 300 IEV=1, NEV
         CALL PYEVNT
         if (mod(iev,100).eq.0) print *,'Event= ',IEV
         IF (IEV.LE.NPRT) CALL PYLIST(LIST_TYPE)
 300  CONTINUE
c
c...Print Cross Section
      CALL PYSTAT(1)
      END

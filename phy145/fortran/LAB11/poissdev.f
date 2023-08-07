      SUBROUTINE POISSDEV(AMU, N, IERROR)
c====================================================
c Subroutine gia dimiourgia enos tyxaiou akeraiou 
c arithmou N>0 symfvna me thn Poissonian katanomi:
c Prob(N) = exp(-amu) * amu**N / N!
c opoy amu > 0 i mesi timi tis katanomis kai dinetai
c apo to xristi. 
c
c An den uparxei problima IERROR = 0
c diaforetika epistrefei IERROR = 1 an AMU<=0
c================================================
      IMPLICIT NONE
      INTEGER N
      INTEGER IERROR
      REAL AMU, AMUOL, AMAX
      REAL EXPMA, XRAN
      REAL RAND, PIR
      DATA AMUOL/-1./
      DATA AMAX/100./
      IF (AMU .GT. AMAX)  GOTO 500
      IF (AMU .EQ. AMUOL) GOTO 200
      IF (AMU .GT. 0.)    GOTO 100
c
c... H mesi timi prepei na einai thetiki
      IERROR = 1
      N = 0
      RETURN

c...Apothikeysi toy ekthetikou gia peretairw kliseis
 100  IERROR = 0
      AMUOL  = AMU
      EXPMA  = EXP(-AMU)
 200  PIR    = 1.
      N = -1
 300  N = N + 1
      PIR = PIR * RAND()
      IF (PIR .GT. EXPMA) GOTO 300
      RETURN

c...Proseggisi me gaussian katanomi an AMU > AMAX
 500  XRAN = RAND()
      N = XRAN*SQRT(AMU) + AMU + 0.5
      RETURN

c...An o xristis thelei na thesei ti timi AMAX gia gaussian proseggisi
c.. gia na ginei xreiazetai na kalesei kaneis to entry point: CALL POISET(VAL)
      ENTRY POISET(AMU)
      AMAX = AMU 
      RETURN
      END

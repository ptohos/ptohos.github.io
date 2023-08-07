c==========================
      Program bicycle
c==========================
      REAL DT, AHEADTIME
      REAL SPEED1, SPEED2
      REAL DIST1, DIST2, TIME
      REAL DISTAB

      WRITE(6,10)
 10   FORMAT(1x,'Eisagete tin taxytita tou 1ou podilati')
      READ(5,*)SPEED1
      WRITE(6,20)
 20   FORMAT(1x,'Eisagete tin taxytita tou 2ou podilati')
      READ(5,*)SPEED2
      WRITE(6,30)
 30   FORMAT(1x,'Eisagete tin apostasi twn 2 polewn')
      READ(5,*)DISTAB

      AHEADTIME = 2.0        ! Xroniki diafora metaksy tvn 2 podilatwn
      DT    = 0.5

      WRITE(6,40)
 40   FORMAT(2x,'Time',3x,' Apostasi 1', 3x,' Apostasti 2')

      TIME = 0.0
      DIST1 = 0.0
      DIST2 = 0.0

 50   IF (DIST1 .LT. DIST2) GOTO 60 ! O podilatis 2 perase ton 1
      IF (DIST2 .GE. DISTAB) THEN
         WRITE(6,70)
 70      FORMAT(2x,' O podilatis 2 eftase sto termatismo prin ton 1')
         GOTO 60
      ENDIF
      WRITE(6,80)TIME, DIST1, DIST2
 80   FORMAT(2x,F4.1,4x,F6.2,4x,F6.2)
      TIME = TIME + DT
      DIST1 = SPEED1 * TIME
      IF (TIME .GT.  AHEADTIME)THEN   ! >2 giati tote tha exei kinhthei o 2
        DIST2 = SPEED2*(TIME - AHEADTIME)
      ENDIF
      GOTO 50
 60   CONTINUE
      END

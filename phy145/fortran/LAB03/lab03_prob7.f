c========================
      program series_pi
c========================
      INTEGER          J, Nterm
      DOUBLE PRECISION SUM, X, Y
      DOUBLE PRECISION PI, PI_SQUARE
c     
c=======================
      PRINT *, ' Ypologismos tou pi apo p^2/6 = 1 + 1/2^2 + 1/3^2+...'
 10   PRINT *, ' Dwse posous orous tis seiras na athroisei '
      READ *, Nterm
      IF (Nterm .LT. 0) THEN
         PRINT *,' Den orisate to plithos twn orwn'
         GOTO 10
      ENDIF

      SUM = 0.       ! Arxiki timi tou athroismatos. Prepei na dilwthei 
                     ! afou diaforetika o upologistis xrisimopoiei otidipote
                     ! timi vrisketai sti mnimi tou sti thesi pou einai 
                     ! i metavliti sum
      DO J = 1, Nterm
         Y = J
         X = Y**2    ! Prosoxi oti kanw anathesi tou J^2 pou einai akeraios 
                     ! se mia REAL metabliti giati sto epomeno vima tha 
                     ! diairesw 1/J^2. An ola einai integers (diladi J^2 kai 
                     ! to 1 ston arithmiti) tote i diairesi integer/integer
                     ! dinei integer alla sto afou to piliko tha einai panta 
                     ! <1 tote i diairesi tha dinei 0   p.x. 1/2 = 0 . 
         sum = sum + 1./X 
      ENDDO
      PI_SQUARE = 6.0 * sum 
      PI        = SQRT(PI_SQUARE)
      PRINT *,' H seira dinei pi = ',pi
      END


C===========================================================
      PROGRAM POLYONYMO
C===========================================================
C  Ypologismos twn polynymvn LEGENDRE. 
C  To programma xrisimopoiei ena 
C  ypoprogramma synartsis gia ton 
C  ypologismo toy Pn(x) toy poluonumou
C  Legendre symfwva me tis anagvgiki sxesi
C             2n-1              n-1
C    Pn(x) = ------ xPn-1(x) - ------Pn-2(x)
C              n                n
C  San efarmogi kai elegxo tou kvdika 
C  to programma ypologizei kai typvnei tis times 
C  tvn polynymvn n=1,2,3,4,5 gia x=0.,0.1,0.2,0.3,...,1.0
C===========================================================
      INTEGER J, K, NSTEP, NPOL, NPOL_MAX
      REAL    X_HIG, X_LOW, STEP
      REAL    X_VAL, PLEGENDRE
      REAL    PVALUE(5,20)
C=================
C Initialization
c=================
      NPOL_MAX = 5              ! Mexri Poluwnumo 5is taksis
      DO J =1, NPOL_MAX
         DO K = 1, 20
            PVALUE(J,K) = 0.0   ! Initialize to pinaka
         ENDDO
      ENDDO
c
      STEP     = 0.1
      X_LOW    = 0.0
      X_HIG    = 1.0
      NSTEP    = 11                           ! +1 giati pigainoume apo 0 ews 1

      DO NPOL = 1, NPOL_MAX                   !  Megisto N gia upologismo
         DO J = 1, NSTEP
            X_VAL = X_LOW + STEP*(J-1)        !  0.0,0.1,0.2,...,1  (11 times)
            PVALUE(NPOL,J) = PLEGENDRE(NPOL,X_VAL) ! Klisi tis sunartisis
         ENDDO
      ENDDO
C=========================
C Ektypwsi apotelesmatwn
c=========================
      WRITE(6,20) (J, J=1,NPOL_MAX)
      DO K = 1, NSTEP
         X_VAL = X_LOW + STEP*(K-1)
         WRITE(6,21)X_VAL, (PVALUE(J,K),J=1,NPOL_MAX)
      ENDDO
 20   FORMAT(1x,' Timi tou X',4x,'P',I1,4(10x,'P',I1))
 21   FORMAT(5x,F3.1,5(3x,F9.5))
      END


C====================================================================
      REAL FUNCTION PLEGENDRE(NPOL,X_VAL)
C====================================================================
C Ypologismos poluwnumwn Legendre symfvna me tin anagwgiki sxesi. 
C
C  H synartisi einai tis morfis P(N,x), me parametrous
C  ton akeraio N kai ton pragmatiko X. Oi akraies times
C  gia NPOL=0 kai NPOL<0 yologizontai kai katopin o deiktis tou
C  poluwnumou auksanei mexri ti timi NPOL dimiourgontas
C  ta P1(x), P2(x),...,Pn(x). Kathe stigmi oi times twn 
C  2 teleutaiwn poluwnumwn kratiountai sti mnimi sa times
C  twn PVAL0 kai LEGENDRE. Otan o deiktis ginei N i sunartisi dinei 
C  tin timi tou PLEGENDRE
C
C INPUT parametroi: 
C                  NPOL : taksi tou poluwnumou
C                  X_VAL: timi tis X
c====================================================================
      INTEGER NPOL, J
      REAL    X_VAL, RJ
      REAL    PVAL0, PVAL, PLEG_NPOL
c================
C Initialization
c================
      PVAL0      = 0.      ! Arxiki timi tis synartisis an NPOL<0
      PLEGENDRE  = 1.      ! Arxiki timi tis synartisis an NPOL=0
c==========================================================
C Ousiastika exoume tis 2 prwtes times twn poluonumwn otan 
c N=1, diladi tin N-2 =-1 kai N-1=0
c========================================================== 
      DO J = 1, NPOL
         RJ = J            ! Allagi se REAL gia apofugi apokopis se diairesi
c====================================================
c Symfvna me to parapanv sxolio PLEGENDRE antistixei
c sti timi Pn-1 kai PVALO stin timi gia Pn-2
c====================================================
         PLEG_NPOL = (2.0*RJ - 1.0)*X_VAL*PLEGENDRE/RJ
         PLEG_NPOL = PLEG_NPOL - (RJ - 1.0)*PVAL0/RJ
C==============================================================
C Antikatestise wste na exoyme panta ta 2 teleutaia poluwnuma
c==============================================================
         PVAL0 = PLEGENDRE        ! H timi tou Pn-1
         PLEGENDRE = PLEG_NPOL    ! H timi tou Pn
C=================================================
C Sti epomeni epanalipsi ta dyo ayta polyvnuma 
c tha einai ta Pn-2 kai Pn-1 antistoixa gia to
C neo poluwnumo Pn
C=================================================
      ENDDO
      RETURN
      END

      REAL FUNCTION GAUSSDEV()
c=====================================
c Function gia ti dimiourgia tyxaiwn
c arithmwn me mesi timi mean=0 kai 
c typiki apoklisi 1
c Xrisimopoiei ti method Box-Muller 
c z1 = sqrt[-2*log(r1)] * cos[2pi*r2]
c z2 = sqrt[-2*log(r1)] * sin[2pi*r2]
c opoy r1 kai r2 einai 2 omoiomorfa 
c katanemimenoi tyxaioi arithmoi sto 
c diastima [-1,1]. 
c z1 kai z2 einai 2 gaussian tyxaioi 
c arithmoi. Kathe fora pou kaleitai 
c i synartisi epistrefetai enas apo 
c toys 2 arithmous. 
c=====================================
      IMPLICIT NONE
      REAL V1, V2, R, FAC
      REAL GSET
      REAL RAND
      INTEGER ISET
      DATA ISET/0/
      SAVE ISET, GSET

      IF (ISET.EQ.0) THEN
1       V1=2.*RAND()-1.
        V2=2.*RAND()-1.
        R=V1**2+V2**2
        IF(R.GE.1.)GO TO 1
        FAC=SQRT(-2.*LOG(R)/R)
        GSET=V1*FAC
        GAUSSDEV=V2*FAC
        ISET=1
      ELSE
        GAUSSDEV=GSET
        ISET=0
      ENDIF
      RETURN
      END

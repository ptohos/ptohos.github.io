c===================================
      program gaussnumbers
c===================================
      implicit none
      real xmean, xsigma
      integer nshots,nmax
      parameter(nmax=100000)
      real x(nmax)
      integer nbins, j
      parameter(nbins=100)
      integer freq(nbins)
      real    val, xval(nbins)
      integer iseed
      data iseed/12345/

      real    GaussDev

 30   print *,'Prosdioriste ton arithmo twn peiramatwn'
      read *,nshots
      if (nshots.gt.nmax) then
         print *,'Dwste mikrotero arithmo peiramatwn'
         print *,'diaforetika allakste to megethos tou pinaka'
         goto 30
      endif
      print *,'Dwste ti mesi timi tis gaussianis katanomis'
      read *,xmean
      print*, "Dwste to sigma tis gaussianis"
      read *,xsigma

      open(unit=20,file='gaussian.dat',status='unknown')
      call srand(iseed) 
      do j =1, nshots
         val = xmean + xsigma*GaussDev()
         x(j) = val
      enddo
      call histogram(x,nshots,nbins,freq,xval)
      do j = 1, nbins
         write(20,100)xval(j),freq(j)
      enddo
 100  format(1x,f8.5,2x,I6)
      close(20)
      end

c=====================================
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

c------------------------------------------------------------
      SUBROUTINE Histogram(X,N,BINS,H,XVAL)
!------------------------------------------------------------
! Ayti i subroutine sas boitha na dimioyrgisete ena pinaka
! ston opoio apouhkeyete ti syxnotita me tin opoia emfanizontai
! oi tyxaioi arithmoi X. Xwrizei kapoio diastima [xmin,xmax]
! se isa ypodiastimata (bins) me eyros binw. An o arithmos 
! einai metaksy enos ypodiastimatos [x_i,x_i+1] tote ayksanoume
! to plithos twn tyxaivn arithmvn sto ypodiastima ayto kata 1 
! Epistrefei to pinaka H pou exei ti syxnotita emfanisis twn X
! kathws kai to pinaka twn timwn twn upodiastimatwn tou X (sto XVAL) 
!------------------------------------------------------------
  	IMPLICIT NONE
  	INTEGER  N
	INTEGER BINS
  	REAL X(N), XVAL(BINS)
  	REAL   MIN, MAX, BINWIDTH
	REAL   MINVA, MAXVA
	INTEGER H(BINS),BIN,I,J,K,MaxH

	DO I = 1, BINS
	   H(I)=0
	ENDDO
	MIN = MINVA(X,N)
  	MAX = MAXVA(X,N)
  	BINWIDTH=(MAX-MIN)/REAL(BINS)
  	DO I=1,N
    	  BIN=1+(X(I)-MIN)/BINWIDTH       ! Briskoume se poio diastima 
                                          ! anikei i timi x(i) 
	  IF ( BIN .LT. 1 ) BIN=1         ! Check for underflows
	  IF ( BIN .GT. BINS ) BIN=BINS   ! Check for overflows
	  H(BIN) = H(BIN)+1               ! Ayksanoume ton arithmo sto 
                                          ! sygkekrimeno diastima
	  XVAL(BIN) = MIN+BINWIDTH/2+(BIN-1)*BINWIDTH ! To meso tou diastimatos [x_i,x_i+1]
	END DO
	RETURN
	END

	REAL FUNCTION MINVA(X,N)
	IMPLICIT NONE
	INTEGER I, N
	REAL   MIN, X(N)
	MIN = X(1)
	DO I = 1, N
	   IF (X(I).LT.MIN) THEN
           MIN = X(I)
	   ENDIF
	ENDDO
	MINVA = MIN
	RETURN
	END

	REAL FUNCTION MAXVA(X,N)
	IMPLICIT NONE
	INTEGER I,  N
	REAL   MAX, X(N)
	MAX = X(1)
	DO I = 1, N
	   IF (X(I).GT.MAX) THEN
           MAX = X(I)
	   ENDIF
	ENDDO
	MAXVA = MAX
	RETURN
	END

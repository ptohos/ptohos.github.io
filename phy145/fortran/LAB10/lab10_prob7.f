c===========================================
      program mc_transformation
c===========================================
c...Xrisimopoioume ti methodo tou
c...metasximatismou gia na dimiourgisoume
c...mia katanomi tuxaiwn arithwm 
c...sumfwna me ti sxesi P(y) = 
c...ksekinontas apo omoiomorfa 
c...katanemimenous arithmous se
c...kapoio diastima [A,B]
c...Sti periptwsi mas theloume 
c...P(y)=sin(y). Epomenws sumfwna
c...me ti methodo:
c...P(y)dy = dx => sin(y)dy=dx
c...Oloklirwsi tha mas dwsei 
c...x=-cos(y)=>y=acos(-x)
c...Epomenws pernontas y sumfwna
c...me ti sxesi acos(-x) tha 
c...prepei na paroume ta y 
c...katanemimena sumfwna me ti 
c...sxesi pou dinetai P(y)=siny
c=========================================== 
      implicit none
      integer iseed
      integer I, Ntries
      parameter(Ntries=1000000)
      real    x
c...Oi parakatw metavlites xreiazontai gia ti subroutine histogram
      integer nbins
      parameter(nbins=316)    ! Arithmos twn upodiastimatwn pou xrisimopoioume
                              ! gia na omadopoiisoume tis times tou y
                              ! Efoson to diastima toy y einai 
                              ! [0,pi] diladi [0,3.14] xwrizoume to 
                              ! diastima se 158 isa upodiastimata pou 
                              ! antistoixoun se 3.14/158 aktinia to kathena
      real y(Ntries), yval(nbins)
      integer freq(nbins)     ! Plithos timwn tis metavlitis y pou brisketai
                              ! se kathe ypodiastima. Einai akeraios

      iseed = 123456
      call srand(iseed)
      do I = 1, Ntries
         x = rand()
         x = -1. + 2*x        ! Omoiorfi katanomi sto diastima [-1,1]
         y(i) = acos(-x)      ! Ta y's tha exoun times sto diastima [0,pi]
      enddo

      call histogram(y,ntries,nbins,freq,yval)
      open(unit=20,file='katanomi_sin.dat',status='unknown')
      do I = 1, Nbins
         write(20,*)yval(i),freq(i)
      enddo
      end

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

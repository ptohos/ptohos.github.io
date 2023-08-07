c----------------------------------------
	program mcgeneration
c----------------------------------------
c To programma ayto kalei ti subroutine 
c GenKdecay gia tin paragwgi gegonotwn 
c Kaoniwn kai prosdiorismo tis apodosis
c enos anixneuti sunartisi toy xronoy 
c zwis twn paragwmenwn kaoniwn.
c To programma diavazei tis plirofories
c apo to file test.dat pou paragetai apo
c tin uporoutina GenKdecay kai upologizei
c tin apodosi tou anixneuti. 
c Katopin kalei kai pali tin yporoutina 
c gia paragwgi enos mikroterou deigmatos
c gegonotwn. H anixneusimi katanomi 
c diorthwnetai me vasi tin apodosi pou 
c posdioristike sto prwto stadio. 
c
c To programma kalei tin uporoutina histogram
c pou tropopoiithike gia na pernoume ta oria
c ta opoia theloume (elaxisto kai megisto)
c
c To programma grafei 2 output files
c efficiency.dat to opoio periexei:
c  sti 1-i stili tous xronous diaspasis (TimeCM)
c  sti 2-i stili ti syxnotita emfanisis twn TimeCM prin tin epilogi
c  sti 3-i stili ti syxnotita emfanisis twn TimeCM meta tin epilogi
c  sti 4-i stili ti efficiency (N_pass/N_all)
c correction.dat to opoio periexei
c  sti 1-i stili tous xronous diaspasis (TimeCM)
c  sti 2-i stili ti suxnotita twn timeCM meta tin epilogi kai prin diorthwsi
c  sti 3-i stili ti stili 2 diorthwmeni gia tin apodosi
c----------------------------------------
	implicit none
	integer nevts, j
	parameter(nevts=40000)
	real timeall(nevts),timepass(nevts)
	integer ipass,nev
	real    xdecay, xprod, mom, time
	real    timelow, timehigh    ! Oria gia to histogramma
	parameter(timelow=0.0)
	parameter(timehigh=5.0) 
	integer nbins, npass, iall
	parameter(nbins=100)
	integer freqtimeall(nbins)
	integer freqtimepass(nbins)
	real    efficiency(nbins)
	real    timebin(nbins)
	real    corr

	call GenKdecay          ! Paragwgi gegonotwn
	open(unit=20,file='test.dat',status='old')  ! To file dimiourgithike
	do j = 1, nevts
	   timeall(j) = -1.
	   timepass(j) =-1. 
	enddo
	read(20,*)      ! Pidame tis prwtes 2 grammes 
	read(20,*)
	iall = 0
	npass = 0
	do j = 1, nevts
	   read(20,*,end=100,err=100)nev,ipass,xprod,mom,xdecay,time
	   iall = iall + 1
	   timeall(iall) = time
	   if (ipass.eq.1) then
	      npass = npass+1
	      timepass(npass) = time ! An den perna to timepass(j)=-1
	   endif
	enddo
 100	close(20)
	call histogram(timeall,iall,nbins,timelow,timehigh,
     &                 freqtimeall,timebin)
	call histogram(timepass,npass,nbins,timelow,timehigh,
     &                 freqtimepass,timebin)
	open(unit=21,file='efficiency.dat',status='unknown')
	do j = 1, nbins
	   if (freqtimeall(j).gt.0) then 
	      efficiency(j) = float(freqtimepass(j))/float(freqtimeall(j))
	   else
	      efficiency(j) = 0.
	   endif
	   write(21,*)timebin(j),freqtimeall(j),freqtimepass(j),
     &                efficiency(j)
	enddo
	close(21)

	call GenKdecay      ! Gia 1000 events
	do j = 1, nevts
	   timeall(j) = -1.
	   timepass(j) = -1.
	enddo
	open(unit=20,file='test.dat',status='old')
	read(20,*)   ! Pidame tis 2 prwtes grammes poy periexoyn sxolia
	read(20,*)
	npass = 0
	do j = 1, nevts
	   read(20,*,end=101,err=101)nev,ipass,xprod,mom,xdecay,time
	   if (ipass.eq.1) then 
	      npass = npass + 1
	      timepass(npass) = time
	   endif
	enddo
 101	close(20)
	call histogram(timepass,Npass,nbins,timelow,timehigh,
     &                 freqtimepass,timepass)
	open(unit=23,file='correction.dat',status='unknown')
	do j =1, nbins
	   if (efficiency(j).gt.0) then 
	      corr = freqtimepass(j)/efficiency(j)  ! Diorthwsi gia apodosi
	   else
	      corr = 0.
	   endif
	   if (freqtimepass(j).ne.0) then
	      write(23,*)timepass(j),freqtimepass(j),corr
	   endif
	enddo
	close(23)
	end

c----------------------------------------
	subroutine GenKdecay	! Monte Carlo for K-decay
C----------------------------------------
c Metatropi tou programmatos GenKdecay se subroutine
c To programma grafei se kapoio file ta apotelesmata 
c tis paragwgis gegonotwn kai periexei episis mia 
c metavliti (passflag) gia to an ta gegonota pernoun 
c ta kritiria epilogis pou thetoume.
c Oi metratopes se sxesi me to arxiko programma pou 
c xrisimopoiisate sto ergastirio einai i metratropi tou
c se subroutine, i eisagwgi tis metablitis passflag
c kai to gegonos oti i pliroforia grafetai gia ola ta 
c gegonota (aneksartita apo to an pernoun ta kritiria
c epilogis i oxi) kai epipleon uparxei kai i pliroforia
c gia to an pernoun tin epilogi.  
c---------------------------------------
	integer i
	integer iseed
	data iseed/12345/
	real beta, gamma
C--------------for K-Decay---------------!
	real TauKaon, MassKaon, d1, d2, c
	real xMean, xSig, pMean, pSig
	data TauKaon  /0.894E-10/
	data MassKaon /497.7/
        data d1, d2   /10.0,40.0/ !Fiducial in cm!
        data xMean    /5.00/
        data xSig     /0.5/
        data pMean    /2000./
        data pSig     /100./
        data c        /3.00E10/
C----------------------------------------!
	integer totalGen, passflag
	real timeCM, timeLab, range
	real x0, decayLoc, P
	character yORn
c----------------------------------------!
	real rand, GaussDev              ! synartiseis gia tyxaioys arithmous
c----------------------------------------!
	logical first
	data first/.true./
	save first

	print *, 'Type total number of events to be generated  '
	read *, totalGen
	print *,' Apply cuts (Y or N)? '
	read *,yOrn
	Open(unit=15, file='test.dat',status='unknown')

	Print *,  'Monte Carlo Generation'
	Print 1000, totalGen, massKaon, d1, d2, tauKaon
	write (15,*) 'Monte Carlo Generation'
	write (15,1000) totalGen, massKaon, d1, d2, tauKaon
 1000   format(' Generated =', I5,' MassK=',F6.0, ' Cuts = d1=',f6.2,
     &         ' d2=', f6.2,' tau-K=',  E10.3)
 1100 format(1x,I6, 2x,I1, F10.2, F10.1, F10.2,F10.2)

c...Ksekinima tis akoloythias twn tyxaiwn arithmwn 
	if (first) then
	   call srand(iseed) 
	   first = .false.
	endif

	i = 0
	nSuccess = 0
	do  while (i .lt. totalGen)
	  x0       = GaussDev()*xSig+xMean     ! simeio paragwgis
	  P        = GaussDev()*pSig+pMean     ! ormi, P, kaoniou
	  beta     = P/EfromP(P,massKaon)      ! beta = u/c kaoniou
	  gamma    = gammaFromBeta(beta)       ! upologismos gamma lorentz
	  timeCM   = cmLifeTime(tauKaon)       ! dimiourgia xronoy zwis kaoniou
	  timeLab  = timeCM*gamma              ! Lorentz xfor to lab!
	  range    = timeLab*beta*c            ! kaon range!
	  decayLoc = x0+range                  ! simeio diaspasis kaoniou
	  passflag = 0
	  i = i+1
	  if (((yORn .ne. 'y')  .and. (yORn .ne. 'Y')) .or.
     &     ((decayLoc .ge. d1) .and. (decayLoc .lt. d2))) then
	    nSuccess = nsuccess+1
	    passflag = 1                      ! Simeiwsi oti to gegonos perna
                                              ! tin epilogi
	  end if
	  write(15,1100) i, passflag, x0,P,decayLoc,timeCM*1e10
	end do  ! do while i < totalGen
	write (15,*) '-1','Total generated =', totalGen,
     &              ', Number of successes =', nsuccess
	print *, 'Total generated =', totalGen,
     &           ', total successes =', nsuccess
	Close(15)
	print *, "Output file ""test.dat"" closed."
	return
	END

c---------------------------------------
	Real function EfromP(p,m)
	real p, m
	EfromP=sqrt(p*p+m*m)
	return
	end

c---------------------------------------
	Real function PfromE(e,m)
	real e,m
	PfromE = sqrt(e*e-m*m)
	return
	end

c----------------------------------------
	Real function GammaFromBeta(b)
	real b
	GammaFromBeta = 1/sqrt(1-b*b)
	return
	end

c----------------------------------------------------------
	Real function PLorentz(P,M,CosTheta,Beta,gamma)
c----------------------------------------------------------
	real P,M,CosTheta,Beta,gamma
	real EfromP
C...Ksekinontas apo Pcm and theta epistrefei Plong sto systima anaforas tou Lab!
	PLorentz = Gamma*(P*CosTheta+beta*EfromP(P,M))
	return
	end

c-----------------------------------------------
	Real function Atanth(y,x)
c-----------------------------------------------
	real y,x, th, pi
	pi = acos(-1.)
	th=atan2(y,x)
	if (x .lt. 0.) th=th+pi
	if ((x .gt. 0) .and. (y. lt. 0)) th=th+2.*pi
	Atanth=th
	return
	end


c--------------------------------------------------
	Real function cmLifeTime(tau)
c--------------------------------------------------
	real r, tau, t, rand
	r = rand()
	t = -tau*alog(1-r)
	cmLifeTime = t
	return
	end
	
c---------------------------------------------------
	REAL FUNCTION GAUSSDEV()
c---------------------------------------------------
	REAL V1, V2, R, FAC
	REAL GSET
	REAL RAND
	INTEGER ISET
	DATA ISET/0/
	SAVE ISET, GSET
	
	IF (ISET.EQ.0) THEN
 1	   V1=2.*RAND()-1.
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
	SUBROUTINE Histogram(X,N,BINS,xlow,xhi,H,XVAL)
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
  	REAL   Xlow, xhi, min, max, BINWIDTH
	INTEGER H(BINS),BIN,I,J,K,MaxH

	DO I = 1, BINS
	   H(I)=0
	ENDDO
	min = xlow
	max = xhi
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


	Program GenKdecay	!Monte Carlo for K-decay!
C----------------------------------------!
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
	integer totalGen
	real timeCM, timeLab, range
	real x0, decayLoc, P
	character yORn
c----------------------------------------!
	real rand, GaussDev              ! synartiseis gia tyxaioys arithmous
c----------------------------------------!
	print *, 'Type total number of events to be generated  '
	read *, totalGen
	print *,' Apply cuts (Y or N)? '
	read *,yOrn
	Open(unit=5, file='test.dat',status='unknown')

	Print *,  'Monte Carlo Generation'
	Print 1000, totalGen, massKaon, d1, d2, tauKaon
	write (5,*) 'Monte Carlo Generation'
	write (5,1000) totalGen, massKaon, d1, d2, tauKaon
 1000   format(' Generated =', I5,' MassK=',F6.0, ' Cuts = d1=',f6.2,
     &         ' d2=', f6.2,' tau-K=',  E10.3)
 1100 format(I6, F10.2, F10.1, F10.2,F10.2)

c...Ksekinima tis akoloythias twn tyxaiwn arithmwn 
	call srand(iseed) 

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
	  i = i+1
	  if (((yORn .ne. 'y')  .and. (yORn .ne. 'Y')) .or.
     &     ((decayLoc .ge. d1) .and. (decayLoc .lt. d2))) then
	    nSuccess = nsuccess+1
	    write(5,1100) nSuccess,x0,P,decayLoc,timeCM*1e10
	  end if
	end do  ! do while i < totalGen
	write (5,*) '-1','Total generated =', totalGen,
     &              ', Number of successes =', nsuccess
	print *, 'Total generated =', totalGen,
     &           ', total successes =', nsuccess
	pause
	Close(5)
	print *, "Output file ""test.dat"" closed."
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
	INTEGER IES
	DATA ISET/0/
	
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

c====================================================
      PROGRAM FACTORIAL
c====================================================
c To programma tha ypologisei to paragontiko
c enos tyxaiou akeraiou arithmou. 
c=====================================================
c Se periptvsi pou o xristis dvsei kapoio
c arnitiko arithmo to programma tha typvnei kapoio
c munima kai tha zita to xristi na epaneksetasei 
c ton arithmo pou edvse.
c Epidi o arithmos pou zita einai INTEGER to
c programma den tha treksei se periptvsi pou 
c o xristis dvsei kapoion REAL arithmo.
c======================================================
c Input parameters: N - O xristis dinei kapoio arithmo
c
c Output parameters: fact - to apotelesma tou N!
c======================================================
      INTEGER J, K
      INTEGER*8 N        ! Akeraios diplis akriveias
      INTEGER FACTI
      REAL    YESNO
      REAL    FACTR
      DOUBLE PRECISION FACTDB, X, P
      DOUBLE PRECISION STIRLING, VALUE
c=============================================
c Parametroi pou tha xrisimopoiisw stin 
c idiki periptvsi pou o arithmos poy 
c dinetai einai megalyteros apo 170.
c=============================================
      INTEGER*8 IEXPONENT     ! Akeraios diplis akriveias
      DOUBLE PRECISION FACTOR,  EBASE
      DOUBLE PRECISION DECIMAL, PLOG10FACT
c=============================================      
c Arxi ektelesimvn entolvn 
c===========================
      GOTO 10
 12   PRINT *,' Eisagwgi lathos typou arithmou gia to N'
      PRINT *,' O arithmos prepei na einai INTEGER typou' 
 10   PRINT *, ' Give a number to calculate its factorial'
      READ(5,11,err=12) N                    ! N exei oristei san INTEGER 
 11   FORMAT(I9)
      IF (N.LT.0) THEN
         PRINT *,'You should give a positive number to continue'
         PRINT *,'Do you want another selection? [1:YES/0:NO]'
         READ(5,*) YESNO
         IF (YESNO.EQ.1) GOTO 10     ! We want another number
         GOTO 100                    ! Finish the program
      ENDIF
c=========================================
c Arxi upologismwn tou paragontikou
c=========================================

c====================================
c Arxika me INTEGER ypologismous
c====================================
      FACTI  = 1                       ! If N=0 still the factorial = 1
      IEXPONENT = 0
      DO J = 1, N
         P     = J
         FACTR = FACTI
         IEXPONENT = LOG10(FACTR) + LOG10(P)  ! Anamenomeno apotelesma gia ton
                                              ! oro poy tha pol/stei 
         IF (IEXPONENT .GT. 9) GOTO 15
         FACTI = FACTI * J
      ENDDO
C
 15   CONTINUE
      IF (IEXPONENT .GT. 9) THEN
         PRINT *
         PRINT *,'We cannot calculate the factorial in INTEGER'
         PRINT *,'representation. Try the REAL representation '
         GOTO 20
      ELSE
         PRINT *
         PRINT *,' The Factorial of N ',N,' is equal to ',FACTI
         GOTO 100
      ENDIF
c==================================
c Trying with REAL representation
c==================================
 20   CONTINUE
      FACTR  = 1.           ! Initialization
      IEXPONENT = 0
      DO J = 1, N
         P = J
         IEXPONENT = LOG10( FACTR ) + LOG10(P) ! Anamenomeno apotelesma gia ton
                                               ! oro poy tha pol/stei 
         IF (IEXPONENT .GT. 34) GOTO 25
         FACTR = FACTR*J    ! INTEGER*REAL = REAL yperisxyei

      ENDDO
c
 25   CONTINUE
      IF (IEXPONENT .GT. 34) THEN
         PRINT *
         PRINT *,'We cannot calculate the factorial in REAL'
         PRINT *,'representation. Try DOUBLE PRECISION'
         GOTO 30
      ELSE
         PRINT *
         PRINT *,' The Factorial of N ',N,' is equal to ',FACTR
         GOTO 100
      ENDIF
c=============================================
c Trying with DOUBLE PRECISION representation
c=============================================
 30   CONTINUE

      FACTDB = 1.          ! Initialization
      IEXPONENT = 0
      DO J = 1, N
         P = J
         IEXPONENT = INT( LOG10(FACTDB) ) + INT( LOG10(P))  ! Ekthetiko
         if (IEXPONENT .GT. 305) goto 35                    ! Ekthetis > 10^305
         FACTDB = FACTDB*J
      ENDDO
C
 35   CONTINUE
      IF (IEXPONENT .GT. 305) THEN
         PRINT *
         PRINT *,'We cannot calculate the factorial with'
         PRINT *,'DOUBLE PRECISION representation'
         PRINT *,'Try something different'
         GOTO 40
      ELSE
         PRINT *
         PRINT *,' The Factorial of ',N,' is equal to ',FACTDB
         GOTO 100
      ENDIF
c
c Dokimazoume me ti methodo Stirling
c====================================
 40   VALUE = STIRLING(DBLE(N))
      PRINT *,' The Factorial of ',N,' ala Stirling einai ',VALUE
c=======================================================================
c Kai tvra to periergo tmima tou programmatos
c O arithmos einai megaluteros apo 169 kai prepei 
c na ypologisoume to paragontiko tou. Wstoso opws
c exoume dei mexri twra analoga me to ti anaparastasi
c xrisimopoioume mporoume na kratisoume megalous 
c arithmoys sti mnimi tou ypologisti. O megaluteros
c sto problima mas einai 170 kai isxuei gia arithmous
c diplis akribeias. 
c An ftasoume sto simeio ayto, simenei oti to apotelesma
c pou pirame einai poly megalo kai prepei na vroume 
c ena diaforetiko algorithmo gia na lysoume to provlima.
c++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
c Skeftite omws oti to paragontiko den einai tipota allo 
c apo mia seira ginomenvn pou poly eukola mporei na 
c metatrapei se athroisma (kai epomenvs to apotelesma 
c enos auroismatos einai mikrotero apo to ginomeno kai mporei
c na kratithei sti mnimi toy upologisti). Gia na metratrepsoume
c to ginomeno se athroisma pernoume to logarithmo toy ginomenou
c Diladi  N! = 1*2*3*4*...*N! => log(N!)=Log(1)+Log(2)+...+Log(N)
c======================================================================
c
 50   CONTINUE

      FACTOR = 0.
      DO J = 1, N
         X = J
         FACTOR = FACTOR + log(X)
      ENDDO
c==========================================================================
c Ypologisame to paragontiko se morfi athroismatos alla tha prepei na  
c typvsoume to apotelesma kai oxi to logarithmo kai epomenvs ksanagurname
c sto arxiko problima. O ypologistis den mporei na to typvsei giati tha 
c prepei na antikatastisoume to apotelesma se kapoia thesi mnimis kai 
c kseroyme oti den mporoume na to kanoyme. Exoyme to wstoso to logarithmo
c
c Kseroume omvs oti log10(x) = log10(e)*log(x) opou x = log(N!)=factor
c Me ton tropo ayto mporoume na grapsoume ton arithmo ws 10^(log10(x)) 
c Gia paradeigma an log10(x)=400.21 tote mporv na grapsv oti 
c x=10^(400.21) = 10^(400)+10^(0.21) 
c Epomenvs xreiazetai na upologizoyme to INTEGER part (I=400) kai to 
c dekadiko tmima (a=0.21) poy einai pantote <10 kai grafoume to 
c apotelesma mas me tin morfi ayti. 10^a * 10^I
c==========================================================================
      EBASE      = EXP( 1. )                        ! exp(1.) = e
c
c Allagi basis. Apo fysiko logarithmo se logarithmo 10
c
      PLOG10FACT = LOG10( EBASE ) * FACTOR          ! log10(x)=log10(e)*log(x)
      IEXPONENT  = PLOG10FACT  
      DECIMAL    = PLOG10FACT - IEXPONENT           ! dekadiko tmima
      DECIMAL    = 10.**DECIMAL
      PRINT *
      WRITE(6,99)N,decimal,iexponent
 99   FORMAT(1x,'The factorial of',1x,I5,1x,'is',F18.15,'E+',I3)
cPRINT *,' The factorial of ',N,' is ',decimal,'E+',iexponent
c========
c DONE
c========
 100  CONTINUE
      END

c==============================================
      DOUBLE PRECISION FUNCTION STIRLING(X)
c==============================================
c Ypologismos me proseggisi prwtou orou 
c Agnooume ta stoixeia pera tou 1
c===============================================
      DOUBLE PRECISION X
      DOUBLE PRECISION PI 
      PI = dacos(-1.D0)       ! Epistrofi tou pi se double precision
      STIRLING = DSQRT(2.D0*pi)*X**(X+0.5D0)*EXP(-X)
      RETURN
      END

C============================================
C Profanvs o tropos aytos den einai o 
C monadikos gia ton ypologismo toy 
C paragontikoy. Yparxoun sunartiseis 
C proseggisis poy mporoun na ypologisoun
C to idio poly pio grigora. Ksefeugoun
C wstoso apo to skopo tis askisis aytis 
C poy perissotero exei na kanei me tin 
C xrisi tvn diaforvn typvn metavlitvn kai 
C toys periorismoys poy dimioyrgoyn oi 
C diaforoi typoi stin apothikeysi toys 
C ston ypologisti. 
C O parakatv algorithmos stamata na leitourgei
C otan o arithmos pou dinoyme (kai orizetai san 
C integer diplis akriveias) kseperasei to megisto 
C arithmo autou tou tupou pou mporei na apothikeysei
C o ypologistis. Ayto sumbenei gia N = ~9*10^17
C Telika o ypologismos diakoptetai oxi apo ton
C ypologismo toy paragontikou alla apo ton idio to 
C aritmo.
C===================================================

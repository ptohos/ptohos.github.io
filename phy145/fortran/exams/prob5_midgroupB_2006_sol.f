c===============================
      program digitfinder
c===============================
      IMPLICIT NONE
      INTEGER      I, J, NLines
      INTEGER      Number, NDigi
      INTEGER      NRead, Ntotal
      INTEGER      MAXDIGI
      PARAMETER    (MAXDIGI=9)         ! Use of parameter.
      INTEGER      DIGIMAT(MAXDIGI)
      INTEGER      NSum
      CHARACTER*50 FILENAME
c- Function used
      INTEGER GET_DIGITS
c
c Initialize ton pinaka DIGIMAT
c===============================
      DO J = 1, MAXDIGI
         DIGIMAT(J) = 0
      ENDDO
c
c Get the file that contains the data
c=====================================
      PRINT *,' Dwse to onoma tou file me tous arithmous'
      READ *,filename
c
      PRINT *,' Opening file:',filename
      OPEN(UNIT=30,FILE=FILENAME,STATUS='OLD')
c
      NLines = 0          ! Metritis gia ola ta records pou diavazei
      NRead  = 0          ! Metritis mono gia ta epeksergazomena records
c
 50   READ(30,*,END=40,ERR=60) Number
      NLines = NLines + 1
      IF (Number.LT.0) GOTO 50    ! An exoume arithmo<=0 diabase ton epomeno

c============================================
c Kyria leitourgeia tou programmatos. 
c Klisi tis synartisis pou vriskei to 
c plithis twn psifiwn enos arithmou
c *** Note>> Oi elegxoi mporoun na ginontai
c kai mesa sti function GET_DIGITS kai na 
c exoume mia akoma parametro IFLAG i opoia
c na mas pliroforei an ola itan ok, an kapoios
c arithmos einai arnitikos i an kapoios
c arithmos exei perissotera apo MAXDIGI psifia
c============================================
      NDIGI = GET_DIGITS(Number)

c==================================================
c Elegxos katallilotitas arithmou psifiwn 
c Den theloume o pinakas DIGIMAT na bgei 
c ektos oriwn (1-MAXDIGI) an o arithmos psifiwn 
c einai megaluteros apo MAXDIGI i 0
c================================================= 
      IF (NDIGI .LE. 0 .OR. NDIGI .GT. MAXDIGI) THEN
         PRINT *,' Illegal arithmos psifiwn '
         PRINT *,' O arithmos ', Number, ' exei ',NDIGI,' psifia'
         PRINT *,' Skipping the number'
         GOTO 50
      ENDIF
c==================================================================
c Debugging. Typwse tous 10 prwtous arithmous kai ton arithmo
c twn psifiwn pou briskoume gia na doume oti to programma einai ok
c================================================================== 
      IF (NREAD .LT. 10) THEN
         WRITE(6,200)Number, NDIGI
      ENDIF
c
c Ayksisi tis analogis thesis tou pinaka sixnotitas psifiwn
c===========================================================
      DIGIMAT(NDIGI) = DIGIMAT(NDIGI) + 1
c
c====================================================
c Ayksisi tou counter twn epeksergazmenwn arithmwn
c Ksekinontas apo NRead=0 kai auksanontas to plithos
c tous edw eimaste sigouroi oti exoume to akribes 
c plithos tous
c===================================================
      NRead = NRead + 1
      GOTO 50
c
 60   PRINT *,' Wrong input number on record',NLines
      PRINT *,' Skipping record'
      GOTO 50
c
c Telos tou file
c================
 40   CLOSE(30)
c=====================================================================
c Cross check apotelesmatwn. 
c To plithos twn arithmwn opws katataxtikan ston pinaka DIGIMAT
c prepei na einai idio me to plithos twn arithmwn pou epeksergastikan
c=====================================================================
      NSum = 0
      DO J = 1, MAXDIGI
         NSum = NSum + DIGIMAT(J)
      ENDDO
      WRITE(6,100)NRead, NSum
      IF (NSum .NE. NRead) THEN
         WRITE(6,101)
      ENDIF

 100  FORMAT(1x,43('='),/,5x,'Apotelesmata katamerismou psifiwn',/,
     &       1x,'Diavastikan synolika',1x,I6,1x,'arithmoi',/,
     &       1x,'kai katameristikan',1x,I6,1x,'arithmoi',/,1x,43('='))

 101  FORMAT(1x,' *** Asyngxronos arithmos stoixeiwn *** Please check') 
 102  FORMAT(14x,'Analytika apotelesmata')
 103  FORMAT(1x,'To plithos twn',1x,I1,'-psifiwn arithmwn einai:',1x,I5)
 200  FORMAT(1x,'O arithmos',1x,I9,' exei',1x,I1,1x,'psifia')
c
c Ektypwsi apotelesmatwn
c=======================
      WRITE(6,102)
      DO J = 1, MAXDIGI              ! Loop ws pros ta pithana psifia
        IF (DIGIMAT(J).GT.0) THEN    ! An uparxei o arithmos psifiwn
           WRITE(6,103)J,DIGIMAT(J)
        ENDIF
      ENDDO
C
      END

c============================================
      INTEGER FUNCTION GET_DIGITS(MYNUMBER)
c============================================
      IMPLICIT NONE
      INTEGER MYNUMBER, INum
      INTEGER IK
      INTEGER NSum
c
      INum = MyNumber
      NSum = 0

c Diairoume ton arithmo me 10 kai to piliko to thetoume sa to neo 
c arithmo. Kathe diairesi mas dinei ena psifio. H diadikasia stamta
c otan to piliko ginei miden opote exoume monopsifio arithmo
      
 10   IK = INum/10
      INum = IK
      NSum = NSum + 1
      IF (INum.GT.0) GOTO 10
      GET_DIGITS = NSum
      RETURN
      END

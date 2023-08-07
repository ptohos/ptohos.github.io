      program prime
c=============================================================
c Ayto to programma upologizei oloys toys prwtous tripsifious
c arithmous pou to teleytaio psifio tous einai INUM to opoio
c dinetai apo to pliktrologio
c
c Yparxoun diaforoi algorithmoi eyresis prwtwn arithmwn, apo 
c poly aplous (gia ti periptwsi poy o arithmos pou eksetazoyme
c einai mikros) mexri arketa periplokous, idiaitera gia polu 
c megalous arithmous. 
c
c Symfwna me to themeliwdes theorima tis arithmitikis kathe 
c thetikos akeraios arithmos mporei na grafei sa ginomeno
c prwtwn arithmwn me monadiko tropo. Diladi an dothei enas
c akeraios A tote mporei na paragotopoiithei, na grafei me ti morfi:
c A = b^i * c^j * d^k *... opoy b,c,d einai prwtoi arithmoi
c An o akeraios mporei na grafei mono san A = 1 * A tote o 
c akeraios einai prwtos (diareitai diladi mono me to eayto tou)
c Apo to parapanw theorima prokuptei oti oloi oi artioi arithmoi
c den einai prwtoi. Epomenws enas aplos algorithmos euresis 
c an kapoios arithmos einai prwtos, einai na eksetasoume an 
c o arithmos diaireitai mono me perittous arithmous mia kai an 
c diaireitai me tous artious tote tha mporei na analythei wste
c na periexei kapoion oro tis morfis 2^k. 
c Wstoso de xreiazetai na eksetasoume olous tous perittous arithmous
c gia na doume an diairoun ton arithmo N pou mas dinetai. Arkei na
c eksetasoume toys perittous mexri N/2. Akomi perissotero arkei na
c eksetasoume olous tous perittous mexri tin timi tis SQRT(N).
c Ayto giati symfwna me to thewrima twn prwtwn arithmwn kai tis
c grafis enos akeraiou, i tetragwniki tou riza tha einai o
c megalyteros prwtos poy tha mporei upsomenos sto 2 
c (mikroteros ekthetis) na dwsei ton arithmo N.
c Oloi oi perittoi arithmoi > SQRT(N) pol/smenoi me SQRT(N) tha
c dinoun apotelesma megalutero apo N, i tha prepei na pol/stoun
c me kapoio apo tous prwtous arithmous < SQRT(N) kai epomenws
c o N den tha einai prwtos. 
c=============================================================
      IMPLICIT NONE
      INTEGER J, L, INUM
      INTEGER KPRIM, LDIV, NPRIM
      INTEGER MDIV, NYPOL
c
 
 10   PRINT *,'Psifio sto opoio tha teleiwnoun oi prwtoi arithmoi'
      READ*,INUM
      if (mod(INUM,2).eq.0) then 
        print *,'O akeraios den mporei na teleiwnei se artio noumero'
        print *,'Dwse ena allo peritto psifio'
        goto 10
      endif

      DO 20 KPRIM = 101, 999, 2         ! Vima 2 gia na pernw mono perittous
         MDIV = INT(SQRT(float(KPRIM))) ! Eyresi tis tetragwnikis rizas tou 
                                        ! arithmou KPRIM. 
                                        ! H Float() metatrepei akeraio se real

         DO LDIV = 3, MDIV, 2       ! Dokimazoume oloys toys perittous apo 3 
           NYPOL = MOD(KPRIM,LDIV)  ! mexri sqrt(KPRIM). An to ypoloipo=0 tote 
           IF (NYPOL.EQ.0) GOTO 20  ! o KPRIM diaireitai akrivws ara den einai 
                                    ! prwtos kai exetazoume ton epomeno KPRIM
         END DO                    

         NPRIM = NPRIM + 1          ! An ftasame edw tote exoume ena prwto.

         IF (MOD(KPRIM,10).EQ.INUM) THEN  ! Exetazoume to teleutaio psifio 
            WRITE(6,30)KPRIM              ! gia na doume an isoutai me to 
         ENDIF                            ! psifio pou epithymoume
 20   CONTINUE
 30   FORMAT(1x,'O arithmos',1x,I3,1x,'einai prwtos')
      END

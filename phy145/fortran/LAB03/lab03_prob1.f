c=====================
      program petrol
c=====================
      INTEGER NSTOPS, KM_PER_LT
      REAL    LASTFILLUP, DIST
      REAL    GAS_USED

      PRINT *, ' Posa Km ekane?'
      READ *, DIST
      PRINT *, ' Pose staseis ekane?'
      READ *, NSTOPS
      PRINT *, ' Posi venzini ebale sto telos?'
      READ *, LASTFILLUP
      
c Ypologizoume tin venzini pou evale
c====================================
      GAS_USED = 40.*NSTOPS + LASTFILLUP  ! 40 litra/stasi + teleytaio gemisma
c
c Diaroume tin apostasi me tin venzini poy evale opote exoume km/lt
c H diairesi tha mas dwsei ena piliko metaksu 2 akeraiwn 
c An prosthesoume 0.5 tote an to piliko dist/gas_used itan panw apo 0.5 
c prosthetontas 0.5 tha pame ston epomeno akeraio, an oxi tha parameinoume 
c sto xamilotero akeraio. px. 12.6 + 0.5 = 13.1 opote kanoume stroggulopoiisi
c ston upsilotero akeraio. An eixame 12.2 + 0.5 = 12.7 opote eksakolouthoume 
c na eimaste ligotero apo 13. 
c Fusika auto pou kanoume einai na kanoume anathesi tis posotitas sta 
c deksia se ena akeraio opote exoume apokopi twn dekadikwn. Diladi 13.2 ->13
c enw 12.7 -> 12. Opote i stroggulopoiisi ginetai ston akeraio 
c====================================
      KM_PER_LT = DIST/GAS_USED + 0.5
      Print *,' H mesi katanalwsi itan ', KM_PER_LT, ' km/lt'
      END
      

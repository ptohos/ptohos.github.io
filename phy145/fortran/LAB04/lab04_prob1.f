c========================
      program pinakas
c========================
      INTEGER I, K, N, NMAX, NREAD
      REAL    A(100), X
c
c Dinoume arxikes times sto pinaka
c==================================
      NMAX = 100         ! Megethos pinaka
      DO I = 1, NMAX
         A(I) = 0
      ENDDO
c
      open(unit=69,file='lab04_prob1.dat',status='old',err=20)
      K = 0
      I = 1

 5    K = K + 1
      read(69,*,end=10,err=15) A(I)
      NRead = I             ! Tosoi arithmoi diavastikan pragmatika. 

      I = I + 1             ! Ti teleutaia fora to I tha ginei 21 alla den 
                            ! tha diabasoume mia kai to file tha teleiwsei
                            ! Epomenws tha exoume ena epipleon stoixeio apo 
                            ! ta sunolika stoixeia tou file

      if (I.LE.NMAX) then   ! Nmax =100 megethos tou pinaka. Den xreiazetai na 
         goto 5             ! gemisoun ola alla tha prepei na eimaste sigouroi
                            ! oti ta stoixeia pou diavazoume den einai 
                            ! perissotera apo 100
      else
         write(6,3) NRead
         write(6,4)
 4       format(1x,'Afinoume ta ypoloipa stoixeia')
         goto 25
      endif
c============================================================
c Oi epomenes 3 entoles ektelountai mono an yparksei problima
c me to file. Diaforetika den prokeitai na ektelestoun pote
c aytes oi entoles 
c============================================================

 20   Print *,' To file lab04_prob1.dat den mporei na anoixthei'
      Print *,' check the file name - Stopping execution'
      Stop
      
c=================================================================
c Sto tmima ayto erxomaste mono an uparksei sfalma stin anagnwsi
c Gia to logo ayto xrisimopoieitai o metritis K wste na kseroume 
c se poio simeio diabasame lathos stoixeio. To stoixeio ayto 
c paraleipetai apo tin eisagwgi stoixeiwn tou pinaka afou to I 
c den ayksanei
c================================================================
 15   write(6,2)K
 2    format(1x,'Lathos format record',1x,I3,1x,'tou file',/,
     &       1x,'parablepoume to record auto')
      goto 5
      
c=================================================================
c Sto tmima ayto erxomaste mono an teleiwsei to file enw 
c prospathousame na diavasoume perissotera stoixeia. 
c Apla typwnoume posa stoixeia diavasame
c================================================================
 10   write(6,3) NREAD
 3    format(1x,'Diavasame',1x,I3,1x,'stoixeia apo to file')

 25   CLOSE(69)     ! Mporoume na kleisoume to file 

      PRINT *,'============================'
      PRINT *,'     STOIXEIA TOU PINAKA    '
      DO I = 1, NREAD
         PRINT *,A(I)
         ENDDO
      PRINT *,'========================================'
      PRINT *,' STOIXEIA TOU PINAKA ME ANAPODH FORA    '
      DO I = NREAD, 1, -1         ! Apo to teleutaio stoixeio sto 1o me vima -1
         PRINT *,A(I)
      ENDDO
      PRINT *,'========================================'


      END

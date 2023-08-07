c========================
      program suma75
c========================
      INTEGER I, J, N, NMAX, IMAX, Ntot
      INTEGER A(25), Nrecord, Ndouble, Target
c
c Dinoume arxikes times sto pinaka
c==================================
      NMAX = 25         ! Megethos pinaka
      DO I = 1, NMAX
         A(I) = 0
      ENDDO
      PRINT *,'Poio einai to epithumito athroisma?'
      READ *,Target
c
      open(unit=99,file='lab04_prob4.dat',status='old')
      Ndouble = 0
      K = 0
      I = 1
 15   Ntot = K
      K = K + 1                      ! Metrame synolika records toy file
      read(99,*,err=20,end=30)A(I)   ! I einai to record pou kataxwreitai

      do j = 1, i-1                  ! Elegxos gia to an uparxei idi stoixeio
                                     ! kataxwrimeno
         if (A(I).eq.A(J)) then 
            If (Ndouble.eq.0) then 
               Print *,'**********************************************'
            endif
            PRINT *,' To record ',K, ' me arithmo ',A(K),
     &              ' exei idi kataxwrethei sti thesi', J
            Ndouble = Ndouble + 1
            goto 15
         endif
      enddo
      Nrecord = I
      I = I + 1
      if (I.gt.NMax) goto 35    ! Ftasame sto orio tou pinaka 
      goto 15

 20   PRINT *,' Lathos format record sto stoixeio ',K
      PRINT *,' Anagnwsi toy epomenou record'
      goto 15
 30   PRINT *,' *********************************************' 
      PRINT *,' Diavastikan ',Ntot,' records'
      PRINT *,' Sumplirwthikan ',Nrecord,' theseis tou pinaka'
      PRINT *,' Brethikan ',Ndouble,' records'
      PRINT *,' *********************************************' 
 35   CLOSE(99)

c
      PRINT *,'Ta zeygi twn stoixeiwn me athroisma ',Target,' einai' 
      DO I = 1, NRecord-1     ! Eksetazoume ta stoixeia tou pinaka
         DO J = I+1, NRecord  ! se zeygos me ta stoixeia tou pinaka 
                              ! pou vriskontai stis epomenes theseis. 
                              ! Afou theloume zeugi to ekswteriko loop
                              ! pigenei mexri N-1 wste to eswteriko loop
                              ! na kalypsei tin teleytaia thesi
            ISUM  = A(I) + A(J)
            IF (ISUM .EQ. TARGET) THEN
               PRINT *,'(',A(I),',',A(J),')'
            ENDIF
         ENDDO
      ENDDO
      END

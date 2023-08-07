c===========================
      Program ThreeDoor
c===========================
      implicit none
      integer iseed, j
      data iseed /123456/
      integer taken(3), ifree(3), nfree
      integer iprize, iselect, iopen, ichoice, iswap
      integer ngames, n_no_change, n_change
      integer igame
      real prob(3), bprob(2)
c
      print *,'Dwse ton arithmo twn paixnidiwn pros prosomoiwsi'
      read *,ngames

      call srand(iseed) ! initialize tin akoulouthia twn tyxaiwn arithmwn
      n_no_change = 0   ! synolikos arithmos epityxiwn xwris allagi portas 
      n_change = 0      ! synolikos arithmos epityxiwn otan allazei porta
      do igame = 1, ngames
c
c Prosdiorismos tis portas me tin ferrari
c
         iprize = 1 + int(3*rand())
c
c Epilogi tyxaias portas apo ton paikti 
c
         iselect = 1 + int(3*rand())
c
c Metrima epituxiwn xwris allagi portas 
c
         if(iselect.eq.iprize) n_no_change = n_no_change + 1
c
c Prosdiorismos tis portas pou anoigei o parousiastis 
c
c Den prepei na einai i porta pou exei epilexei o paiktis 
c i ayti pou exei tin ferrari se periptwsi pou i epilogi 
c tou paikti den exei ferrari. 
c Stin periptwsi pou i ferrari einai piso apo tin porta
c pou exei epileksei o paiktis, o parousiastis 
c anoigei mia opoiadipote apo tis alles 2 portes
c
         nfree = 0
         do j=1,3
            taken(j) = 0
            ifree(j) = 0
         end do
         taken(iselect) = 1
         taken(iprize) = 1
         do j=1,3
            if(taken(j).eq.0) then 
               nfree = nfree + 1
               ifree(nfree) = j
            endif
         end do
         iopen = ifree(1)       ! Epilogi tis 1is eleytheris portas
         if (nfree.eq.2) then   ! An uparxoun 2 eleytheres portes anoigma tyxaia
            ichoice = 1 + int(2*rand())
            iopen = ifree(ichoice) 
         endif
c
c Eponenws i porta tin opoia mporei na epilexei o paiktis einai:
c
         do j=1,3
            if(j.ne.iopen.and.j.ne.iselect) iswap = j
         end do
c
c Metrima twn epituxiwn epilegontas tin alli kleisti porta
c
         if(iswap.eq.iprize) n_change = n_change + 1
      enddo
c
      write(6,*) 'Arithmos paixnidiwn ',ngames
      write(6,*) 'Arithmos epityxiwn xwris allagi portas/ pithanotita ',
     &            n_no_change, 100.*n_no_change/ngames
      write(6,*) 'Arithmos epityxiwn me allagi portas/ pithanotita    ',
     &            n_change, 100.*n_change/ngames
c==========
      print *," =========================== "
      print *," Deyteros aploysteros tropos "
      print *," =========================== "
c==========
      n_no_change = 0
      n_change = 0
      do igame = 1, ngames
         prob(1) = rand()
         prob(2) = rand()
         prob(3) = rand() 
         ichoice = 1 + int(3.0*rand())
         bprob(1) = prob(ichoice)
         if(ichoice.eq.1) bprob(2) = max(prob(2),prob(3))
         if(ichoice.eq.2) bprob(2) = max(prob(1),prob(3))
         if(ichoice.eq.3) bprob(2) = max(prob(1),prob(2))
         if(bprob(1).ge.bprob(2)) then
            n_no_change = n_no_change + 1
         else
            n_change = n_change + 1
         end if
      end do
c***  average number of games and wins
      write(6,*) 'Arithmos paixnidiwn ',ngames
      write(6,*) 'Arithmos epityxiwn xwris allagi portas/ pithanotita ',
     &            n_no_change, 100.*n_no_change/ngames
      write(6,*) 'Arithmos epityxiwn me allagi portas/ pithanotita    ',
     &            n_change, 100.*n_change/ngames
      end



      program poisson
c=====================================
c To programma ayto upologizei tin
c Poissonian pithanotita na vrethoyn
c J gegonota otan o mesos arithmos 
c gegonotwn einai A.
c To programma upologizei tin pithanotita
c gia oles tis periptwseis gegonotwn apo
c 1 ews J. 
c Prosoxi xreiazetai ston upologismo 
c tou paragontikou opou i xrisimopoiisi 
c INTEGER typou metavlitis odigei se 
c uperxeilisi
c=====================================
      implicit none
      integer j, Nev, Nmean
      real    factorial
      real    prob

      print *,'Dwste to meso arithmo gegonotwn'
      read *,Nmean
      print *,'Dwste ton arithmo twn paratiroumenwn gegonotwn'
      read *,Nev
      factorial = 1.
      do j = 1, Nev
         factorial = factorial * j
         prob = Nmean**float(j)*exp(-float(Nmean))/factorial
         write(6,10)j,Nmean,prob*100
      enddo
 10   format(1x,'H pithanotita na paratirithoun',1x,i2,1x,'gegonota',
     &       1x,'enw anamenontan',1x,i3,1x,'einai',1x,F8.5,'%')
      end

c==========
c O parapanw tropos epilexthike giati o arithmos twn gegonotwn einai 
c seiriakos 1,2,3,...,20 opote to paragontiko gia kathe periptwsei 
c prokyptei apo to proigoumeno pol/zontas me to neo arithmo. 
c Kapoios tha mporouse na upologizei to paragontiko se kathe periptwsi 
c apo tin arxi. 
c
c  Do j = 1, Nev
c    factorial = 1.
c    do k = 1, j
c      factorial = factorial * k   !<< Upologismos akrivws tou paragontikou
                                   !<< gia kathe periptwsi
c    enddo
c    prob = Nmean**float(j)*exp(-float(Nmean))/factorial
c==========

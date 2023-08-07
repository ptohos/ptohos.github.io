      program zaria
      implicit none
      integer j,k,l,ipa, Nshots
      integer iseed, nzaria
      parameter(nzaria=10)
      integer freq(nzaria+1), inum
      real theory, anal

      print *,'Arithmos prospatheiwn?'
      read*,Nshots
      open(unit=20,file='zaria.dat',status='unknown')
      iseed= 123456
      call srand(iseed)
      do j = 1, nzaria+1
         freq(j) = 0
      enddo
      do j = 1, Nshots
         ipa = 0
         do k = 1, nzaria
            l = 1 + int(6*rand())
            if (l.eq.6) ipa = ipa+1
         enddo
         freq(ipa+1) = freq(ipa+1)+1
      enddo
      do j = 1, nzaria+1
         write(20,20)j-1,freq(j)
         anal = theory(j-1,nzaria)
         write(6,21) j-1, freq(j), nshots,freq(j)*100./nshots, anal*100.
      enddo
 20   format(1x,i2,2x,i9)
 21   format(1x,'Akrivws ',1x,i2,1x,'zaria na feroun 6 symbainei se',
     &       1x,i9,1x,'prospatheies apo tis ',I9,/,
     &       1x,'H pithanontita einai:',1x,E11.5,1x,'%',
     &       1x,'me anamenomeni theoritika:',1x,E11.5,1x,'%')
      end

c=================================================
      real function theory(npass,ntot)
c=================================================
c Ypologismos tis dionimikis pithanotitas na 
c paroume npass epityxies apo tis sunolikes ntot 
c dunates prospatheies
c=================================================
      implicit none
      integer npass, nfail, ntot
      real probpass, probfail
      real fact, prob

      probpass = 1./6.
      probfail = 1.-probpass
      nfail    = ntot - npass

      prob = fact(ntot)/fact(npass)/fact(nfail)
      prob = prob * (probpass)**npass * (probfail)**nfail
      theory = prob
      return
      end

c==================================================
      real function fact(number)
c==================================================
c Ypologismos tou paragontikou
c==================================================
      implicit none
      integer number,j
      
      fact = 1.
      if (number.lt.0) then 
         print *,'Lathos eisagwgi arithmou gia upologismo paragontikou'
         print *,'Stop execution'
         stop
      endif
      if (number.eq.0) return
      do j = 1, number
         fact = fact * j
      enddo
      return
      end

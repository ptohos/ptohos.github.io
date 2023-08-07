      program summation
      implicit none
      integer Low_End, Hi_End, Integ
      integer isum, numb
      real    ave, sum

 10   print *,'Give the Lower Integer'
      read *,Low_End
      print *,'Give the Upper Integer'
      read *,Hi_End
      if (Hi_End .le. Low_End) then 
         print *,'Lathos oria diastimatos'
         print *,'Upper End ',Hi_End,' is < Low_End ',Low_End
         print *,'Please select again'
         goto 10
      endif
c     
c Efoson theloyme to athroisma twn akeraiwn apo Low_End
c mexri Hi_End, xreiazetai na grapsoume ena brogxo poy 
c tha arxizei na metra apo Low_End+1 (anoikto diastima) 
c mexri Hi_End-1 kai na ayksanei kata monada. Prepei 
c akoma na kratame to plithos twn epanalipsewn wste sto
c telos na upologisoume to meso oro.
c
      isum = 0.0 ! Prepei na midenisoume to athroisma 
                 ! diaforetika o upologistis tha parei 
                 ! sto sum opoiadipote timi vrisketai 
                 ! sti mnimi tou. Dokimaste na deite ti 
                 ! tha simvei an den exete thesei to isum=0
      numb = 0
      DO Integ=Low_End+1, Hi_End-1
         isum = isum + integ    ! prosthetw sto sum to 
                                ! neo akeraio. Akeraio athroisma
         numb = numb + 1        ! Prosthesa ena neo akeraio
      enddo

      sum = isum                ! Metatropi se real wste na upologistei
                                ! swsta o mesos oros diaforetika tha 
                                ! exoume diairesi akeraiwn kai epomenws
                                ! apokopi dekadikwn psifiwn

      if (numb.gt.0) then       ! Elegxos giati mporei to
                                ! diastima pou dwsame na min
                                ! periexei akeraio 
         
         ave = sum/numb
      else
         ave = 0.0
      endif
      print *,"======================================================="
      print *,"Athroisma akeraiwn sto diastima (",Low_End,Hi_End,")"
      print *,"Brethikan ",numb," akeraioi"
      print *,"Me athroisma ",isum
      if (numb.gt.0) then 
         print *,"O mesos oros einai ",ave
      else
         print *,"Den yparxei mesos oros"
      endif
      print *,"======================================================="
      end

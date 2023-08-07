      program makesum
      implicit none
      integer I, Nterms, Nmax_Term
      Double Precision R, SUM, Sum_N, Term, OldTerm
      Double Precision epsi

      Sum_N = 0.0D0  ! To athroisma twn N prwtwn orwn
      Sum   = 0.0D0  ! Midenizoume to athroisma
      print *,"Dwste tin timi tou r"
      read *,R
      print *,"Dwste to plithos twn orwn tou 1ou athroismatos"
      read *, Nmax_Term
      print *,"Dwste tin epithumiti akriveia tis apeiris seiras"
      read *,epsi

 
      I = 0           ! Ksekiname apo I=0 wste ti prwti fora na exoume I=1
      Term = 1.0D0    ! Otan I=0 tote o oros einai term = R**0 = 1
      OldTerm = Term

 10   I = I + 1
      Term = Term*R   ! Kathe neos oros prokyptei apo to proigoumeno 
                      ! pol/zontas me R. 
      if (term .ge. epsi) then ! Eksetazoume an o neos oros > akriveia
         Sum = Sum + term
         if (I.eq.Nmax_Term) Sum_N = Sum
         Nterms = I
         OldTerm = Term
         goto 10             ! Synexizoume ston epomeno oro (Auksanoume to I)
      else
         goto 20             ! Petyxame tin epithumiti akriveia opote tha 
                             ! typwsoume ta apotelesmata
      endif
 20   continue               ! Edw erxomaste otan petuxoume tin akriveia 
                             ! diaforetika to programma den ekserxetai apo to 
                             ! loop tou athroismatos

      print *,"========================================================"
      print *,"Apotelesmata tou athroismatos tis seiras Sum_i=1 r^i "
      print *,"gia r = ",R
      print *,"To athroisma twn ",Nmax_term," prwtwn orwn einai: ",Sum_N
      print *,"To athroisma gia n->inf kai akriveia",epsi," einai: ",Sum
      print *,"H akribeia symvainei gia n = ",I-1," me term = ",OldTerm
      print *,"Enw o ",I,"-th oros isoutai me term = ", term
      print *,"========================================================"
      end

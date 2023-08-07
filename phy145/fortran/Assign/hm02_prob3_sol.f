      program seira
c==================================================
c To programma ayto upologizei
c tin apeiri seira:
c  y=f(x) = 0.6 - 1/x + 1/(3x^3) - 1/(5x^5)...
c me akriveia 10^-5 (dinetai apo to pliktrologio) 
c H seira ypologizetai gia times tou 
c x sto diastima [xmin,xmax] me vima xstep
c==================================================
      implicit none
      integer nold, nterm, nterms_used
      real akriveia
      real x, xmin, xmax, xstep
      real sum, term

      print *,'Dwste tin epithumiti akriveia tou athroismatos'
      read *, akriveia
      print *,'Dwste tin min kai max timi tou x'
      read *,xmin, xmax
      print *,'Dwste to vima ayksisis tou x'
      read *, xstep
      x = xmin

      do while (x.le.xmax)
         nterms_used = 0
         sum         = 0.6            ! O statheros oros tis seiras
         nterm       = 1
         term        = -1./x          ! O prwtos oros tis seiras
         do while (abs(term).gt.akriveia) 
            nterms_used = nterms_used + 1
            sum = sum + term
            nold  = nterm             ! Kratame ton proigoumeno syntelesti 
            nterm = nterm + 2         ! O syntelestis tou neou orou
            term  = -term*nold/x**2/nterm  ! O neos oros prokuptei apo ton 
                                           ! proigoumeno diairontas me x^2
                                           ! kai pol/zontas me ton proigoumeno
                                           ! suntelesti (1,3,5,7) kai diairontas
                                           ! me ton neo suntelesti (3,5,7...)
                                           ! Parallila allazoume to prosimo
                                           ! O parapanw tropos apofeugei ton 
                                           ! upologismo megalwn arithmwn kathe
                                           ! fora 
         enddo
         write(6,10)x, sum, nterms_used
         x = x + xstep
      enddo
 10   Format(1x,'Gia x =',1x,F3.1,1x,'f(x) =',1x,F8.5,
     &       1x,'xrisimopoiontas',1x,i5,1x,'orous')
      end
c===============
c To eyros twn timwn tou x tha mporouse kapoios na to upologisei ws eksis:
c nsteps = (xmax - xmin)/xstep + 1
c x = xmin
c do i = 1, nsteps
c    idies entoles opws kai proigoumenws
c    x = x+xstep
c enddo
c================

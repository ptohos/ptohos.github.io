c========================================
      program bisection
c========================================
c Sti parakatw lusi mporeite na deite 
c pws apofeugoyme to problima opoy opoio
c h synartisi ti lusi tis opoias psaxnoume 
c einai fthinousa. Thymitheite oti to 
c programma poy uparxei sa paradeigma 
c stis dialekseis kai oi perissoteroi 
c kanate sto lab upothetei oti i sunartisi
c einai ayksousa opote sto aristero orio 
c poy dinete, i synartisi einai arnitiki 
c kai sto deksi einai thetiki. 
c Gia to logo ayto brikate ti lusi tis 
c sunartisis f(x) = x-cos(x)
c An theorisoume omws oti f(x) = cos(x) - x 
c tote i sunartisi einai fthinousa alla 
c kai sto katw orio i f(x) einai thetiki 
c enw sto panw orio i f(x) einai arnitiki
c kai epomenws den tha breite pote ti lusi
c me vasi to kwdika pou exete grapsei. 
c Mporeite na to dokimasete. 
c========================================
c Apli efarmogi tis bisection methodou
c========================================
      implicit none
      integer niter
      double precision tol     ! I akriveia pou zitate
      double precision X1, X2  ! oria tou diastimatos poy periexoun ti lysi
      double precision XL, XR, X_MID, X, DX
      double precision FXL, FXR, F_MID
      double precision root
      double precision func

      print *, ' Dwse ta oria tou diastimatos poy periexoun ti riza'
      read *, x1, x2
      print *, ' Poia i epithumiti akriveia'
      read *, tol

      XL    = x1
      XR    = x2
      niter = 0
      FXL   = func(xl)
      FXR   = func(xr)
c======================================================================
c Elegxos an to diastima periexei lysi tis synartisis
c======================================================================
      if ( (FXL*FXR).GT.0) THEN  ! Exoume to idio prosimo kai den uparxei lusi
         PRINT *
         PRINT *,' H synartisi den exei lysi sto arxiko diastima !!!'
         PRINT *,' Den mporoume na vroume lusi. STOP the program'
         GOTO 999
      endif
C======================================================================
C Elegxos wste to thetiko tmima tis synartisis brisketai sto X+DX
c======================================================================
      IF (FXL .LT. 0.) THEN
         ROOT = XL
         DX = XR - XL
      ELSE
         ROOT = XR
         DX = XL - XR
      ENDIF
c=============================
c Kurio tmima tis methodou
c=============================
 10   NITER = NITER + 1
      DX    = 0.5 * DX              ! Neo euros diastimatos
      X_MID = ROOT + DX             ! Meso tou neou diastimatos
      F_MID = FUNC(X_MID) 
      IF (F_MID .LE. 0.) ROOT = X_MID ! Einai arnitiki opote antikatestise to 
                                      ! to orio toy diastimatos sto opoio i 
                                      ! sunartisi einai arnitiki
C===================================================================
C Se geniki periptvsi, to diastima (DIST) mporei na einai arnitiko!
C Ayto tha sumvei otan i sunartisi einai thetiki sto X_LOW kai 
c arnitiki sto X_UP opote tha xreiastei na kinoumaste apo to X_UP
C Xreiazetai epomenvs na eksetasoume tin apoluti timi 
C====================================================================
      IF ((ABS(DX/X_MID).LT.TOL).OR.(F_MID.EQ.0.)) GOTO 100
C
C
      GOTO 10

 100  CONTINUE
      WRITE(6,3)ROOT
 3    FORMAT(1x,'H riza tis eksisvsis einai',1x,E17.9)
      PRINT *, 'Arithmos epanipsevn pou xreiastikan: ',NITER
 999  CONTINUE
  
      end

c===========================================
      Double Precision Function FUNC(X)
c===========================================
c H synartisi F
c===========================================
      implicit none
      double precision x

      func = cos(x)-x
      return
      end

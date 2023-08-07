       program seira_groupb
       implicit none
       REAL    X, Xmin, Xmax, Dx
       REAL    EPSILON, S
       REAL    NATURAL
       
       
       PRINT *, ' Dwste tin akribeia'
       READ *, EPSILON
       PRINT *, ' Poia ta oria tou diastimatos gia upologismo [Xmin/Xmax]'
       READ *, Xmin, Xmax
       PRINT *, ' Ana poses times na eksetastoun'
       READ *, Dx
       X = Xmin
 2     S = natural(X,EPSILON)
       WRITE(6,20) X, S
       X = X + Dx
       if (X .LE. Xmax) goto 2
 20    Format(1x,'Gia x =',1x,f3.1,3x,' S =',1x,f8.6)

       END
c=====================================
       REAL FUNCTION NATURAL(Z,PRC)
c=====================================
       IMPLICIT NONE
       INTEGER N
       REAL    Z, Zo, PRC
       REAL    SUM

       
       SUM = 0.
       N   =  1
 2     Zo  = (Z/N)**N
       IF (ABS(Zo) .GT. PREC) THEN      ! Zo einai panta o epomenos oros.
                                        ! Epomenws xreiazetai na eksetasoume 
                                        ! an einai mikroteros apo tin akriveia
          SUM = SUM + Zo                ! SUM(N+1)-SUM(N) = Zo
          N   = N + 1
          GOTO 2
       ENDIF
c       
       NATURAL = SUM
c
       RETURN
       END
      
          
       

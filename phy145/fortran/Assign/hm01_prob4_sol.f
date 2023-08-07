c=====================================
      program roots
c=====================================
c Ypologismos pragmatikis rizas 
c enos polionumou 3ou bathmou
c   x^3 + ax^2 + bx + c = 0
c
c  H riza x0 = A + B - a/3
c  opou
c      A = (-q/2 + sqrt(R))^(1/3)
c      B = (-q/2 + sqrt(R))^(1/3)
c      R = p^3/27 + q^2/4
c      p = -a^2/3 + b
c      q = 2*a^3/27 - a*b/3 + c
c=====================================
      IMPLICIT NONE
      REAL A, B, C
      REAL R, P, Q
      REAL AA, BB
      REAL SQRT_R, HALF_Q
      REAL SIGN_AA, SIGN_BB
      REAL X0

      PRINT *, 'Dwste tin stathera a tou x^2'
      read *, A
      PRINT *, 'A = ',A
c
      PRINT *, 'Dwste tin stathera b tou x'
      read *, B
      PRINT *, 'B = ',B
c      
      PRINT *, 'Dwste tin stathera c'
      read *, C
      PRINT *, 'C = ',C
c
      P = -A**2/3.0 + B
      Q = 2.*A**3/27.0 - (A*B)/3.0 + C
      R = P**3/27.0 + Q**2/4.0
      SQRT_R = SQRT(MAX(0.,R))      ! Apofeugoume riza arnitiki
                                    ! Xrisimopoioyme ti metabliti SQRT_R
                                    ! giati i posotita emfanizetai 2 fores
                                    ! mia sto A kai mia sto B opote etsi 
                                    ! kanoume ton ypologismo 1 fora mono
      HALF_Q = -Q/2.0               ! Opws kai gia SQRT_R
c
      AA = HALF_Q + SQRT(R)
      BB = HALF_Q - SQRT(R)
c===============================================
c Edw einai to duskolo toy programmatos
c An AA i BB einai arnitika tote o H/Y 
c den mporei na ypologisei ti kybiki riza.
c Kseroume omws oti i kybiki riza enos 
c arnitikou arithmou yparxei kai einai isi
c me to arnitiko tis thetikis timis. 
c Epomenws xreiazetai na broume to prosimo
c tis yporizis posotitas kai meta na paroyme
c tin riza tis apolutis timis kai na 
c pollaplasiasoume me to prosimo. 
c Yparxei synartisi sti FORTRAN poy dinei 
c to prosimo (i SIGN(1.,x) dinei sto 1 to 
c prosimo tou x) alla mporoume na to 
c ypologisoyme kai diaforetika: sign_aa = x/|x|
c================================================
      SIGN_AA = AA/ABS(AA)          ! Exoume to prosimo tou AA
                                    ! Edw kapoios mporei na pei oti an AA=0
                                    ! exoyme diairesi 0/0 enw i synartisi 
                                    ! tis FORTRAN sign dinei + an x=0 
                                    ! Xvris ti xrisi IF den mporoume na 
                                    ! kseperasoyme to problima ayto
c
      AA = ABS(AA)**(1.0/3.0)       ! Prosoxi ston ektheti 1/3 = 0 
                                    ! enw 1./3. dinei to svsto apotelesma
                                    ! episis xreiazetai parenthesi diaforetika
                                    ! ypswnei stin 1 kai diairei to apotelesma
                                    ! me 3.  Diladi an AA=9 tote to apotelesma
                                    ! einai 3 anti gia 2.08 
c
      AA = SIGN_AA * AA             ! i kybiki riza tou AA
c
      SIGN_BB = BB/ABS(BB)       
      BB = ABS(BB)**(1.0/3.0)
      BB = SIGN_BB * BB

      X0 = AA + BB - A/3.

      PRINT *,'===================================================='
      PRINT *,' H pragmatiki riza tou poluwnimou einai x0=',X0
      PRINT *,'===================================================='
      END

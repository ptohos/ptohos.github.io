c===============================================
      program disect
c===============================================
c Programma gia upologismo tou akeraiou kai 
c dekadikou merous enos dedomenoi pragmatikou
c thetikou arithmou
c
c Yparxoun 2 tropoi gia na to kanoume
c Eite xrisimopoiontas ti sunartisi tis 
c bibliothikis tis Fortran (INT(x) opoy x noumero)
c i me to na uesoume ton REAL ariumo se 
c ena INTEGER prokalvntas ti metatropi tou
c eisagvmenou arithmoi apo REAL se INTEGER
c============================================== 
c Input arguments:
c     X: the number to be disected 
c Output arguments:
c     INTPART: integer part
c     RADPART: radical part
c==============================================
      REAL X, RADPART
      INTEGER INTPART
c
c READ now the number
c==============================================
      write(6,*) 'Give a positive number X:'
      read(5,*) X
c      
c-Estimate the two parts using the integer assignment
c======================================================
      INTPART = X          ! Assignment of real to an integer variable
      RADPART = X-INTPART  ! Subtraction of integer part from the number
c
      write(6,*) ' The number X = ',X, 'has'
      write(6,*) ' Integer part = ', INTPART ' and radical = ',RADPART
c      
c-Estimate the two parts using the INT function
c==============================================
      INTPART = INT(X)     ! Get the INT part of the number
      RADPART = X-INTPART  ! Subtraction of integer part from the number
c
      write(6,*) ' The number X = ',X, 'has'
      write(6,*) ' Integer part = ', INTPART ' and radical = ',RADPART
c

      stop
      end

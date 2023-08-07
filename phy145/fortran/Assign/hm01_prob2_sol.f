c===============================================
      program quadratic
c===============================================
c A program to calculate the roots of 
c a quadratic equation ax^2+bx+c=0
c At this introductory stage we assume
c that the solution exists all the time.
c (We didn't know of the IF statements).
c The roots are given by the known formula
c (-b+-sqrt(b^2-4ac))/(2a)
c We will not check whether the discriminant
c is positive or negative. We'll do this later
c=============================================== 
c Input arguments:
c     A: the coefficient of x**2 
c     B: the coefficient of x
c     C: the constant
c Output arguments:
c     x1: root 1
c     x2: root 2
c==============================================
      REAL A, B, C
      REAL X1, X2
      REAL ROOT, DEV
c
c READ now the coefficients
c==============================================
      write(6,*) 'Give the coefficient A:'
      read(5,*) A
      write(6,*) 'Give the coefficient B:'
      read(5,*) B
      write(6,*) 'Give the coefficient C:'
      read(5,*) C
c      
c-Estimate the determinant so we don't carry it around
c======================================================
      root = b**2 - 4.*a*c
      dev  = 2.*a
c
c-Here we may run into troubles if root<0! 
c The computer will abort if it happens 
c But by now we all know how to handle it
c======================================================
      x1 = (-b+sqrt(root))/dev
      x2 = (-b-sqrt(root))/dev
      write(6,*) ' root(+) =',x1, ' root(-) =',x2
      stop
      end

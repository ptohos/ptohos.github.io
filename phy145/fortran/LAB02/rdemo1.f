      PROGRAM RDEMO
C This program reads an integer, prints it out as an INTEGER, converts it into
C a real number, and prints it out as a REAL
C
      IMPLICIT NONE
      REAL X
      INTEGER I
      
      PRINT *,'Please enter an integer: '
 
      READ *, I
      PRINT *,'The number you entered (as an INTEGER) was: ', I

      X = I
      PRINT *,'The number you entered (as a REAL) was: ', X
      
      END

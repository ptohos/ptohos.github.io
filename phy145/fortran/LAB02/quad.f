      PROGRAM quad
************************************************************************
* Program to solve a quadratic equation using the quadratic formula.   *
* Variables used are:                                                  *
*     A, B, C      : the coefficients of the quadratic equation        *
*     DISC         : the discriminant, B ** 2 - 4 * A * C              *
*     ROOT1, ROOT2 : the two roots of the equation                     *
*                                                                      *
* Input:  The coefficients A, B, and C                                 *
* Output: The two roots of the equation                                *
************************************************************************

      REAL A, B, C, DISC, ROOT1, ROOT2

      PRINT *, 'ENTER THE COEFFICIENTS OF THE QUADRATIC EQUATION'
      READ *, A, B, C
      
      DISC = B ** 2 - 4.0 * A * C
	  DISC = SQRT(DISC)
	  
      ROOT1 = (-B + DISC) / (2.0 * A)
      ROOT2 = (-B - DISC) / (2.0 * A)
      PRINT *, 'THE ROOTS ARE', ROOT1, ROOT2

      END


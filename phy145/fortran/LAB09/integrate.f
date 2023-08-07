c======================================================================
	PROGRAM Integration
c======================================================================
C To programma einai grammeno perissotero gia na deiksei ta 
c diafora vimata pu xrisimopoioyntai apo tis methodous 
c oloklirwsis kai den exei beltistopoiithei gia taxytita
c======================================================================
	IMPLICIT NONE
	DOUBLE PRECISION x0,x1,Value,Exact,pi
	INTEGER i,j,nx
C=====  Functions
	DOUBLE PRECISION TrapeziumRule
	DOUBLE PRECISION MidpointRule
	DOUBLE PRECISION SimpsonsRule
	DOUBLE PRECISION GaussQuad
C=====  Constants
	pi = 2.0*ASIN(1.0D0)
	Exact = 2.0
C=====  Limits
	x0 = 0.0
	x1 = pi
C=======================================================================
C       = Trapezium rule =
C=======================================================================
	WRITE(6,*)
	PRINT *,' Trapezium rule'
	nx = 1
	DO i = 1, 20
	   Value =	 TrapeziumRule(x0,x1,nx)
	   WRITE(6,*)nx,Value,Value - Exact
	   nx = 2*nx
	ENDDO
C=======================================================================
C       = Midpoint rule =
C=======================================================================
	WRITE(6,*)
	PRINT*, ' Midpoint rule'
	nx = 1
	DO i = 1, 20
	   Value = MidpointRule(x0,x1,nx)
	   WRITE(6,*)nx,Value,Value - Exact
	   nx = 2*nx
	ENDDO
C=======================================================================
C       = Simpson's rule =
C=======================================================================
	WRITE(6,*)
	PRINT *,' Simpson''s rule'
	WRITE(6,*)
	nx = 2
	DO i = 1, 10
	   Value = SimpsonsRule(x0,x1,nx)
	   WRITE(6,*)nx,Value,Value - Exact
	   nx = 2*nx
	ENDDO
C=======================================================================
C       = Gauss Quadrature =
C=======================================================================
	WRITE(6,*)
	PRINT *,' Gauss quadrature'
	nx = 1
	DO i = 1, 10
	   Value = GaussQuad(x0,x1,nx)
	   WRITE(6,*)nx,Value,Value - Exact
	   nx = 2*nx
	ENDDO
	END
c=======================================================================
	DOUBLE PRECISION FUNCTION F(x)
c=======================================================================
C       Ayti einai i synartisi pros oloklirwsi
c       f(x) = sin(x)
c=======================================================================
	IMPLICIT NONE
	DOUBLE PRECISION x
	F = SIN(x)
	RETURN
	END
c=======================================================================
	DOUBLE PRECISION FUNCTION TrapeziumRule(x0,x1,nx)
c=======================================================================
	IMPLICIT NONE
	INTEGER nx
	DOUBLE PRECISION x0,x1
C=====  functions
	DOUBLE PRECISION F
C=====  local variables
        INTEGER i
        DOUBLE PRECISION dx,xa,xb,fa,fb,Sum
c       
	dx = (x1 - x0)/DFLOAT(nx)
	Sum = 0.0
	DO i = 0, nx-1
	   xa = x0 + DFLOAT(i)*dx
	   xb = x0 + DFLOAT(i+1)*dx
	   fa = f(xa)
	   fb = f(xb)
	   Sum = Sum + fa + fb
	ENDDO
	Sum = Sum * dx / 2.0
	TrapeziumRule = Sum
	RETURN
	END
c======================================================================
	DOUBLE PRECISION FUNCTION MidpointRule(x0,x1,nx)
c======================================================================
	IMPLICIT NONE
	INTEGER nx
	DOUBLE PRECISION x0,x1
C=====  functions
	DOUBLE PRECISION F
C=====  local variables
        INTEGER i
	DOUBLE PRECISION dx,xa,fa,Sum
	dx = (x1 - x0)/Dfloat(nx)
	Sum = 0.0
	DO i = 0, nx-1
	   xa = x0 + (DFLOAT(i)+0.5)*dx
	   fa = f(xa)
	   Sum = Sum + fa
	ENDDO
	Sum = Sum * dx
	MidpointRule = Sum
	RETURN
	END
c======================================================================
	DOUBLE PRECISION FUNCTION SimpsonsRule(x0,x1,nx)
C======================================================================
	IMPLICIT NONE
	INTEGER nx
	DOUBLE PRECISION x0,x1
C=====  functions
	DOUBLE PRECISION F
C=====  local variables
	INTEGER i
	DOUBLE PRECISION dx,xa,xb,xc,fa,fb,fc,Sum
	
	dx = (x1 - x0)/DFLOAT(nx)
	Sum = 0.0
	DO i = 0, nx-1, 2
	   xa = x0 + DFLOAT(i)*dx
	   xb = x0 + DFLOAT(i+1)*dx
	   xc = x0 + DFLOAT(i+2)*dx
	   fa = f(xa)
	   fb = f(xb)
	   fc = f(xc)
	   Sum = Sum + fa + 4.0*fb + fc
        ENDDO
	Sum = Sum * dx / 3.0
	SimpsonsRule = Sum
	RETURN
	END
c========================================================================
	DOUBLE PRECISION FUNCTION GaussQuad(x0,x1,nx)
C========================================================================
	IMPLICIT NONE
	INTEGER nx
	DOUBLE PRECISION x0,x1
C=====  functions
	DOUBLE PRECISION F
C=====  local variables
	INTEGER i
	DOUBLE PRECISION dx,xa,xb,fa,fb,Sum,dxl,dxr
	
	dx = (x1 - x0)/DFLOAT(nx)
	dxl = dx*(0.5D0 - SQRT(3.0D0)/6.0D0)
	dxr = dx*(0.5D0 + SQRT(3.0D0)/6.0D0)
	Sum = 0.0
	DO i = 0, nx-1
	   xa = x0 + DFLOAT(i)*dx + dxl
	   xb = x0 + DFLOAT(i)*dx + dxr
	   fa = f(xa)
	   fb = f(xb)
	   Sum = Sum + fa + fb
	ENDDO
	Sum = Sum * dx / 2.0
	GaussQuad = Sum
	RETURN
	END
	

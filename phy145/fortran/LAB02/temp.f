	  program temp	  
************************************************************************
* Program to convert a temperature of DEGC degrees                     *
* on the Celsius scale to the corresponding                            *
* temperature  DEGF on the Fahrenheit scale.                           *
*                                                                      * 
* Input:  a tempature in degrees Celsius                               *
* Output:  a tempature in degrees Fahrenheit                           *
************************************************************************
	  REAL DEGC, DEGF	  
          print *, 'Enter temperature in degrees celsius'
	  read *,DEGC	  
          DEGF = (9.0/5.0) * DEGC + 32.0
	  print *, 'Fahrenheit temperature is', DEGF
	  end
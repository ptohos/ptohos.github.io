	program constvar
*-------------------------------------------------------------------
* To programma ayto deixnei tin xrisi metablitwn kai statherwn stin 
* Fortran 77 xrisimopoiontas aples entoles eisodou eksodou
*-------------------------------------------------------------------
* Prwta, orizoume ena set metablitwn. H entoli "implicit none" 
* anagkazei mas anagkazei na orisoume tis metablites.
*-------------------------------------------------------------------
	implicit none
	integer i, j, k
      real    x, y, z
      character s*10, t*20
	integer index1, index2, index3
	real time, velocity, acceleration
	character line1*30
*-------------------------------------------------------------------
* Katopin, zitame kapoies times gia tis metavlites aytes.
*-------------------------------------------------------------------
	print*,"Dwste mia timi gia tin akeraia metabliti I = "
	read *, I
	print*,"Dwste mia timi gia tin akeraia metabliti J = "
	read *, J
	print*,"Dwste mia timi gia tin akeraia metabliti K = "
	read *, K
	print*,"Dwste mia timi gia tin pragmatiki metabliti X = "
	read *, X
	print*,"Dwste mia timi gia tin pragmatiki metabliti Y = "
	read *, Y
	print*,"Dwste mia timi gia tin pragmatiki metabliti Z = "
	read *, Z
	print*,"Dwste mia timi gia tin metavliti xaraktirwn S (10 xaraktires max) = "
	read *, S
	print*,"Dwste mia timi gia tin metabliti xaraktirwn T (20 xaraktires max) = "
	read *, T
*-------------------------------------------------------------------
* Telos typwnoyme tis times twn metablitwn xrisimopoiwntas ton 
* tropo ektypwsis poy exei i Fortran 77
*-------------------------------------------------------------------
      print*
      print*,"Ayto einai to apotelesma tis ektypwsis:"
	print*,"======================================="
	print*,"Dwsate treis akeraies metablites me times:"
	print*,"I = ",i,", J = ",j,", kai K = ",k
	print*,"Dwsate episis kai treis pragmatikes metablites me times:"
	print*,"X = ",x,", Y = ",y,", kai Z = ",z
	print*,"Telos orisate duo metablites xaraktirwn me times:"
	print*,"S = ",s,", T = ",t
*----------------------------------------------------------------------
* Twra, tha kanoume merikoys ypologismoys xrisimopoiontas anathesi (=)
*----------------------------------------------------------------------
	index1 = 2*i
	index2 = 3*i-4*j
	index3 = 5*i-3*j+4*k
	time   = x**2
	velocity = (x+y)/2.0
	acceleration = 5*(x*y + y*z)
	line1 = s//t                 ! Prosthesi metavlitwn xaraktira ginetai me to //
*------------------------------------------------------------------
* Twra tha typwsoyme ta apotelesmata twn parapanw entolwn anathesis
*------------------------------------------------------------------
	print*
	print*,"Perissotera apotelesmata"
	print*,"========================"
	print*,"Oi times twn metablitwn index1, index2, index3:"
	print*,index1,"   ",index2,"   ",index3
      print*
	print*,"Enw oi times twn metablitwn time, velocity, kai acceleration einai:"
	print*,time,"   ",velocity,"   ",acceleration
      print*
	print*,"Telos i metabliti xaraktirwn line1 exei timi:"
	print*,line1
*------------------------------------------------------------------
        end
*------------------------------------------------------------------


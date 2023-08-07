#include<stdio>

int main()
{
 int number; /* input number */
 int temp1; /* first temporary integer */
 int temp2; /* second temporary integer */
 int firstDigit; /* first digit of input */
 int secondDigit; /* second digit of input */
 int fourthDigit; /* fourth digit of input */
 int fifthDigit; /* fifth digit of input */

 printf( "Enter a five-digit number: " ); /* get number */
 scanf( "%d", &number );

 temp1 = number;

 /* determine first digit by integer division by 10000 */
 firstDigit = temp1 / 10000;
 temp2 = temp1 % 10000;

 /* determine second digit by integer division by 1000 */
 secondDigit = temp2 / 1000;
 temp1 = temp2 % 1000;

 temp2 = temp1 % 100;

 /* determine fourth digit by integer division by 10 */
 fourthDigit = temp2 / 10;
 temp1 = temp2 % 10;

 fifthDigit = temp1;

 /* if first and fifth digits are equal */
 if (firstDigit == fifthDigit ) {

 /* if second and fourth digits are equal */
 if ( secondDigit == fourthDigit ) {

 /* number is a palindrome */
 printf( "%d is a palindrome\n", number );
 } /* end if */
 else { /* number is not a palindrome */
 printf( "%d is not a palindrome\n", number );
 } /* end else */

 } /* end if */
 else { /* number is not a palindrome */
 printf( "%d is not a palindrome\n", number );
 } /* end else */

 return 0; /* indicate successful termination */

 } /* end main *

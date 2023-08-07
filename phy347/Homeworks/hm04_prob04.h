#ifndef Final_prob01
#define Final_prob01
#endif

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
using namespace std;

class Rectangle {
public:
  Rectangle( double *, double *, double *, double * );
  void setCoord( double *, double *, double *, double * );
  void perimeter( void );
  void area( void );
  void square( void );
  bool isValid( void ) { return valid; }
  void setValid( bool v ) { valid = v; }
private:
  double point1[ 2 ];
  double point2[ 2 ];
  double point3[ 2 ];
  double point4[ 2 ];
  bool valid;
};

// Definition of member functions 

Rectangle::Rectangle( double *a, double *b, double *c, double *d )
{
  setCoord( a, b, c, d );
}

void Rectangle::setCoord( double *p1, double *p2,
			  double *p3, double *p4 ) {
 // Arrangement of points
 // p4.........p3
 // . .
 // . .
 // p1.........p2

 const int x = 0, y = 1; // added for clarity

 // validate all points
 point1[ x ] = ( p1[ x ] > 20.0 || p1[ x ] < 0.0 )? 0.0 : p1[ x ];
 point1[ y ] = ( p1[ y ] > 20.0 || p1[ y ] < 0.0 )? 0.0 : p1[ y ];
 point2[ x ] = ( p2[ x ] > 20.0 || p2[ x ] < 0.0 )? 0.0 : p2[ x ];
 point2[ y ] = ( p2[ y ] > 20.0 || p2[ y ] < 0.0 )? 0.0 : p2[ y ];
 point3[ x ] = ( p3[ x ] > 20.0 || p3[ x ] < 0.0 )? 0.0 : p3[ x ];
 point3[ y ] = ( p3[ y ] > 20.0 || p3[ y ] < 0.0 )? 0.0 : p3[ y ];
 point4[ x ] = ( p4[ x ] > 20.0 || p4[ x ] < 0.0 )? 0.0 : p4[ x ];
 point4[ y ] = ( p4[ y ] > 20.0 || p4[ y ] < 0.0 )? 0.0 : p4[ y ];
 
 // verify that points form a rectangle
 if (point1[ y ] == point2[ y ] && point1[ x ] == point4[ x ] &&
     point2[ x ] == point3[ x ] && point3[ y ] == point4[ y ]) {

   perimeter();
   area();
   square();
   setValid( true ); // valid set of points
 }
 else {
   cout << "Coordinates do not form a rectangle!\n";
   setValid( false ); // invalid set of points
 }
}

void Rectangle::perimeter( void ) {
  double l = fabs( point4[ 1 ] - point1[ 1 ] ),
    w = fabs( point2[ 0 ] - point1[ 0 ] );
  
  cout << setiosflags( ios::fixed | ios::showpoint )
       << "length = " << setprecision( 1 ) << ( l > w ? l : w )
       << "\twidth = " << ( l > w ? w : l )
       << "\nThe perimeter is: " << 2 * ( w + l ) << '\n'
       << resetiosflags( ios::fixed | ios::showpoint );
}

void Rectangle::area( void ) {
  double l = fabs( point4[ 1 ] - point1[ 1 ] ),
    w = fabs( point2[ 0 ] - point1[ 0 ] );
  
  cout << setiosflags( ios::fixed | ios::showpoint )
       << "The area is: " << setprecision( 1 ) << w * l
       << resetiosflags( ios::fixed | ios::showpoint ) << "\n\n";
}

void Rectangle::square( void ) {
  const int x = 0, y = 1; // added for clarity
  
  if ( fabs( point4[ y ] - point1[ y ] ) ==
       fabs( point2[ x ] - point1[ x ] ) )
    
    cout << "The rectangle is a square.\n\n";
}


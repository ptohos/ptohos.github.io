/*Programma to opoio deixnei pws pernoyn orismata se synartisi.
  Pass by value, Pass by reference, Pass by address.
*/
 
#include  <iostream>
using namespace std;
 
void swapByValue( int a , int b  );
void swapByRef  ( int &a, int &b );
void swapByAdr  ( int *a, int *b );
 
int main()
{
    int x = 10;
    int y = 20;
 
    cout << endl;
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    swapByValue( x , y  ); /*H allagi den fainetai stin kalousa sunartisi*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl; 
 
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    swapByRef( x , y  );  /*H allagi fainetai stin kalousa sunartisi alla den katalamvanei mnimi*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl; 
 
    x = 50;
    y = 100;
 
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    swapByAdr( &x , &y  ); /*H allagi fainetai stin kalousa sunartisi kai klatalamvanei xwro sto mnimi*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl;  
 
    return 0;
}
 
void swapByValue( int a , int b  )
{
    int c;
     
    c = a;
    a = b;
    b = c;
}
 
void swapByRef( int &a , int &b  )
{
    int c;
     
    c = a;
    a = b;
    b = c;
}
 
void swapByAdr( int *a , int *b  )
{
    int c;
     
     c = *a;
    *a = *b;
    *b =  c;
}

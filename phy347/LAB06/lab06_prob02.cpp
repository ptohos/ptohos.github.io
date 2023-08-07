#include <iostream>  
#include <string>  
#include <cstdio>

using namespace std;

class complex {  
public:  
  
  complex();
  complex(double,double); 
  void read();
  void display();
  complex operator+(complex a2);
  complex operator-(complex a2);
  complex operator*(complex a2);
  complex operator/(complex a2);
private:
  int imag;
  int real;  
}; 

complex::complex()
{
  real=0;
  imag=0;
}  //Default constructor

complex::complex( double, double){
  real=0;
  imag=0;
}

void complex::read()  
{  
  cout<<"\nEnter Real Part:";  
  cin>>real;  
  cout<<"Enter Imaginary Part:";  
  cin>>imag;  
}  

void complex::display()  
{  
  cout<<"\n= "<<real<<"+"<<imag<<"i";  
}  

complex complex::operator+(complex a2)  
{  
  complex a;  
  a.real=real+a2.real;  
  a.imag=imag+a2.imag;  
  return a;  
}  

complex complex::operator-(complex a2)  
{  
  complex a;  
  a.real=real - a2.real;  
  a.imag=imag - a2.imag;  
  return a;  
}  

complex complex::operator*(complex a2)  
{  
  complex a;  
  a.real=(real*a2.real)-(imag*a2.imag);  
  a.imag=(real*a2.imag)+(imag*a2.real);  
  return a;  
}  

complex complex::operator/(complex a2)  
{  
  complex a;  
  a.real=((real*a2.real)+(imag*a2.imag))/((a2.real*a2.real)+(a2.imag*a2.imag));  
  a.imag=((imag*a2.real)-(real*a2.imag))/((a2.real*a2.real)+(a2.imag*a2.imag));  
  return a;  
} 

 
int main()  
{  
  int ch;  
  complex a,b,c;  
  do  
    {  
      cout<<"\n1.Addition 2.Substraction";  
      cout<<" 3.Mulitplication 4.Division 5.Exit\n";  
      cout<<"\nEnter the choice :";  
      cin>>ch;  
      switch(ch)  
	{  
	case 1:  
	  cout<<"\nEnter The First Complex Number:";  
	  a.read();  
	  a.display();  
	  cout<<"\nEnter The Second Complex Number:";  
	  b.read();  
	  b.display();  
	  c=a+b;  
	  c.display();  
	  break;  
	case 2:  
	  cout<<"\nEnter The First Complex Number:";  
	  a.read();  
	  a.display();  
	  cout<<"\nEnter The Second Complex Number:";  
	  b.read();  
	  b.display();  
	  c=b-a;  
	  c.display();  
	  break;  
	case 3:  
	  cout<<"\nEnter The First Complex Number:";  
	  a.read();  
	  a.display();  
	  cout<<"\nEnter The Second Complex Number:";  
	  b.read();  
	  b.display();  
	  c=a*b;  
	  c.display();  
	  break;  
	case 4:  
	  cout<<"\nEnter The First Complex Number:";  
	  a.read();  
	  a.display();  
	  cout<<"\nEnter The Second Complex Number:";  
	  b.read();  
	  b.display();  
	  c=a/b;  
	  c.display();  
	  break;  
	}  
    }while(ch!=5);  
  return 0; 
}  

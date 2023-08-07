#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

double Factorial(int);
double Legendre(double);
double NewtonRaphson(double, double, double);

int main()
{
  double x, dx;
  double xmin, xmax, eps;
  double x1, x2;

  cout<<"Give the initial value of x\n";
  cin >> xmin;
  cout<<"Give the max value of x\n";
  cin >> xmax;
  cout<<"Give the step size\n";
  cin >> dx;
  cout<<"Give the precision\n";
  cin >> eps;
  //==================================================
  // Anoigma 2 arxeiwn gia apothikeusi apotelesmatwn
  //==================================================
  ofstream file1, file2;
  //ifstream infile;
  file1.open("Legendre.dat");
  file2.open("LegendreRoots.dat");
  
  int nsteps = (xmax - xmin)/dx;
  for(int i=0; i <= nsteps; i++)
    {
      x = xmin + i*dx;
      file1 << fixed << setw(6) << setprecision(3)<< x
	    << fixed << setw(10) << setprecision(4) << Legendre(x) << endl;
      x += dx;
    }
   file1.close();
      
 // Open the file again to read the values
   ifstream infile("Legendre.dat");
   string line;
   getline(infile,line);
   x1 = stod(line);      //metatropi twn xaraktirwn se double 
   while(1) {
     getline(infile,line);
     x2 = stod(line);
     // Ypologismos rizas mono an allazei prosimo i sunartisi
     if (Legendre(x1)*Legendre(x2) < 0) {
       file2 << fixed << setw(12) << setprecision(8)<<NewtonRaphson(x1,x2,eps) << endl; 
     }
     if (x1 > 0) break;
     x1 = x2;
   }
   infile.close();
   file2.close();
} 


double Factorial(int n){                           
  if(n==0) {return 1;}
  else {return n*Factorial(n-1);}
}

double Legendre(double x){
  double L=8, A, Beta, pol=0, r=0;
  A=1/pow(2,L);
  for(int r=0; r<=L/2; r++){
    Beta = Factorial(2*(L-r))/(Factorial(r)*Factorial(L-r)*Factorial(L-2*r));
    pol+=pow(-1,r) * pow(x,L-2*r) * Beta;
  }
  return pol*A;
}


double NewtonRaphson(double x1, double x2, double eps){
  double deriv, xx3;
  double xx1 = x1;
  double xx2 = x2;
  while(1){
    deriv = (xx1 - xx2)/(Legendre(xx1) - Legendre(xx2));
    xx3 = xx1 - Legendre(xx1)*deriv;
    xx1 = xx2;
    xx2 = xx3;
    if (abs(Legendre(xx3)) > eps && abs(xx2 - xx1) > eps) break;
  }
  return xx3;
}

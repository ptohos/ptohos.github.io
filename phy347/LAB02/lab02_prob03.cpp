//==========================
// Newton-Raphson method for finding roots 
//     4*x = cos(x)
//==========================
#include <iostream>
#include <cmath>
using namespace std;

#define N 100 // max number of iterations
double func(double x);
double deriv(double x);

int main()
{
   double p, pnew, f, dfdx, tol;
   cout << "What is the tolerance?" << endl;
   cin >> tol;
   cout << "Enter starting value of x:" << endl;
   cin >> pnew;

   //main loop
   for (int i = 0; i< N; i++){
    p = pnew;   //anathesi tis proigoumenis lysis
    // Evaluate the derivative and the function
    f = func(p);      //function to solve
    dfdx = deriv(p);  //paragwgos tis 4x-cos(x)
    pnew = p - f/dfdx;
    if (abs(pnew - p) < tol) { 
      cout << "root is " << pnew << " to within " << tol << "\n"; 
      return 0;
    } // end of if 
  }   // end of loop
   cerr << "Failed to converge after " << N << " iterations." << endl;
  return 1;
}


double func(double x)
{
  double f;
  f = 4*x - cos(x);
  return f;
}

double deriv(double x)
{
  double f;
  f = 4 + sin(x);
  return f;
}

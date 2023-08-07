#include<iostream>
#include<cmath>

using namespace std;
 
// Use as a function 4x-cos(x)
double func(double x)
{
  return 4*x - cos(x);
}
 
// Derivative of the above function which is 3*x^x - 2*x
double derivFunc(double x)
{
  return 4 + sin(x);
}
 
// Function to find the root
void newtonRaphson(double x,double epsilon)
{
    double h = func(x) / derivFunc(x);
    while (abs(h) >= epsilon)
    {
        h = func(x)/derivFunc(x);
	x = x - h;  // x(i+1) = x(i) - f(x) / f'(x)  
    }
    cout << "The value of the root is : " << x << "\n";
}
 
// 
int main()
{
  double x0;
  double tol;
  cout << "Give the starting value of x\n";
  cin >> x0;
  cout << "Give the accuracy of the solution\n";
  cin >> tol;
  
  newtonRaphson(x0,tol);
  return 0;
}

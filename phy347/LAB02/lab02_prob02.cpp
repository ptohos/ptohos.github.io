#include <iostream>
using namespace std;

int factorial (int);

int factorial(int n)
{
 int loop = 1;
 int fac ;
 if (n == 0) return 1;
 else return n*factorial(n-1);
}


int main()
{
  int mynumb;
  cout << "Enter an integer number to calculate the factorial" << endl;
  cin >> mynumb;
  if (mynumb < 0) {
    cout << " Factorial of a negative number "<< mynumb << " does not exist\n";
    exit(-1);
  }
  cout << "The factorial of " << mynumb << " is " << factorial(mynumb)<< endl;
}

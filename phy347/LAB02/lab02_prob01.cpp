#include<iostream>
using namespace std;

int main()
{
  int loop, factorial, mynumb;
  factorial = 1;
  cout << "Enter an integer number to calculate the factorial" << endl;
  cin >> mynumb;
  if (mynumb < 0) {
    cout << " Factorial of a negative number "<< mynumb << " does not exist\n";
    exit(-1);
  }
  else {
    for (int loop=mynumb; loop>=1; loop--){
      factorial = factorial * loop;
    }
  }
  cout << "The factorial of "<< mynumb << " is " << factorial << endl;
}

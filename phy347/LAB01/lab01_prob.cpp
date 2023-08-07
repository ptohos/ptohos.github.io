#include<iostream>

using namespace std;

int main()
{
  int A, B, C;
  int imax1, imax2, imax3;
  int istore;
  
  cout << "Give three integers A/B/C\n";
  cin >> A >> B >> C;
  imax1 = A;     /* Set all ordered numbers to A */
  imax2 = A;
  imax3 = A;

  if (B > imax1) {
    imax1 = B;
  }
  else {
    imax2 = B;   /* if B<A then set the remaining two as B */
    imax3 = B;
  }
  if (C > imax1) {
    istore = imax1;
    imax1 = C;
    imax3 = imax2;
    imax2 = istore;
  }
  else if (C > imax2) {
    istore = imax2;
    imax2 = C;
    imax3 = istore;
  }
  else{
    imax3 = C;
  }
  cout << "The ordered list of numbers is "
       << imax1 << " " << imax2 << " " << imax3 << endl;
}

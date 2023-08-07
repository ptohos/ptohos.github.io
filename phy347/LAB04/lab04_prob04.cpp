/************************
 Eyresi tis pithanotitas 
 ne riksoume ena nomiza 
 6 fores kai na paroume 
 toulaxiston 4 fores tin
 idia opsi
************************/
#include <iostream>
#include <fstream>
#include <iomanip>
#include <ctime>
#include <cmath>
#include <cstdlib>

using namespace std;

double binom(double, int, int);
int factorial(int);

int main() {

  int mxthrows = 6;
  double prob=0.5;
  double rnd;
  srand(time(NULL));

  for (int iloop = 1; iloop < 8; iloop++) {
    int sum = 0;
    int nexp = 0;
    for (int iexp = 0; iexp< pow(10,iloop); iexp++){
      int success = 0;
      nexp++;
      for (int ithrow = 0; ithrow < mxthrows; ithrow++){
	rnd = float(rand())/RAND_MAX;
	if (rnd > prob) success++;
      }
      if (success >=4) sum++;
    }
    printf("%8d \t \t %5.4f\n",nexp,double(sum)/nexp);
  }
  double theory =0;
  for (int i=4; i<=mxthrows; i++)
    theory += binom(prob,i,mxthrows);
  printf(" Theoritiki timi %5.4f\n",theory);
}

int factorial(int n)
{
  if (n <=1 ) return 1;
  else return n*factorial(n-1);
}

double binom(double prob, int nsuccess, int ntries) {
  int nfail = ntries - nsuccess;
  double binocoeff = factorial(ntries)/factorial(nsuccess)/factorial(nfail);
  double value = pow(prob,nsuccess)*pow(prob,nfail);
  return value*binocoeff;
}

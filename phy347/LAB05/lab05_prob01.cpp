/**************************************************
 Eyresi tou olokliromatos tis sunartisis 1/(1+x^2)
 me ti methodo tis mesis timis kai tis deigmatoleipsias
***************************************************/
#include <iostream>
#include <fstream>
#include <iomanip>
#include <ctime>
#include <cmath>
#include <cstdlib>

using namespace std;

double func(double);
double func_maxval(int,double,double);
void mc_midvalue(int, double, double, double &, double &);
void mc_sampling(int,double, double, double &, double &);

int main() {

  double xmin, xmax;
  double Integral, Error;
  srand(time(NULL));

  cout << "Lower x-value" << endl;
  cin >> xmin;
  cout << "Higher x-value" << endl;
  cin >> xmax;

  printf("The exact value of the integral 1/(1+x*x) between 0 and 1 is %7.4f\n",
	 M_PI/4.); 
  printf("  Ntries \t \t Mesi timi \t \t Aporripsis\n");
  for (int itries=1; itries<8; itries++){
    int Ntries = pow(10,itries);
    mc_midvalue(Ntries, xmin, xmax, Integral, Error);
    double temp1 = Integral;
    double temp2 = Error;

    mc_sampling(Ntries, xmin, xmax, Integral, Error);
    printf("%8.d \t  %7.4f +/- %7.4f \t  %7.4f +/- %7.4f\n",
	   Ntries, temp1, temp2, Integral, Error);
  }
}

double func(double x) {
  double value = 1/(1+pow(x,2));
  return value;
}

double func_maxval(int ntries, double xmin, double xmax) {
  double mx = -99999900.;
  for (int i=0; i<ntries; i++) {
    double x = xmin+(xmax-xmin)*double(rand())/RAND_MAX;
    if (func(x) > mx) mx = func(x);
  }
  return mx;
}
 
void  mc_midvalue(int ntries, double xmin, double xmax, 
		  double & integral, double & error) {
  double sum = 0;
  double sumsq = 0;
  double ave;
  double rnd;
  
  for (int itries = 0; itries < ntries; itries++){
    rnd = double(rand())/RAND_MAX;
    double x = xmin + (xmax-xmin)*rnd;
    double fx = func(x);
    sum   += fx;
    sumsq += fx*fx;
  }
  ave = sum/ntries; 
  error = (sumsq/ntries - ave*ave);
  error = sqrt(error/ntries);
  integral = ave;
}


void  mc_sampling(int ntries, double xmin, double xmax, 
		  double & integral, double & error) {
  double sum = 0;
  double sumsq = 0;

  int nunder = 0;
  double rnd;
  double ymax = func_maxval(ntries,xmin,xmax);
  for (int itries = 0; itries < ntries; itries++){
    rnd = double(rand())/RAND_MAX;
    double x = xmin + (xmax-xmin)*rnd;
    double fx = func(x);
    rnd = double(rand())/RAND_MAX;
    double y = ymax * rnd;
    if (y <= fx) nunder++;
  }
  integral = ((xmax-xmin)*nunder)/ntries;
  error = ((xmax-xmin)*sqrt(nunder))/ntries;
}


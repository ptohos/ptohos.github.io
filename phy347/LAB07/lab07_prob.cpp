#include <iostream>
#include <cmath>
#include <TRoot.h>
#include <TFile.h>
#include <TH1D.h>

using namespace std;
TFile* outfil = new TFile("ode.root", "RECREATE");
TH1D* myhist1 = new TH1D("myhist1","histo Euler",101,-0.01,2.01);
TH1D* myhist2 = new TH1D("myhist2","histo Euler-Crommer",101,-0.01,2.01);
TH1D* myhist3 = new TH1D("myhist3","histo RK2",101,-0.01,2.01);
TH1D* myhist4 = new TH1D("myhist4","histo RK4",101,-0.01,2.01);

class ode {
public:
  ode(double to, double xO, double T,      //Constructor
      double (*fderiv) (double, double) ) {
    t_init  = to; 
    x_init  = xO; 
    t_final = T; 
    sfn=fderiv;
  }
  double* euler(int n) const;
  double* eulerpc(int n) const;
  double* rk2(int n) const;
  double* rk4(int n) const;
private:
  double t_init;
  double x_init;
  double t_final;
  double (*sfn) (double t, double x);
};

double* ode::euler(int n) const {  // Euler
  double* x = new double [n + 1];  // orismos metavlitou pinaka
  double h = (t_final - t_init)/n; // step size
  x[0] = x_init;                   // initial value
  for (int k = 0; k < n; k++){
    x[k+1] = x[k] + h*sfn(t_init + k*h, x[k]);
    double time = t_init+h*(k+1);
  }
  return x;                       // H synartisi epistrefei pinaka 
}

double* ode::eulerpc(int n) const {
  double* x = new double [n + 1];
  double h = (t_final - t_init)/n;
  x[0] = x_init;
  for (int k = 0; k < n; k++) {
    x[k+1] =x[k] +h*sfn(t_init + k*h, x[k]) ;      
    x[k+1] =x[k] +h*sfn(t_init +(k+1)*h, x[k+1]);
  }
 return x;
}

double* ode::rk2(int n) const {
  double* x = new double [n + 1];
  double h = (t_final - t_init)/n;
  x[0] = x_init;
  for (int k = 0; k < n; k++) {
    double tp = t_init + k*h;
    double f = h*sfn(tp, x[k]);
    x[k+1] = x[k] + 0.5*(f + h*sfn(tp + h, x[k] + f));
  }
  return x;
}

double* ode::rk4(int n) const {
  double* x = new double [n + 1];
  double h = (t_final - t_init)/n;
  double hh = h/2.;
  x[0] = x_init;
  
  for (int k = 0; k < n; k++) {
    double tp = t_init + k*h;
    double xs = x[k];
    double F1 = sfn(tp,xs);
    double F2 = sfn(tp+hh,xs+hh*F1);
    double F3 = sfn(tp+hh,xs+hh*F2);
    double F4 = sfn(tp+h,xs+h*F3);
    x[k+1] = x[k] + (F1+2.0*(F2+F3)+F4)*h/6.0;
  }
  return x;
}

double fderivative(double t, double x) { //derivative function
  return x*(1 - exp(t))/(1 + exp(t));
}

double exact(double t) { // exact solution
  return 12*exp(t)/pow(1 + exp(t) , 2);
}

int main() {
  ode exmp(0 , 3, 2, fderivative);   // x(0) = 3, T = 2
  double* soln1 = exmp.euler(100);    // 100 subintervals
  double* soln2 = exmp.eulerpc(100);
  double* soln3 = exmp.rk2(100);
  double* soln4 = exmp.rk4(100);

  double norm1 = 0;
  double norm2 = 0;
  double norm3 = 0;
  double norm4 = 0;
  double h = 2.0/100;                // grid size
  for (int k = 1; k <= 100; k++){     // compute error
    norm1 = max (norm1 , fabs(exact(k*h) - soln1[k])) ;
    norm2 = max (norm2 , fabs(exact(k*h) - soln2[k])) ;
    norm3 = max (norm3 , fabs(exact(k*h) - soln3[k])) ;
    norm4 = max (norm4 , fabs(exact(k*h) - soln4[k])) ;
    myhist1->Fill(k*h,soln1[k]);
    myhist2->Fill(k*h,soln2[k]);
    myhist3->Fill(k*h,soln3[k]);
    myhist4->Fill(k*h,soln4[k]);
  }
  cout << "Theoritiki lysi: " << exact(100*h) << '\n';
  cout << "Euler lysi: " << soln1[100] << '\n';
  cout << "Euler-Crommer lysi: " << soln2[100] << '\n';
  cout << "Runge-Kutta 2ou bathmou: " << soln3[100] << '\n';
  cout << "Runge-Kutta 4ou bathmou: " << soln4[100] << '\n';
 
  cout << "max norm of error by euler's method = "
       << norm1 << '\n';
  cout << "max norm of error by euler crommer method = "
       << norm2 << '\n';
  cout << "max norm of error by RK2 method = "
       << norm3 << '\n';
  cout << "max norm of error by RK4 method = "
       << norm4 << '\n';
  outfil -> Write();
  outfil -> Close();
}



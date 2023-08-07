#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <TROOT.h>
#include <TFile.h>
#include <TH1D.h>

using namespace std;

class ode {
public:
  ode(double to, double xO, double v0, double T,      //Constructor
      void (*fderiv) (double, double*, double*) ) {
    t_init  = to; 
    x_init  = xO;
    v_init  = v0;
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
  double v_init;
  double t_final;
  void (*sfn) (double t, double *x, double *dxdt);
};

double* ode::euler(int n) const {   // Euler
  static int off  = n+1;
  double *x = new double [2*n];   // orismos metavlitou pinaka
  double h = (t_final - t_init)/n;  // step size
  double *dxdt = new double [2];
  double *xtemp = new double [2];
  x[0]     = x_init;                // initial value
  x[off+0] = v_init;
  double time = t_init;

  for (int k = 0; k < n; k++){
    xtemp[0] = x[k];         // position
    xtemp[1] = x[off+k];     // velocity
    sfn(t_init+k*h, xtemp, dxdt);
    x[k+1] = x[k] + h*dxdt[0];
    x[off+k+1] = x[off+k] + h*dxdt[1];
    time = t_init+h*(k+1);
  }
  delete []xtemp;
  return x;                       // H synartisi epistrefei pinaka 
}

double* ode::eulerpc(int n) const {
  static int off = n+1;
  double *x = new double [2*n];
  double *xtemp = new double [2];
  double *dxdt = new double [2];
  double h = (t_final - t_init)/n;
  x[0]     = x_init;
  x[off+0] = v_init;

  for (int k = 0; k < n; k++) {
    xtemp[0] = x[k];
    xtemp[1] = x[off+k];
    sfn(t_init + k*h, xtemp, dxdt);
    x[k+1]     = x[k];
    x[off+k+1] = x[off+k] + h*dxdt[1];
    xtemp[0]   = x[k+1] ; 
    xtemp[1]   = x[off+k+1];
    sfn(t_init + (k+1)*h, xtemp, dxdt);
    x[k+1]     = x[k] + h*dxdt[0];
    x[off+k+1] = x[off+k+1];
  }
  delete []xtemp;
  return x;
}

double* ode::rk2(int n) const {
  static int off = n+1;
  double *x = new double [2*n];
  double *xtemp = new double [2];
  double *dxdt = new double [2];
  double h = (t_final - t_init)/n;
  x[0] = x_init;
  x[off+0] = v_init;
  double *k1    = new double [2];
  double *k2    = new double [2];
				
  for (int k = 0; k < n; k++) {
    xtemp[0] = x[k];
    xtemp[1] = x[off+k];
    sfn(t_init + k*h, xtemp, dxdt);     // upologismos twn paragwgvn stin arxi
    k1[0] = dxdt[0];
    k1[1] = dxdt[1];
    xtemp[0] = x[k]     + h/2*dxdt[0];  // euler step sto meso toy diastimatos
    xtemp[1] = x[off+k] + h/2*dxdt[1];
    sfn(t_init + (k+0.5)*h, xtemp, dxdt); // upologismos twn paragwgwn sto meso
    k2[0] = dxdt[0];
    k2[1] = dxdt[1];
    x[k+1]     = x[k]     + h * k2[0];
    x[off+k+1] = x[off+k] + h * k2[1];
  }
  delete []xtemp;
  delete []k1;
  delete []k2;
  return x;
}

double* ode::rk4(int n) const {
  static int off   = n+1;
  double *x = new double [2*n];
  double *xtemp = new double [2];
  double *dxdt = new double [2];
  double h = (t_final - t_init)/n;
  double hh = h/2.;
  x[0]     = x_init;
  x[off+0] = v_init;
  double *k1 = new double [2];
  double *k2 = new double [2];
  double *k3 = new double [2];
  double *k4 = new double [2];
  
  for (int k = 0; k < n; k++) {
    double tp = t_init + k*h;
    xtemp[0] = x[k];
    xtemp[1] = x[off+k];
    sfn(tp, xtemp, dxdt);                   //K1
    k1[0] = dxdt[0];
    k1[1] = dxdt[1];
    xtemp[0] = x[k]     + hh*k1[0];
    xtemp[1] = x[off+k] + hh*k1[1];
    sfn(tp+hh, xtemp, dxdt);                //K2
    k2[0] = dxdt[0];
    k2[1] = dxdt[1];
    xtemp[0] = x[k]     + hh*k2[0];
    xtemp[1] = x[off+k] + hh*k2[1];
    sfn(tp+hh, xtemp, dxdt);                //K3
    k3[0] = dxdt[0];
    k3[1] = dxdt[1];
    xtemp[0] = x[k]     + h*k3[0];
    xtemp[1] = x[off+k] + h*k3[1];
    sfn(tp+h, xtemp, dxdt);                 //K4
    k4[0] = dxdt[0];
    k4[1] = dxdt[1];
    
    x[k+1]     = x[k]     + (k1[0]+2.0*(k2[0]+k3[0])+k4[0])*h/6.0;
    x[off+k+1] = x[off+k] + (k1[1]+2.0*(k2[1]+k3[1])+k4[1])*h/6.0;
  }
  return x;
  delete []xtemp;
  delete []k1;
  delete []k2;
  delete []k3;
  delete []k4;
}

void fderivative(double t, double *x, double *dxdt) { //derivative function
  dxdt[0] = x[1];    // derivative of position  dx/dt =  v
  dxdt[1] = -x[0];   // derivatice of velocity  dv/dt = -x
}
/*
void exact(double t, double *x, double *xtheory) { // exact solution
  xtheory[0] = x[0]*cos(t);     // position
  xtheory[1] = -x[1]*sin(t);    // velocity
}
*/
int run_ode() {
  //double hstep = 0.01;
  int maxb     = 10*6300;
  //double Tmax  = maxb*hstep;
  double Tmax  = 10*(2*TMath::Pi());
  double hstep = Tmax/maxb;
  double lowxbin = -hstep/2.;
  double hixbin = Tmax-hstep/2.;

  ode exmp(0 , 1, 0, Tmax, fderivative);   // t0=0, x0=1, v0=0  kai T = 63
  double* soln1 = exmp.euler(maxb);    // 100 subintervals
  
  double* soln2 = exmp.eulerpc(maxb);
  double* soln3 = exmp.rk2(maxb);
  double* soln4 = exmp.rk4(maxb);
  
  double xpos, velo, ene, E0;
  double x0 = 1.;
  double v0 = 0.;
  E0 = 0.5*x0*x0 + 0.5*v0*v0;

 TFile* outfil = new TFile("ode-oscillator.root", "RECREATE");
 TH1D* eulpos = new TH1D("eulpos","Euler - position",maxb,lowxbin,hixbin);
 TH1D* eulvel = new TH1D("eulvel","Euler - velocity",maxb,lowxbin,hixbin);
 TH1D* eulene = new TH1D("eulene","Euler - energy",maxb,lowxbin,hixbin);
 TH1D* eulenedif = new TH1D("eulenedif","Euler - energy diff",maxb,lowxbin,hixbin);

 TH1D* eucpos = new TH1D("eucpos","EulerCromer - position",maxb,lowxbin,hixbin);
 TH1D* eucvel = new TH1D("eucvel","EulerCromer - velocity",maxb,lowxbin,hixbin);
 TH1D* eucene = new TH1D("eucene","EulerCromer - energy",maxb,lowxbin,hixbin);
 TH1D* eucenedif = new TH1D("eucenedif","EulerCromer - energy diff",maxb,lowxbin,hixbin);
 TH1D* rk2pos = new TH1D("rk2pos","RK 2 - position",maxb,lowxbin,hixbin);
 TH1D* rk2vel = new TH1D("rk2vel","RK 2 - velocity",maxb,lowxbin,hixbin);
 TH1D* rk2ene = new TH1D("rk2ene","RK 2 - energy",maxb,lowxbin,hixbin);
 TH1D* rk2enedif = new TH1D("rk2enedif","RK 2 - energy diff",maxb,lowxbin,hixbin);
 TH1D* rk4pos = new TH1D("rk4pos","RK 4 - position",maxb,lowxbin,hixbin);
 TH1D* rk4vel = new TH1D("rk4vel","RK 4 - velocity",maxb,lowxbin,hixbin);
 TH1D* rk4ene = new TH1D("rk4ene","RK 4 - energy",maxb,lowxbin,hixbin);
 TH1D* rk4enedif = new TH1D("rk4enedif","RK 4 - energy diff",maxb,lowxbin,hixbin);

 for (int k = 0; k < maxb; k++){
    xpos = soln1[k];
    velo = soln1[maxb+1+k];
    ene  = 0.5*xpos*xpos + 0.5*velo*velo;
    eulpos->Fill(k*hstep,xpos);
    eulvel->Fill(k*hstep,velo);
    eulene->Fill(k*hstep,ene);
    eulenedif->Fill(k*hstep,ene-E0);
 
    xpos = soln2[k];
    velo = soln2[maxb+1+k];
    ene  = 0.5*xpos*xpos + 0.5*velo*velo;
    eucpos->Fill(k*hstep,xpos);
    eucvel->Fill(k*hstep,velo);
    eucene->Fill(k*hstep,ene);
    eucenedif->Fill(k*hstep,ene-E0);

    xpos = soln3[k];
    velo = soln3[maxb+1+k];
    ene  = 0.5*xpos*xpos + 0.5*velo*velo;
    rk2pos->Fill(k*hstep,xpos);
    rk2vel->Fill(k*hstep,velo);
    rk2ene->Fill(k*hstep,ene);
    rk2enedif->Fill(k*hstep,ene-E0);

    xpos = soln4[k];
    velo = soln4[maxb+1+k];
    ene  = 0.5*xpos*xpos + 0.5*velo*velo;
    rk4pos->Fill(k*hstep,xpos);
    rk4vel->Fill(k*hstep,velo);
    rk4ene->Fill(k*hstep,ene);
    rk4enedif->Fill(k*hstep,ene-E0);
    /*
    cout << setw(15) << setprecision(8) << k*hstep 
	 << setw(15) << setprecision(8) << xpos 
	 << setw(15) << setprecision(8) << velo 
	 << setw(15) << setprecision(8) << ene-E0 <<endl;
    */
}
 TCanvas *c = new TCanvas("c","c", 0, 0,1200,1200);
 c->Divide(2,2);
 c->cd(1);

 eulene->SetMaximum(0.55);
 eulene->SetMinimum(0.45);
 eulene->SetMarkerStyle(24);
 eulene->SetMarkerColor(kBlack);
 eulene->SetMarkerSize(0.5);
 eulenedif->Draw("hist p");

 c->cd(2);
 eucene->SetMarkerStyle(25);
 eucene->SetMarkerColor(kBlue);
 eucene->SetMarkerSize(0.5);
 eucenedif->Draw("hist p");
 
 
 c->cd(3);
 rk2ene->SetMarkerStyle(21);
 rk2ene->SetMarkerColor(kRed);
 rk2ene->SetMarkerSize(0.5);
 rk2enedif->Draw("hist p");

 c->cd(4);
 rk4ene->SetMarkerStyle(20);
 rk4ene->SetMarkerColor(kGreen);
 rk4ene->SetMarkerSize(0.5);
 rk4enedif->Draw("hist p");

 outfil -> Write();
 //outfil -> Close();
 return 0;
}



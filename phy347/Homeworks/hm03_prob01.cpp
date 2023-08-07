#include<iostream>
#include<iomanip>
#include<cmath>
#include "TFile.h"
#include "TH1.h"

using namespace std;

void hm03_prob01(){

  double time, xpos, vel;
  double t0, x0, v0, tmax;
  double dt,K, mass, omega, omegasq;
  double ene, E0;
  printf("\nEnter t0, x0, v0 \n");
  scanf("%lf%lf%lf",&t0,&x0,&v0);
  printf("\nEnter time step, max time (arithmos periodwn), K, mass\n");
  scanf("%lf%lf%lf%lf",&dt,&tmax,&K,&mass);

  omegasq = K/mass;
  omega = K/mass;
  double twopi=2*acos(-1.);
  double period = omega*twopi;
  tmax = period*tmax;
  int ntsteps = (tmax-t0)/dt;
  
  double lowxbin = -dt/2.;
  double hixbin = tmax-dt/2.;
  
  E0 = 0.5*x0*x0 + 0.5*v0*v0;  //Mixaniki Energeia talantwti 
  
  TFile* outfile = new TFile("ode-oscillator.root", "RECREATE");
  TH1D* eulpos = new TH1D("eulpos","Euler - position",ntsteps,lowxbin,hixbin);
  TH1D* eulvel = new TH1D("eulvel","Euler - velocity",ntsteps,lowxbin,hixbin);
  TH1D* eulene = new TH1D("eulene","Euler - energy",ntsteps,lowxbin,hixbin);
  TH1D* eulenedif = new TH1D("eulenedif","Euler - energy diff",ntsteps,lowxbin,hixbin);
  
  time = t0;
  xpos = x0;
  vel = v0;
  for (int k = 0; k < ntsteps; k++){
    double xtheo = x0*cos(k*time);
    double vtheo = v0*sin(k*time);
    double xtemp = xpos;
    double vtemp = vel;
    xpos = xtemp + vtemp * dt;  //Euler step for position. The position at the
                                //beginning of the time step and the deriv=vtemp
                                //at the beginning of the time step
    vel = vtemp + (-xtemp)*dt;  //Paragwgos tis taxititas einai dv/dt = -x

    ene  = 0.5*xpos*xpos + 0.5*vel*vel;
    eulpos->Fill(k*dt,xpos);
    eulvel->Fill(k*dt,vel);
    eulene->Fill(k*dt,ene);
    eulenedif->Fill(k*dt,ene-E0);
  }
 outfile -> Write();
 return 0;
 }



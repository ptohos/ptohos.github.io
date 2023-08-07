/*
  The Problem is:
  Suppose our data obeys the distribution
  R(t) = A + Be^{-Gamma*t} for 0<t<3 sec
  a) For A=1/sec, B=2/sec and Gamma=2/sec, generate fake data 
     using the acceptance-rejection method
  b) Calculate the log-likelihood for these data
  c) Make a 2D plot of -log-likehood for the fake data for the
     variables Gamma and kappa=A/B.  Determine how close
     the minimum is to the true minimum
  d) Plot -2lnL and find the uncertainty on Gamma, assume we know kappa
     exactly
*/
// ----------------------------------------------------------------------------------- //

#define NGRID 100
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#include <TROOT.h>
#include <TH1.h>
#include <TH2.h>
#include <TF1.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TFile.h>
#include <TMath.h>
#include <TRandom3.h>
#include <TGraph.h>
#include <TLatex.h>

// ----------------------------------------------------------------------------------- //
void lifetimeLikelihood(int ntries) {
  // ----------------------------------------------------------------------------------- //

  // Make pretty plots
  gROOT->Reset();
  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  gStyle->SetOptFit(0);
  gStyle->SetPadTickX(1);
  gStyle->SetPadTickY(1);
  gStyle->SetStatBorderSize(1);
  gStyle->SetCanvasColor(0);


  Int_t font=42; // Helvetica
  Double_t tsize=0.05;
  
  gStyle->SetTextFont(font);
  gStyle->SetTextSize(tsize);
  gStyle->SetLabelFont(font,"x");
  gStyle->SetTitleFont(font,"x");
  gStyle->SetLabelFont(font,"y");
  gStyle->SetTitleFont(font,"y");
  gStyle->SetLabelFont(font,"z");
  gStyle->SetTitleFont(font,"z");

  gStyle->SetLabelSize(tsize,"x");
  gStyle->SetTitleSize(tsize,"x");
  gStyle->SetLabelSize(tsize,"y");
  gStyle->SetTitleSize(tsize,"y");
  gStyle->SetLabelSize(tsize,"z");
  gStyle->SetTitleSize(tsize,"z");
  
  // Here is the start of the real code
  
  double A = 1.0;

  double B = 2.0;
  double GammaTrue = 2.0;
  double tmax = 3.0;
  
  vector<double> data;           // Vector of data measurements

  TRandom* random = new TRandom();
  random->SetSeed(123);
  

  TH1D hist("data","Fake Data: Number of Entries vs t",100,0,tmax);
  hist.GetXaxis()->SetTitle("time (sec)");
  hist.GetYaxis()->SetTitle("Number of entries");

  
  // Generate data:
  // ===============
  
  int npass = 0;
  while(npass<ntries) {
    double x = random->Uniform(tmax);
    double y = random->Uniform(A+B);
    if(y<A+B*exp(-GammaTrue*x)) {
      data.push_back(x);
      hist.Fill(x);
      npass++;
    }
  }

  TCanvas c1("c1","c1",600,400);
  hist.Draw();
  c1.Print("LifeTimeLikelihood_plot1.png");

  double kappaTrue=A/B;

  // Analyze the data
  // =================
  // Start by initializing all the variables
  double min_kappa = 0.5*kappaTrue;
  double max_kappa = 1.5*kappaTrue;
  double min_gamma = 1.0;
  double max_gamma = 3.0;

  TH2D h_loglike("LogLikelihood","LogLikelihood",NGRID,min_gamma,max_gamma,
		 NGRID,min_kappa,max_kappa);
  h_loglike.GetXaxis()->SetTitle("Gamma (1/sec)");
  h_loglike.GetYaxis()->SetTitle("Kappa");


  double delta_kappa = (max_kappa-min_kappa)/NGRID;
  double delta_gamma = (max_gamma-min_gamma)/NGRID;
  double min=1.0e20;
  int best_i = -1;
  int best_j = -1;
  double x[NGRID];
  double y[NGRID];

  double likelihoodGrid[NGRID][NGRID];

  // Loop over hypothesis for the value of kappa and calculate log likelihood
  // ---------------------------------------------------------------------
  for (int i=0; i < NGRID; i++) {
    double gamma = min_gamma + double(i)*delta_gamma;
    for (int j=0; j < NGRID; j++) {
      double kappa = min_kappa + double(j)*delta_kappa;
      double minusTwiceLogLikelihood=0;
      double denom = tmax*kappa + (1.0-exp(-gamma*tmax))/gamma;    
      // Loop over the data generated above
      // -----------------------------------
      int idatmax = data.size();
      for (int idat=0; idat < idatmax; idat++) {
        double Likelihood = (kappa+exp(-gamma*data[idat]))/denom;
        minusTwiceLogLikelihood += -2.0*log(Likelihood);
      }

      likelihoodGrid[i][j]= minusTwiceLogLikelihood;
      
      if(minusTwiceLogLikelihood < min) {
        best_i=i;
        best_j=j;
        min=minusTwiceLogLikelihood;
      }
    }
  }

  for(int i=0; i<NGRID; i++) {
    for(int j=0; j<NGRID; j++) {
      h_loglike.SetBinContent(i,j,likelihoodGrid[i][j]-min);
    }
  }
  double best_gamma = min_gamma+double(best_i)*delta_gamma;
  cout << "Gamma true is: " <<  GammaTrue
       << " best gamma: " << best_gamma << endl;
  cout << "kappa true is: " << kappaTrue 
       << " best kappa: " << min_kappa + double(best_j)*delta_kappa << endl;

  // Draw the 2D plot
  h_loglike.Draw("COL");
  c1.Update();
  c1.Print("LifeTimeLikelihood_plot2.png");
  

  // Hold kappa at true value and scan Gamma
  int imin=0;
  double yAtMin=1.0e20;
  for (int i=0; i<NGRID; i++) {
    x[i] = min_gamma + double(i)*delta_gamma;
    y[i] = likelihoodGrid[i][NGRID/2];
    if(y[i]<yAtMin) {
      yAtMin=y[i];
      imin = i;
    }
  }

  // Calculate the +- 1 sigma values
  double delPlus=0.0, delMinus=0.0;
  int iPlus = imin, iMinus = imin;

  while(delPlus<1.0 && iPlus<NGRID) {
    delPlus=y[iPlus]-y[imin];
    iPlus++;
  }
  while(delMinus<1.0 && iMinus>-1) {
    delMinus=y[iMinus]-y[imin];
    iMinus--;
  }
  cout << " delPlus " << delPlus << " delMinus " << delMinus << endl;
  // The rest of this is just making the plot
  // =========================================
  cout  << "Estimate of gamma: " << best_gamma
	  << "^{+" << x[iPlus]-x[imin] <<"}_{"
	<< x[imin]-x[iMinus] << "}" << endl;

  ostringstream fitinfo;
  fitinfo << "Estimate of gamma: " << best_gamma
	  << "^{+" << x[iPlus]-x[imin] <<"}_{"
	  << x[imin]-x[iMinus] << "}";

  string strFitInfo = fitinfo.str();

  double xx[2], yy[2];
  xx[0] = x[iMinus];
  yy[0] = y[iMinus];
  xx[1] = x[iPlus];
  yy[1] = y[iMinus];

  
  TCanvas* c = new TCanvas();
  TGraph* gr1 = new TGraph(2,xx,yy);
  gr1->SetLineColor(kRed);
  gr1->SetLineWidth(4.0);
  gr1->SetMarkerSize(0.0);
  
  TGraph* gr = new TGraph(NGRID,x,y);
  gr->SetLineWidth(2.0);
  gr->GetXaxis()->SetTitle("#Gamma");
  gr->GetYaxis()->SetTitle("-2ln(L)");
 
  gr->Draw();
  gr1->Draw("same");
  double delY=y[0]-yy[0];

  cout << " yy[0] " << yy[0] << " y[0] " << y[0] << endl; 
  //  TLatex * tex0 = new TLatex(min_gamma+0.35,yy[0]+5.0*range,"Determination of #Gamma");
  //  tex0->Draw();
  TLatex * tex1 = new TLatex(min_gamma+0.35,yy[0]+0.8*delY,"True #Gamma: 2.0");
  tex1->Draw();
  TLatex * tex2 = new TLatex(min_gamma+0.35,yy[0]+0.65*delY,strFitInfo.c_str());
  tex2->Draw();
  TLatex* tex3 = new TLatex(min_gamma+0.35,yy[0]+0.5*delY,"#Delta(-2ln(L))=1.0");
  tex3->SetTextColor(kRed);
  tex3->Draw();

  c->SaveAs("LifeTimeLikelihood_plot3.png");
  
}


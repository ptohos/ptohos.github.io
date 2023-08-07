/*
  The Problem:
  Suppose our data obeys the distribution
  N(x) = A + Bx for 0<x<10.
  1) Generate 1000 randomly distributed events for the case A=1, B-2
  2) Take these 1000 events as your data sample.  Use the log-likelihood
     method to determine the value of kappa and its uncertainty. 
*/
// --------------------------------------------------------------------------//
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#include <TROOT.h>
#include <TH1.h>
#include <TF1.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TFile.h>
#include <TMath.h>
#include <TRandom3.h>
#include <TGraph.h>
#include <TLatex.h>

// ------------------------------------------------------------------------- //
void ExampleLikelihoodFit() {
//-- ----------------------------------------------------------------------- //

  // Some things to make the plot look nice
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
  

  // Here we go with the real thing
  
  const int Ntries = 1000;     // Number of tries
  double A = 1.0;
  double B = 2.0;
  double x_max = 10.0;
  
  vector<double> data;        // Vector of data measurements
  TRandom3 r;
  gRandom->SetSeed(123);
  

  // Generate data:
  // ===============
  
  // Define the function A+Bx with
  // ------------------------------
  
  TF1* myfun =  new TF1("myfun","[0]+[1]*x",0,x_max); 
  myfun->SetParameter(0,A);
  myfun->SetParameter(1,B);
  
  // Use that function to generate 1000 random points
  // ------------------------------------------------
  
  for(int i=0; i<Ntries; i++) {
    double x = myfun->GetRandom();
    data.push_back(x);
  }

  // Analyze the data
  // =================
  // Start by initializing all the variables
  const int Ngrid=100;
  double min_kappa = 0.0;
  double max_kappa = 1.0;
  double delta_kappa = (max_kappa-min_kappa)/Ngrid;
  double min=1.0e20;
  int best_i = -1;
  double x[100];
  double y[100];


  // Loop over hypothesis for the value of kappa and calculate log likelihood
  // ---------------------------------------------------------------------
  for (int i=0; i < Ngrid; i++) {
    double kappa = min_kappa + double(i)*delta_kappa;
    double beta = 1.0/(kappa*x_max+0.5*x_max*x_max);
    double alpha = beta*kappa;
    double minusTwiceLogLikelihood=0;
    
    // Loop over the data generated above
    // -----------------------------------
    for (uint idat=0; idat < data.size(); idat++) {
      double Likelihood = alpha+beta*data[idat];
      minusTwiceLogLikelihood += -2.0*log(Likelihood);
    }
    x[i] = kappa;
    y[i] = minusTwiceLogLikelihood;
    if(minusTwiceLogLikelihood < min) {
      best_i=i;
      min=minusTwiceLogLikelihood;
    }
  }
  
  // Calculate the minimum
  double best_kappa = min_kappa+double(best_i)*delta_kappa;

  // Calculate the +- 1 sigma values
  double delPlus=0.0, delMinus=0.0;
  int iPlus = best_i, iMinus = best_i;

  while(delPlus<1.0) {
    delPlus=y[iPlus]-y[best_i];
    iPlus++;
  }
  while(delMinus<1.0) {
    delMinus=y[iMinus]-y[best_i];
    iMinus--;
  }

  //
  // Make the plot using the above results
  // =========================================
  ostringstream fitinfo;
  fitinfo << "Estimate of kappa: " << best_kappa
	  << "^{+" << x[iPlus]-x[best_i] <<"}_{-"
	  << x[best_i]-x[iMinus] << "}";

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

  TGraph* gr = new TGraph(Ngrid,x,y);
  gr->SetLineWidth(2.0);
  gr->GetXaxis()->SetTitle("#kappa");
  gr->GetYaxis()->SetTitle("-2ln(L)");
 
  gr->Draw();
  gr1->Draw("same");

  double max = y[0];
  double range = max-min;

  //
  // Write some text for explanation
  //------------------------------------
  TLatex * tex0 = new TLatex(0.1,min+0.98*range,"Determination of #kappa from 1,000 MC events");
  tex0->Draw();
  TLatex * tex1 = new TLatex(0.35,min+0.9*range,"True #kappa=0.5");
  tex1->Draw();
  TLatex * tex2 = new TLatex(0.35,min+0.8*range,strFitInfo.c_str());
  tex2->Draw();
  TLatex* tex3 = new TLatex(0.4,min+0.1*range,"#Delta(-2ln(L))=1.0");
  tex3->SetTextColor(kRed);
  tex3->Draw();

  c->SaveAs("Example_LogLikelikhood.png");
  
}


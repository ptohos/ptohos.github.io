#include "TCanvas.h"
#include "TSystem.h"
#include "TH2.h"

//===================
void example1(){
//===================
// define three Poisson and three Gaussian distributions as
// functions and draw them.
//===================
  gStyle->SetOptStat(0);
  const float pi=3.14157;
  TF1* poiss0=new TF1("poiss1","TMath::Poisson(x,2)",0,50);
  TF1* poiss1=new TF1("poiss1","TMath::Poisson(x,10)",0,50);
  TF1* poiss2=new TF1("poiss1","TMath::Poisson(x,20)",0,50);

  TF1* gauss0=new TF1("gauss0","(TMath::Gaus(x,2,sqrt(2)))/(sqrt(2*2*pi))",0,50);
  TF1* gauss1=new TF1("gauss1","(TMath::Gaus(x,10,sqrt(10.)))/(sqrt(10.*2*pi))",0,50);
  TF1* gauss2=new TF1("gauss2","(TMath::Gaus(x,20,sqrt(20.)))/(sqrt(20.*2*pi))",0,50);
  // set the line colors for gaussian to red
  gauss0->SetLineColor(kRed);
  gauss1->SetLineColor(kRed);
  gauss2->SetLineColor(kRed);
  
  // define a dummy histogram
  TH1F* null = new TH1F("nl","",35,0,35);

  TCanvas* c1 = new TCanvas("c1","",800,600);
  null->SetMaximum(0.5);
  null->Draw();
  // draw all the functions
  poiss0->Draw("same");
  gauss0->Draw("same");
  poiss1->Draw("same");
  gauss1->Draw("same");
  poiss2->Draw("same");
  gauss2->Draw("same");
  // add a legend to label them
  TLegend* leg;
  leg=new TLegend(0.6,0.6,0.9,0.9);
  leg->AddEntry(poiss0,"Poisson","l");
  leg->AddEntry(gauss0,"Gauss","l");
  leg->Draw();
  // print this to a png file
  c1->Print("gauspois.png");
}

//===================
void example2(){
//===================
// we simulate the through of a die N times (N=10, 100 and 1000)
//===================
  gStyle->SetOptStat(0);
  TH1F* null1 = new TH1F("nl1","",6,0.5,6.5);

  TH1F* hist10 = new TH1F("h10","",6,0.5,6.5);
  TH1F* hist100 = new TH1F("h100","",6,0.5,6.5);
  TH1F* hist1000 = new TH1F("h100","",6,0.5,6.5);
  hist10->SetLineColor(2);hist10->SetLineWidth(4);
  hist100->SetLineColor(4);hist100->SetLineWidth(4);
  hist1000->SetLineWidth(4);
  TRandom* rand=new TRandom();

  // Throw a die 1000 times and get a random number
  // between 1 and 6 for each throw.
  for (int i=0;i<1000;i++) {
    float r0=rand->Integer(6)+1;
    if (i<10)  hist10->Fill(r0);
    if (i<100)  hist100->Fill(r0);
    hist1000->Fill(r0);
  }
  // label the axes
  null1->GetXaxis()->SetTitle("die value");
  null1->GetYaxis()->SetTitle("fraction of throws");
  TCanvas* c1 = new TCanvas("c1","",800,600);
  null1->Draw();
  hist10->DrawNormalized("same");
  hist100->DrawNormalized("same");
  hist1000->DrawNormalized("same");
  printf("mean=%6.2f, RMS=%6.2f\n",hist10->GetMean(),hist10->GetRMS());
  printf("mean=%6.2f, RMS=%6.2f\n",hist100->GetMean(),hist100->GetRMS());
  printf("mean=%6.2f, RMS=%6.2f\n",hist1000->GetMean(),hist1000->GetRMS());
  TLegend* leg;
  leg=new TLegend(0.6,0.6,0.9,0.9);
  leg->AddEntry(hist10,"10 throws","l");
  leg->AddEntry(hist100,"100 throws","l");
  leg->AddEntry(hist1000,"10000 throws","l");
  leg->Draw();
  c1->Print("dice.png");
}

//===================
void example3(){
//===================
// we simulate a lifetime distribution and then we fit it
//===================
  gStyle->SetOptFit(1111);
  // assume lifetime of c*tau=500 micron
  float ctau=500; 
  TH1F* tau1=new TH1F("t1","",100,0,5000);
  TH1F* tau2=new TH1F("t2","",100,0,5000);
  TH1F* tau3=new TH1F("t3","",100,0,5000);
  // emulate 10, 1000 and 100000 measurements
  TRandom* rand=new TRandom();
  for (int i=0;i<100000;i++) {
    float r0=rand->Exp(ctau);
    if (i<10) tau1->Fill(r0);
    if (i<1000) tau2->Fill(r0);
    tau3->Fill(r0);
  }
  tau1->GetXaxis()->SetTitle("ct [#mu m]");
  tau1->GetYaxis()->SetTitle("fraction of experiments");
  tau1->SetLineColor(2);tau1->SetLineWidth(4);
  tau2->SetLineColor(4);tau2->SetLineWidth(4);
  tau3->SetLineWidth(4);
  tau1->SetAxisRange(0,3000);
  TCanvas* c1 = new TCanvas("c1","",800,600);
  tau1->DrawNormalized();
  tau2->DrawNormalized("same");
  tau3->DrawNormalized("same");
 TLegend* leg;
 leg=new TLegend(0.6,0.6,0.9,0.9);
  leg->AddEntry(tau1,"10 measurements","l");
  leg->AddEntry(tau2,"1000 measurements","l");
  leg->AddEntry(tau3,"100000 measurements","l");
  leg->Draw();
  // get the mean and the RMS of each
  printf("mean=%6.2f, RMS=%6.2f\n",tau1->GetMean(),tau1->GetRMS());
  printf("mean=%6.2f, RMS=%6.2f\n",tau2->GetMean(),tau2->GetRMS());
  printf("mean=%6.2f, RMS=%6.2f\n",tau3->GetMean(),tau3->GetRMS());
  c1->Print("ctau.png");
  // now we can also fit the lifetime with an exponential
  tau2->Fit("expo");
}

//===================
void example4() {
//===================
// we simulate a gaussian distribution centered at 90
// and perform a gaussian and a 2nd order polynomial fit
//====================
  TRandom* rand=new TRandom();
  gStyle->SetOptFit(1111);
  TH1F* mass = new TH1F("mass","",70,55,125);
  mass->GetXaxis()->SetTitle("mass [GeV/c^{2}]");
  mass->GetYaxis()->SetTitle("number of events per 0.5 GeV/c^{2}");
  for (int i=0;i<1000;i++) {
    mass->Fill(rand->Gaus(90,5));
  }
  mass->Draw();
  //== Fit with a gaussian
  mass->Fit("gaus");
  TCanvas* c1 = new TCanvas("c1","",800,600);
  c1->Clear();
  c1->cd(1);
  mass->Draw("e");
  c1->Print("mass_fit1.png");
  // now fit 2nd order polynomial but in the range between 80 and 100 GeV
  mass->Fit("pol2","","",80,100);
  c1->Clear();
  c1->cd(1);
  mass->Draw("e");
  c1->Print("mass_fit2.png");
}

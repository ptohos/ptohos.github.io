#include <iostream>
#include <string>

#include <TROOT.h>
#include "TRandom.h"
#include "TH1F.h"
#include "TCanvas.h"

using namespace std;

void centralLimit(int numEvt, int numTrials, string fileName, bool printIt) {

  // Create one histogram 
  // Arguments are: Name of histogram, Title, number of bins,min, max
  TH1F hist("hist","Number of Entries vs X",100,0,1.0);
  
  // This next command makes Root calcuate the mean and sigma using the
  // data rather than the center of the bins.
  hist.Sumw2();

  // We need to create an object that is a random number generator
  TRandom* random = new TRandom();
  random->SetSeed(123);

  cout << "About to generate " << numTrials << " trials with " << numEvt
       << " events per trial"  << endl;

  for (int trials = 0; trials<numTrials; trials++) {
    double sum=0;
    double sumsq=0;
    double x;
    for (int i=0; i<numEvt; i++) {
      // TRandom::Uniform(x) throws a flat distribution from 0 to x
     x = random->Uniform(1.0);
     sum+=x;
     sumsq+=x*x;
    }
    double av = sum/((double) numEvt);
    double avsq = sumsq/((double) numEvt);
    hist.Fill(av);
    if(printIt) cout << "For trial " << trials << " mean x=" << av
		     << " sigma=" << sqrt(avsq-av*av) << endl;
  }
  // Make a canvase and put the plot on it.
  TCanvas c1;
  hist.Draw();
  c1.cd(2);
  c1.Print(fileName.c_str());

}           //End of macro

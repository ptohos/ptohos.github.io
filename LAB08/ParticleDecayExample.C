//===========================================================================
// Filename:  ParticleDecayExample.C
//
// An example of how to write a simple
// Monte Carlo using ROOT.
//
// To run this macro startup ROOT and then do:
//
// .L ParticleDecayExample.C++
// doParticleDecays(10000,10.0,20.0);
//
// To exit ROOT type
// .q
//
// The output of this macro is a gif file called ParticleDecayPlots.gif and
// a root file called ParticleDecayExample.root
//
// Here is the problem we are simulating:
// 
// A beam of 10,000 B+ particles with lifetime of 1.638e-12 and mass
// 5.279 GeV start at x=0 and travel in the +x-direction. The particle
// beam have momenta uniformly distributed between 10 and 20 GeV.
//
//  a) Make a 1 dimensional histogram of the number of particles that decay 
//     as a function of x for x between 0 and 1 cm 
//  b) Make a profile plot of the mean decay distance as a function of 
//     B+ momentum (a profile plot gives the average value of one variable
//     as a function of another)
//===========================================================================

#include <iostream>     // This is the C++ class used to print things
                        // All Root classes have names starting with T
#include "TRandom.h"    // This is the random number class in Root
#include "TH1F.h"       // This is a 1D histogram
#include "TProfile.h"   // A profile plot gives the mean and variance per bin
#include "TCanvas.h"
#include "TFile.h"

using std::cout;
using std::endl;
//===========================
// This declares our class
// The input is the number of events, the min and the max momentum 
//
// The way the code is written is to allow the user to pass the
// number of events to simulate and the range of particle momenta
// Pmin and Pmax.
// The code has hard wired the mass and lifetime of the particle which
// someone may decide to pass also as arguments.
//==========================
void doParticleDecays(int numEvt, double Pmin, double Pmax) {

  double tau = 1.638e-12; //seconds   Lifetime
  double mass = 5.279; // GeV
  double c = 3.0e10;  // cm per sec   speed of light

  // Create one histogram and one Profile plot
  // Arguments are: Name of Profile, Title, number of bins,min, max
  TProfile hProf("hProf","Mean Decay distance vs momentum",100,Pmin,Pmax);

  // Arguments are: Name of histogram, Title, number of bins,min, max
  TH1F hist("hist","Number of Decays vs distance",100,0,1.0);

  // We need to create an object that is a random number generator
  TRandom* random = new TRandom();
  // It could be done also with the instruction TRandom random
  // which defines an object of the class TRandom;
  
  cout << "About to generate " << numEvt << " events" 
       << " with Pmin=" << Pmin << " and Pmax = " << Pmax << endl;
  for (int i=0; i<numEvt; i++) {
    // Throw dice to get the momentum of the particle
    // TRandom::Uniform(x) throws a flat distribution from 0 to x
    double momentum = Pmin+random->Uniform(Pmax-Pmin);
    //Distribution from Pmin to Pmin+DeltaP<=Pmax
    // Now let's find the proper decay length
    double energy = sqrt(momentum*momentum+mass*mass);
    double beta = momentum/energy;           //boost=v/c = p/E
    double gamma = 1.0/sqrt(1.0-beta*beta);  //Lorentz gamma=1/sqrt(1-(v/c)**2) 
    // Throw dice to get the decay length
    // TRandom::Exp(tau) generates according to Exp(-t/tau)
    double distance=random->Exp(gamma*c*tau);
    //        
    //==========*******=====================
    // BTW, if you created something with a "new" you use a "->" to get to
    // its methods since "new" gives you back a pointer.
    // If you created it with just a declaration you use a "."
    // (i.e. if we had defined the object random as TRandom random
    // we could have used it as:  momentum=Pmin+random.Uniform(Pmax-Pmin)
    // Below we use like this the object hist that was declared for the 1d
    // histogram and the object hProf
    //======================================
    hist.Fill(distance);
    hProf.Fill(momentum,distance);
  }
  // Make a canvas and put the two plots on it.  Then write the plot to a file
  TCanvas c1;
  c1.Divide(1,2);
  c1.cd(1);
  hist.Draw();
  c1.cd(2);
  hProf.Draw();
  c1.Print("ParticleDecayPlots.gif");
  // Create a root file and write the histogram and profile to it in
  // root format.  You can then display them later in root
  // WARNING: If you run this macro twice, you will overwrite the root file
  // If you change "recreate" to "new" then the macro will signal an error
  // and fail to write a file if a file with the specified name already exists
  TFile f("ParticleDecayExample.root","recreate");
  hProf.Write();
  hist.Write();

}           //End of macro

/****************************************************
  Ypologismos radienergoy diaspasis purinwn
  San input dedomena xrisimopoiounta ta akoloutha
  NoParticleStart = 1000
  max_steps  = 5000
  Nsamples   = 1000
  decay_prob = 0.001
 Oi parapanw times dinontai se ena arxeio to 
 onoma tou opoiou to programma zita apo to xristi 
 Ta dedomena tha prepei na dwthoun sti morfi 
 1000
 5000 
 1000
 0.001
 
****************************************************/
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
using namespace  std;

// Dilwsi sunartisewn gia eisagwgi stoixeiwn
// oloklirwsi kai eksagwgi stoixeiwn
void initialise(int&, int&, int&, double& ) ;
void mc_sampling(int, int, int, double, int*);
void output(int, int, int*);

int main()
{
  int NoParticleStart, max_steps, Nsamples;
  double decay_prob;
  srand(time(NULL));
    
  // Read in data 
  initialise(NoParticleStart, max_steps, Nsamples, decay_prob);

  int ncumulative[max_steps+1];

  // Do the mc sampling
  mc_sampling(NoParticleStart, max_steps, Nsamples, decay_prob, ncumulative);

  // Print out results 
  output(max_steps, Nsamples, ncumulative);

  // Done
  return 0; 
}

void initialise(int & NoParticleStart, int & max_steps, int & Nsamples,
                double & decay_prob) 
{
  ifstream inpfile;
  string inpfilename;
  
  cout << "Give the name of the input file" << endl;
  cin >> inpfilename;
  inpfile.open(inpfilename.c_str());
  if (inpfile.fail()) {
    cout << " Problems with input file "<< endl;
    return;
  }
  cout << "Initial number of particles = " << endl ;
  inpfile >> NoParticleStart;
  cout << "maximum time = " << endl;
  inpfile >> max_steps;
  cout << "# MC steps= " << endl;
  inpfile >> Nsamples;
  cout << "# Decay probability= " << endl;
  inpfile >> decay_prob;
  cout << "Arxikes sunthikes" << endl;
  cout << " No of nuclei: " << NoParticleStart << endl;
  cout << " Decay probability w=1/t:" << decay_prob << endl;
  cout << " Max MC steps: " << max_steps << endl;
  cout << " Max MC samples: " << Nsamples << endl;
}  // end of function initialise   


void output(int max_steps, int Nsamples, int* ncumulative)
{
  ofstream outfile;
  string outfilename, rootfile;
  cout << "Give the name of the output file" << endl;
  cin >> outfilename;
  outfile.open(outfilename.c_str());
  if (outfile.fail()) {
    cout << "Problems opening output file" << endl;
    return;
  }
  for(int i=0; i <= max_steps; i++){
    outfile << setiosflags(ios::showpoint | ios::uppercase);
    outfile << setw(15) << i;
    outfile << setw(15) << setprecision(8);
    outfile  << ncumulative[i]/((double) Nsamples) << endl;
  }
  outfile.close();
}  // end of function output 


void mc_sampling(int NoParticleStart, int max_steps, int Nsamples,
                 double decay_prob, int *ncumulative)
{
  /*************************************************************************
  Perigrafi tis diadikasias deigmatolipsias:
  Ena MC peirama/deigma sunistatai apo tin prosomoiwsi tis diaspasis
  twn purinwn sumfwna me tin prokathorismeno pithanotita (decay_prob). 
  Se kathe xroniko vima (istep) eksetazontai oloi oi purines pou 
  yparxoun diathesimoi gia diaspasi (No2Decay) gia to an tha diaspastoun
  me vasi tin decay_prob. Analoga allazei o arithmos twn pyrinwn 
  pou den exoun diaspastei kai tha xrisimopoiithou stin epomeni 
  xroniki stigmi. 
  H diadikasia epanalamvanetai mexri mia megisti xroniki stigmi 
  (max_steps) pou einai o megistos arithmos epanalipsewn gia to MC deigma.
  Ta parapanw apoteloun ena kai mono MC peiram/deigma. Gia na 
  yparxei statistiki meleti tha prepei na epanalifthei i diadikasia 
  arketes fores (Nsamples)
 *************************************************************************/
  for (int i=0; i<=max_steps; i++) ncumulative[i] = 0;
  for (int isample = 1; isample <= Nsamples; isample++){   
    int No2Decay = NoParticleStart;
    ncumulative[0] += NoParticleStart;

    for (int istep=1; istep <= max_steps; istep++){
      int Particle2Decay = No2Decay;
      //dokimi olwn twn purinwn gia diaspasi
      for (int Nparticle = 1; Nparticle <= Particle2Decay; Nparticle++) {
	    double rnd = double(rand())/RAND_MAX;
        if( rnd <= decay_prob) {
          No2Decay--;
        }
      }  // end of loop over particles 
      ncumulative[istep] += No2Decay; // O arithmos twn pirinwn pou apomenoun
                                      // ti sygkekrimeni xroniki stigmi istep
                                      // kai gia to sygkekrimeno deigma isample
                                      // athroizetai sta apotelesmata twn allwn 
                                      // isample deigmatwn. Etsi sto telos 
                                      // tha exoume ton anamenomeno meso arithmo
                                      // purinwn se kathe xroniki stigmi
    }  // end of loop over MC steps 
  }    // end of loop over MC samples
}   // end mc_sampling function  



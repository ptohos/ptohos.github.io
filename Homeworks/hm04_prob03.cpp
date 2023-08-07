/*****************************************************************
 Programma gia tin prosomoiwsi tou theorimatos Fermat elaxistou  
 xronou gia to fwtos otan ayto kineitai apo ena meso me deikti
 diathlasi n1 se allo me deikti diathlasis n2 mesw mias 
 diaxwristikis epifaneias

 Gia na to kanete link me to root xrisimopoiiste tin entoli 
  g++ -I `root-config --incdir` hm04_prob03.C `root-config --libs` -o test

 Tha mporoysate na trexete to file me tin entoli: 
 ./test < hm04_prob03.inp
 To hm04_prob03.inp periexei ola ta dedomena:
 Number of surfaces:      10
 Position of divider:      5
 Index of refraction:      1
 Index of refraction:      1.5
 Position of light source: 2
 Position of light detect: 8
 Step to move surface hit: 0.5
 Tries to perform:         1000000
 File out                  hm04_prob03.dat
 Root File out             hm04_prob03.root
 To histogram sto root mporeite na to deite me tin entoli 
 light2->Draw("pl");      to l enwnei me grammi ta simeia-p einai o marker 
******************************************************************/
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <TFile.h>
#include <TH1D.h>
#include <TH2D.h>

using namespace std;

void initialize(int&, int&, double&, vector<double>&, vector<double>&);
void change_path(int, double, vector<double>&, vector<double>);
void write_out(vector<double>, vector<double>);

int main() {
  srand(time(NULL));
  vector<double> ysurf, vsurf;
  vector<double> yinit;
  double dymax;
  int NSurf, Ntries;

  initialize(NSurf, Ntries, dymax, ysurf, vsurf);
  yinit = ysurf;
  change_path(Ntries, dymax, ysurf,vsurf);
  write_out(ysurf,yinit);
}

void initialize(int& NSurf, int& Ntries, double& dymax, 
		vector<double>& ysurf, vector<double>& vsurf){
  int Ndiv;
  double nindex1, nindex2;
  double fpos, lpos;
  double ymin, ymax;
  cout << " Enter the number of surfaces" << endl;
  cin >> NSurf;
  cout << " Enter the number of the dividing surface" << endl;
  cin >> Ndiv;
  cout << " Enter the index of refraction for 1st medium" << endl;
  cin >> nindex1;
  cout << " Enter the index of refraction for 2nd medium" << endl;
  cin >> nindex2;
  cout << " Enter the position of the light source on 1st surface\n";
  cin >> fpos;
  cout << " Enter the position of the light detector on last surface\n";
  cin >> lpos;
  cout << " Enter the max vertical variation dy gia allagi\n";
  cin >> dymax;
  cout << " Enter the max number of tries\n";
  cin >> Ntries;
  
  for (int i=0; i<NSurf; i++) {
    vsurf.push_back(1./nindex1);
    if (i >= Ndiv) vsurf[i] = 1./nindex2;  // o tropos prosvasis se stoixeio 
                                           // toy vector poy douleuei panta 
                                           // einai []. 
                                           // O tropos vector.at(i) doyleyei
                                           // otan to vector einai const
                                           // poy den isxyei edw
    if (i==0) {
      ysurf.push_back(fpos);
    }
    else if (i<NSurf-1) {
      double rnd = double(rand())/RAND_MAX;
      double apos = fpos + (lpos-fpos)*rnd;
      ysurf.push_back(apos);
    }
    else {
      ysurf.push_back(lpos);
    }
  }
}


void change_path(int Ntries, double dymax, 
		 vector<double> & ysurf, vector<double> vsurf){
  double t_org, t_new;
  double ynew, dych;
  double dxpos, dist;
  double dysq;
  int Nsurf = ysurf.size();
  dxpos = 1;

  for (int itries=0; itries < Ntries; itries++) {
    double rnd = double(rand())/RAND_MAX;
    int isurf = 1+int((Nsurf-2)*rnd);        // Epilogi tuxaias epifaneias 
    rnd = double(rand())/RAND_MAX;           // prepei na ksanariksoume tyxaio
                                             // arithmo
    ynew = ysurf[isurf] + (2*rnd -1)*dymax;  // Epilogi neou simeiou 
                                             // tyxaia katanemimenou ws pros
                                             // to arxiko simeio kai mesa 
                                             // sto diastima +/- dymax
    dysq = pow((ysurf[isurf] - ysurf[isurf+1]),2);
    dist = sqrt(dxpos*dxpos + dysq);         // d stin epomeni epifaneia
    t_org = dist/vsurf[isurf];               // t gia tin epomeni epifaneia
    dysq = pow((ysurf[isurf] - ysurf[isurf-1]),2);
    dist = sqrt(dxpos*dxpos + dysq);         // d stin proigoumeni epifaneia
    t_org = t_org + dist/vsurf[isurf-1];     // t_tot gia na paei apo
                                             // metaksy twn 2 epeifaniwn
                                             // isurf-1 se isurf+1
    // Epanalamvanoume gia to neo simeio
    dysq = pow((ynew - ysurf[isurf+1]),2);
    dist = sqrt(dxpos*dxpos + dysq);
    t_new = dist/vsurf[isurf];
    dysq = pow((ynew - ysurf[isurf-1]),2);
    dist = sqrt(dxpos*dxpos + dysq);
    t_new = t_new + dist/vsurf[isurf-1];

    if (t_new < t_org) {    // mikroteros xronos
      ysurf[isurf] = ynew;
    }
  } // ntries
}// function


void write_out(vector<double> ypos, vector<double> yinit){
  ofstream outfile;
  string outfilename, rootfilename;
  cout << "Give the output name\n";
  cin >> outfilename;
  outfile.open(outfilename.c_str());
  if (outfile.fail()) {
    cout << " Error opening output file" << endl;
    return;
  }
  cout << "Give the root file name\n";
  cin >> rootfilename;
  TFile* rootout = new TFile(rootfilename.c_str(),"RECREATE");
  if (! rootout->IsOpen()){
    cout << " Error opening root file" << endl;
    return;
  }
  int nsurf = ypos.size();

  TH1D* light1 = new TH1D("light1", "Light path arxika",nsurf,-0.5,nsurf-0.5);
  TH1D* light2 = new TH1D("light2", "Light path telika",nsurf,-0.5,nsurf-0.5);
 
  for(int i=0; i < nsurf; i++){
    outfile << setiosflags(ios::showpoint | ios::uppercase);
    outfile << setw(15) << i;
    outfile << setw(15) << setprecision(8) << ypos[i];
    outfile << setw(15) << setprecision(8) << yinit[i] << endl;

    light1->Fill(i,yinit[i]);
    light2->Fill(i,ypos[i]);
  }
  rootout->Write();
  rootout->Close();
}  // end of function output 

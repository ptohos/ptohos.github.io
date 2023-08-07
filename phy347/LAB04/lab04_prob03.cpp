#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct PartInfo {

  int    pid;
  int    q;
  float  px;
  float  py;
  float  pz;
  float  E;
  float  m;

  void init() {
    pid         =  0;
    q           =  -99;
    px          =  0.0;
    py          =  0.0;
    pz          =  0.0;
    E           =  0.0; 
    m           =  0.0;
  }
};
/**************************
 Declaring some functions
***************************/
void  Event_Analysis(vector<PartInfo>, vector<PartInfo>,
		     vector<PartInfo>, vector<PartInfo> &, 
                     vector<PartInfo> &, vector<PartInfo> &,
		     vector<PartInfo> &);
void  FillPartInfo(PartInfo &aParticle);
float GetTransverseMomentum(PartInfo aParticle);
float GetRapidity(PartInfo aParticle);
int   HadronIdentity(int partId);
/*****************
 Global variables
******************/
int ntot_evts=0, ntot_ele=0, ntot_muo=0, ntot_had=0;
int ntot_gdele=0, ntot_gdmuo=0, ntot_bhad=0, ntot_chad=0;
int old_evt=-1;

int read_evt, read_pid;
float read_E, read_m;
float read_px, read_py, read_pz;

int main() {
  vector<PartInfo> EleColl;
  vector<PartInfo> MuoColl;
  vector<PartInfo> HadColl;
  //
  vector<PartInfo> GdEleColl;
  vector<PartInfo> GdMuoColl;
  vector<PartInfo> BhadColl;
  vector<PartInfo> ChadColl;

  ifstream inpfile;
  inpfile.open("Particles.dat");
  /***************
   Read the data
  ****************/
  while (1) {
    if (inpfile.fail()) break;
    inpfile >> read_evt >> read_pid >> read_px 
            >> read_py >> read_pz >> read_E >> read_m;

    /******************
    Check for new event 
    if true tote kane tin analusi tou proigoumenou event
    xrisimopoiontas ola ta collections twn swmatidiwn 
    Otan teleiwsei krata statistiki kai reset ta collections
    *******************/
    if (read_evt != old_evt) {
      Event_Analysis(EleColl,MuoColl,HadColl,GdEleColl,
		     GdMuoColl,BhadColl,ChadColl);
      old_evt = read_evt;
      ntot_evts ++;
      ntot_ele = ntot_ele + EleColl.size();
      ntot_muo = ntot_muo + MuoColl.size();
      ntot_had = ntot_had + HadColl.size();
      ntot_gdele = ntot_gdele + GdEleColl.size();
      ntot_gdmuo = ntot_gdmuo + GdMuoColl.size();
      ntot_bhad  = ntot_bhad  + BhadColl.size();
      ntot_chad  = ntot_chad  + ChadColl.size();
      EleColl.clear();
      MuoColl.clear();
      HadColl.clear();
      GdEleColl.clear();
      GdMuoColl.clear();
      BhadColl.clear();
      ChadColl.clear();
    }
    /********************
    Fill of the collections/particle type
    *********************/
    if (abs(read_pid) == 11) {
      PartInfo Ele;      //Dimiourgia enos antikeimenou typou PartInfo
      Ele.init();            //Initilization twn idiotitwn toy
      FillPartInfo(Ele); //Gemisma twn idiotitwn tou
      EleColl.push_back(Ele); //kratame ton arithmo twn object Ele se vector
    }
    else if (abs(read_pid) == 13){
      PartInfo Muo;
      Muo.init();
      FillPartInfo(Muo);
      MuoColl.push_back(Muo);
    }
    else {
      PartInfo Hadron;
      Hadron.init();
      FillPartInfo(Hadron);
      HadColl.push_back(Hadron);
    }
  } 

  cout << "Total number of events read = " << ntot_evts << endl;
  cout << "No. of electrons = "<< ntot_ele << " out of which " 
       << ntot_gdele << " with pt > 20 GeV " << endl; 
  cout << "No. of muon      = "<< ntot_muo << " out of which " 
       << ntot_gdmuo << " with pt > 20 GeV" << endl;
  cout << "No. of hadrons   = "<< ntot_had << endl;
  cout << "There are " << ntot_bhad << " b-hadrons with pt>20GeV" << endl;
  cout << "There are " << ntot_chad << " c-hadrons with pt>20GeV" << endl;
}
   
void Event_Analysis(vector<PartInfo> EleColl, vector<PartInfo> MuoColl,
                    vector<PartInfo> HadColl, vector<PartInfo> &GdEleColl,
		    vector<PartInfo> &GdMuoColl, vector<PartInfo> &BhadColl, 
		    vector<PartInfo> &ChadColl) 
{
  int nele = EleColl.size();
  int nmuo = MuoColl.size();
  int nhad = HadColl.size();
  
  for (int i =0 ; i < nele; i++){
    float pt = GetTransverseMomentum(EleColl[i]);
    float rap = GetRapidity(EleColl[i]);
    if (pt >= 20) {
      GdEleColl.push_back(EleColl[i]);
    }
  }
  for (int i =0 ; i < nmuo; i++){
    float pt = GetTransverseMomentum(MuoColl[i]);
    float rap = GetRapidity(MuoColl[i]);
    if (pt >= 20) {
      GdMuoColl.push_back(MuoColl[i]);
    }
  }
  for (int i =0 ; i < nhad; i++){
    float pt = GetTransverseMomentum(HadColl[i]);
    float rap = GetRapidity(HadColl[i]);
    if (pt >= 20) {
      int PartId = HadColl[i].pid;
      int bctype = HadronIdentity(PartId);
      if (bctype == 4) {
	ChadColl.push_back(HadColl[i]);
      }
      else if (bctype == 5){
	BhadColl.push_back(HadColl[i]);
      }
    }
  }
}


void FillPartInfo(PartInfo &aParticle)      // H struct allazei
{
  aParticle.pid = read_pid;
  aParticle.q   = read_pid/abs(read_pid);
  aParticle.E   = read_E;
  aParticle.px  = read_px;
  aParticle.py  = read_py;
  aParticle.pz  = read_pz;
  aParticle.m   = read_m;
}

float GetTransverseMomentum(PartInfo aParticle)  //H struct den allazei
{
  float pt;
  pt = sqrt(aParticle.px * aParticle.px + 
            aParticle.py * aParticle.py + 
            aParticle.pz * aParticle.pz);
  return pt;
}

float GetRapidity(PartInfo aParticle)
{
  float rapidity;
  rapidity = (aParticle.E + aParticle.pz)/(aParticle.E - aParticle.pz);
  rapidity = log(rapidity);
  rapidity = 0.5*rapidity;
  return rapidity;
}

 int HadronIdentity(int partId)
   /*** An to apotelesma einai 4 exoume cquark-swmatidio
        an 5 exoyme bquark-swmatidio */
{
  int type = abs(partId)%10000; 
  if (type < 1000) {
    type = type/100;
  }
  else {
    type = type/1000;
  }
  return type;     
}

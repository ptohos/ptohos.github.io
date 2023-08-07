#include <iostream>
#include <iomanip>
#include <fstream>

#include "TFile.h"    //header files gia file,histos kai ntuples/trees
#include "TH1.h"      //den xreiazontai alla kalo na uparxoun 
#include "TH2.h"
#include "TH3.h"
#include "TNtuple.h"
#include "TTree.h"

void ReadFromFile()
{
  // Prepei na anoiksoume to file gia na to diavasoume  
  ifstream infile;         
  infile.open("myfile.dat");
  
  float x,y,z;
  int nlines = 0;

  /* Orizw ena file sto opoio mporw na apothikeusw ta histograms kai trees 
     gia na ta exw argotera */
  TFile* fileout = new TFile("basic.root","RECREATE");

  /* Orismos twn 3 eidwn histograms 1-D, 2-D kai 3-D me metavlites float
     tha mporouse na einai double to ti gemizw i integer typou alla tote 
     tha eprepe na ta orisw san TH1D i TH1I  */

  TH1F* h1 = new TH1F("h1d","x-distribution",100,-5.,5.);
  TH2F* h2 = new TH2F("h2d","y vs x", 100,-5.,5.,100,-10.,10.);
  TH3F* h3 = new TH3F("h3d","z vs y vs x", 100,-5.,5.,100,-10.,10.,50,0.,50.);
  TH3F* h4 = new TH3F("h4","test me ntuple", 100,-5.,5.,100,-10.,10.,50,0.,50.);
  /* Orismos enos ntuple to opoio mporei na kratisei tis metavlites mou
     san pinakes kai meta mporw na doulepsw me aytes kanontas diafores 
     epiloges klp. To idio to kaneis kai meta Trees pou deixnw parakatw */

  TNtuple* myntuple = new TNtuple("myntuple","ntuple from basic file","x:y:z");

  /* Edw tha mporousame na orisoume ena Tree - analogo tou ntuple"
    TTree* mytree = new TTree("mytree","MyFirstTree");
    mytree->Branch("x",&x,"x/F");   // i metavliti enos branch typou Float
    mytree->Branch("x",&y,"y/F");
    mytree->Branch("z",&z,"z/F");
  */

  // Diavazw to file
  while(1) {         // ayto simainei oso einai true (xwris provlima) diavazeis 
    infile >> x >> y >> z;   //ayto thymizei to cin alla diavazw apo to infile
    if (!infile.good())break;
    // tupwnw ta noumera pou diavazw gia tis 5 prwtes grammes
    // to %8f simenei typwse ena float (f) me 8 psifia poy perna sti thesi %
    if (nlines < 5) printf("x=%8f, y= %8f, z=%8f\n",x,y,z);
    
    // gemise ta histograms
    h1d -> Fill(x);
    h2d -> Fill(x,y);     // ston aksona y einai to y
    h3d -> Fill(x,y,z);
    myntuple -> Fill(x,y,z);
    nlines++;
  }
  // afou exw diavasei olo to ntuple mporw na kanw alla pragmata
  // Edw kanw project to ntuple se 3d histo (h4) xrisimopoiwntas 
  // tin epilogi to x kai y na einai >0 

  myntuple->Draw("x:y:z>>h4","x>0 && y>0");  

  // To idio tha mporousame na eixame kanei an anoigame to root file pou 
  // ftiaksame meta to telos tis diadikasias aytis
   
  printf("found %d data lines sto file\n",nlines);
  infile.close();   // kleinoume to file pou anoiksame gia na diavasoume ta data
  fileout->Write(); // grafoume to file me ta histos kai to ntuple
}
 

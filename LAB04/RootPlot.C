TFile* f = new TFile file("basic.root");
f.ls() ; // kanei list tou periexomenou tou file
h1d->Draw();
h2d->Draw();
h2d->Draw("surface");
gStyle->SetMarkerStyle(20);   // bullets gia marker
gStyle->SetMarkerSize(0.8);   // megethos tou marker
h3d -> Draw();
TH1D* yhisto = new TH1D("yhi","y-value",100,-10,10)
myntuple->Draw("y>>yhi");     // vale tin metavliti y sto histogram yhi 
yhisto->Draw();
// Estw thelw na dw to x kai to y mazi 
h1d->Draw();
yhisto->SetLineColor(2);   // allazoume to xrwma tis grammis
yhisto->SetLineStyle(2);   // to histo exei diakekomeni grammi
yhisto->Draw("same");
myntuple->Draw("x","x>0");

// Mporoume na dimiourgisoyme osa histos theloume stin idia selida.
// Ayto ginetai dimiourgontas ena canvas 
// to opoio mporeis na xwriseis se diafora meri .
// to onoma tou pointer sto canvas, o titlos kai oi diastaseis
//   se pixels 800 x-eyros,800 y-eyros) */
TCanvas* c2 = new TCanvas("c2","my canvas",0, 0, 800,800)   
c2->Divide(2,2)   // to xwrizw se 2x2 (4 meri diladi)
c2->cd(1);        // pigenw stin 1-o thesi (panw aristera)
h1d->Draw();
c2->cd(2);        // pigenw stin 2-i thesi (panw deksia)
h2d->Draw();
c2->cd(3);        // pigenw stin 2-i thesi (katw aristera)
h3d->Draw();
c2->cd(4);        // teleutaia thesi (katw deksia)
myntuple->Draw("x","y>0");


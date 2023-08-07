/**************************************************************
 To programma ypologizei tis ropes adraneias enos stereou gyrw
 apo 2 aksones mias sfairas, aktinas R1, pou apoteleitai apo 2
 diaforetika ylika puknotitwn d1 kai d2. To yliko me puknotita 
 d2 brisketai se ena kulindro aktinas r2, ws pros to kentro tis 
 sfairas kai ton z-aksona. To yliko me puknotita d1 gemizei to 
 upoloipo tis sfairas. Oi ropes adraneias poy ypologizontai einai
 oi Iz kai Ix pou antistoixoun se peristrofes gurw apo ton z 
 kai x aksona. To programma diavazei ena input file 'hm04_prob01.inp'
 pou periexei plirofories gia:
  sradius cradius d1 d2 nperbin maxer opou:
  * sradius: i aktina tis sfairas (se m)
  * cradius: i aktina tou kylindrou (se m)
  * d1: i puknotita tis sfaira se (kg/m^3)
  * d2: i puknotita tou kylindrou se (kg/m^3)
  * nperbin: o arithmos twn MC deigmatwn gia kathe peirama
  * maxer: to megisto statistiko sfalma
 Ta apotelesmata grafontai sto file res.dat se monades kg*m^2
 kai periexei Arithmo prospatheiwn/Sample, Iz, error, Ix, error
 To programma stamata otan epiteyxtei ikanopoiitiki akrivei 
 kai gia tis 2 ropes adraneias.
 Gia na treksete to programma afou to kanete compile dwste tin entoli
 ./hm04_prob01.x < hm04_prob01.inp
 *************************************************************
 To programma ektelei mia MC oloklirwsi mesa se kubo akmis 1 
 (diladi i sfaira brisketai se ena kouti aktinas 0.5). Apo ti
 stigmi pou to oloklirwma einai 3-d kai i synartisi pros oloklirwsi
 einai i r**2, ta apotelesmata gia tin sfaira aktinas 0.5 
 pol/zontai me (2*sradius)**5 gia na exoume to teliko apotelesma
 gia ti sfaira aktinas sradius
**************************************************************/
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

void initialize(double&,double&,double&,double&,int&,double&);

int main() {
  bool keeplooping, first=true;
  double sradius, cradius;
  double dens1, dens2;
  double precision;
  int NMCtries;  
  initialize(sradius,cradius,dens1,dens2,NMCtries,precision);
  srand(time(NULL));
  
  double rr2 = 0.25*pow((cradius/sradius),2);
  int nloops = 0;
  double avz = 0;
  double avx = 0;
  double erz = 0;
  double erx = 0;
  keeplooping = true;

  double rnd;
  while (keeplooping){
    nloops += 1;
    double sz1 = 0;
    double sz2 = 0;
    double sx1 = 0;
    double sx2 = 0;
    for (int itries=0; itries < NMCtries; itries++){
      rnd = double(rand())/RAND_MAX;   // Epilogi tyxaiou simeio sto 
      double x2 = pow((rnd - 0.5),2);  // thetiko tetartimorio toy kibou
      rnd = double(rand())/RAND_MAX;
      double y2 = pow((rnd - 0.5),2);
      rnd = double(rand())/RAND_MAX;
      double z2 = pow((rnd - 0.5),2);
      double r2 = x2 + y2;             // 2-D apostasi apo to kentro tis sfairas
      if (r2 + z2 <= 0.25) {           // 3-D apostasi apo to kentro tis sfairas
	if (r2 <= rr2) {               // H provoli sto x-y epipedo 
	  sz2 = sz2 + r2;              // einai mesa ston kulindro
	  sx2 = sx2 + y2 + z2; 
	}
	else {                         // diaforetika einai sti sfaira
	  sz1 = sz1 + r2;
	  sx1 = sx1 + y2 + z2; 
	}
      }
    }
    sz1 = sz1/double(NMCtries); //Mesi timi twn apostasewn apo tous x-z aksones
    sz2 = sz2/double(NMCtries); //gia tin sfaira kai ton kulindro
    sx1 = sx1/double(NMCtries);
    sx2 = sx2/double(NMCtries);
    double iz=(dens1 * sz1 + dens2 * sz2)*pow((2*sradius),5);// Ypogismos tis
    double ix=(dens1 * sx1 + dens2 * sx2)*pow((2*sradius),5);// ropis adraneias
    avz +=iz;
    erz +=iz*iz;
    avx +=ix;
    erx +=ix*ix;
    
    double avz_copy = avz;
    double avx_copy = avx;
    double erz_copy = erz;
    double erx_copy = erx;
    avz = avz/double(nloops);  //Mesi timi twn timw twn ropwn adraneias 
    avx = avx/double(nloops);  //apo ta mexri twra deigmata
    erx = erx/double(nloops);  //To sfalma einai v^2 = (<f>^2 - <f^2>)/nloops
    erz = erz/double(nloops);  //opws prokuptei apo N*V^2=[Sum(<f>-f_i)^2] =
                               //  Sum(<f>^2)+Sum[(f_i)^2] - 2Sum[(f_i)<f>] =
                               //  N <f>^2 + Sum[(f_i)^2] - 2<f>Sum(f_i)=
                               //  N<f>^2 + Sum[(f_i)^2] - 2N<f>^2=
                               //  Sum[(f_i)^2] - N<f>^2 => v^2 = Sum/N - <f>^2
                               //To erx=Sum[(f_i)^2]/N to <avx>=<f>^2

    erx = sqrt((erx - avx*avx)/nloops);
    erz = sqrt((erz - avz*avz)/nloops);

    if (first) {
      printf("  MC sampling \t \t Ropi adraneias Iz \t \t Ropi adraneias Ix\n");
      first = false;
    }
    printf("%5d \t \t %8.4e +/- %8.4e \t \t %8.4e +/- %8.4e\n",nloops,
	    avz,erz,avx,erx);
    if (nloops >=10 && erz/avz < precision && erx/avx < precision){
      keeplooping = false;
      break;
    }
    else {
      avz = avz_copy;
      avx = avx_copy;
      erx = erx_copy;
      erz = erz_copy;
    }
  } // end of do while 
}




void initialize(double& sradius, double& cradius, double & dens1, 
		double& dens2, int& NMCtries, double& precision){
  cout << "Input the radius of the sphere " << endl;
  cin >> sradius;
  cout << "Input the radius of the cylinder" << endl;
  cin >> cradius;
  if (cradius > sradius) {
    cout << " Problems" << endl;
    cout << " Cylinder to large to fit in the sphere" << endl;
    return;
  }
  cout << "Input the density of the sphere" << endl;
  cin>> dens1;
  cout << "Input the density of the cylinder" << endl;
  cin >> dens2;
  cout << "Input the number of MC tries per sample " << endl;
  cin >> NMCtries;
  cout << "Input the desired precision of the integration" << endl;
  cin >> precision;
}

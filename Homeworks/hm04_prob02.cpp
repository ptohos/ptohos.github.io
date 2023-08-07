#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

int main() {

  srand(time(NULL));
  int open_number, secret_number;
  int nloto, NWeeks2Sample;
  int atleastone, nwinners;
  int mxcase=2;
  double rnd;

  NWeeks2Sample = 500;  //arithmos ebdomadwn gia deigmatolipsia
  for (int icase=0; icase<mxcase; icase++) {
    atleastone = 0;
    nwinners = 0;
    if (icase==0) nloto = 1E4;
    if (icase==1) nloto = 1E7;
    for (int j = 0; j< NWeeks2Sample; j++){
      bool first = true; 
      for (int iloto = 0; iloto < nloto; iloto++){
	rnd = double(rand())/RAND_MAX;
	open_number = 1 + rnd*9998;         //o anoiktos arithmos
	rnd = double(rand())/RAND_MAX;
	secret_number = 1 + rnd*9998;       //o krufos arithmos 
	if (secret_number == open_number) {
	  if (first) {              // gia kathe deigma/week 1 nikitis 
	    first = false;
	    atleastone++;
	  }
	  nwinners++;
	} // 2 arithmoi idioi
      }// ws pros ta loto
    }// ws pros tis weeks=deigmata
    printf("Apotelesmata gia %8d lotos:\n",nloto);
    printf("O mesos oros nikitwn: %9.3f\n",double(nwinners)/NWeeks2Sample);
    printf("H pithanotita gia 1 toulaxiston nikiti: %8.5f\n",
	   double(atleastone)/NWeeks2Sample);
  } // periptwseis arithmou laxeiwn
}

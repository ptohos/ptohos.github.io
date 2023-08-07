#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

double convert_zero2pi(double angle){
  double temp = angle - int(angle/(2*M_PI))*2*M_PI ;
  return temp;
}
double convert_2rad(double angle){
  double temp = (angle/360.)*M_PI ;
  return temp;
}

double sin_sum(double angle, double epsi) {
  /*
    Paratiroume oti kathe neos oros tis seiras diaferei apo 
    ton proigoumeno kata -x**2/((2*i+1)*(2*i)). Gia paradeigma
    gia i=1 exoume -x**3/3!  enw gia i=2 exoume x**5/5! =x**3/3! * x**2/(4*5)
    Xrisimopoiontas ayti ti sxesi mporoume na ypologoisoume kathe neo oro
    pol/zontas ton proigoumeno me -x**2/((2i+1)*2i)
    O 1os oros gia i=0 einai x kai apotelei tin arxiko oro tou athroismatos
  */
  int nterm = 0;
  double sum = 0;
  double term = angle; 

  while (abs(term) > epsi) {
    nterm++;
    sum +=term;
    term = -term*angle*angle/(2*nterm*(2*nterm+1));
  }
  return sum;
}

double cos_sum(double angle,double epsi){
  /*
    Analoga me tin seira tou imitonou, proxwroume gia to cos.
    Kathe neos oros tis seiras diaferei apo 
    ton proigoumeno kata -x**2/((2*i-1)*(2*i)). Gia paradeigma
    gia i=3 exoume -x**6/6!  enw gia i=4 exoume x**8/8! =x**6/6! * x**2/(7*8)
    Xrisimopoiontas ayti ti sxesi mporoume na ypologoisoume kathe neo oro
    pol/zontas ton proigoumeno me -x**2/((2i-1)*2i)
    O 1os oros gia i=0 einai 1 kai apotelei tin arxiko oro tou athroismatos
  */

  int nterm = 0;
  double sum = 0;
  double term = 1; 

  while (abs(term) > epsi) {
    nterm++;
    sum +=term;
    term = -term*angle*angle/(2*nterm*(2*nterm-1));
  }
  return sum;
}
int main() {
  double angle, x, epsi;
  string degrad;
  cout << " Give the angle" << endl;
  cin >> angle;
  cout << " Radians or Degrees? [Insert rad or deg]" << endl;
  cin >> degrad;
  if (degrad == "rad") x = convert_zero2pi(angle);
  if (degrad == "deg") x = convert_2rad(angle);
  cout << " Insert desired precision" << endl;
  cin >> epsi;

  cout << "Gia tin seira toy imitonou exoyme" <<endl;
  cout << "=================================" << endl;
  cout << "Gia x = " << angle << " Sum = " << sin_sum(x,epsi) 
       << " kai sin(x) = " << sin(x) <<endl;

  cout << "Gia tin seira tou sunimitonou exoume"<<endl;
  cout << "====================================" << endl;
  cout << "Gia x = " << angle << " Sum = " << cos_sum(x,epsi) 
       << " kai cos(x) = " << cos(x) <<endl;


}

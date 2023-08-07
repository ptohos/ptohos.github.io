#include <iostream>
#include <fstream>
#include <cctype>
int count_character(char letter);

using namespace std;

int main() 
{
  char letter;

  cout.setf(ios::left);

  /* Typwnoume tis epikefalides toy pinaka */
  cout.width(19);
  cout << "Character";
  cout << "Frequency" << endl;
  for (int i=0; i<39; i++) cout << "-";
  cout << endl;
  /* Eyresi olwn twn grammatwn 
     Ta kefalaia grammata vriskontai 
     prin ta mikra kai epomenws an 
     thelate na breite ta grammata ayta
     to loop eprepe na einai 
     (letter='A'; letter <='z' ; letter++) */
  for (letter = 'a' ; letter <= 'z' ; letter++) {
    int ncount = count_character(letter);
    if (ncount < 0) break;
    cout.width(19);
    cout << letter << ncount<< endl;
  }
	
  return 0;
}

int count_character(char letter) {

  char character;
  ifstream in_stream;

  in_stream.open("lab03_prob04.cpp");
  if (in_stream.fail()) {
    cout << "Error opening file\n"; 
    return -1;
  }
  in_stream.get(character);
		
  int count = 0;
  // Metroume kathe gramma aneksartita an einai kefalaio i oxi
  // kai gia to logo ayto xreiazetai na eksetasoume gia kathe 
  // gramma an o xaraktiras einai to antistoixo kefalaio gramma
  // xrisimopoiwntas tin sunartisi toupper poy brisketai sto
  // header file cctype 
  while (! in_stream.fail()) {
    if (character == letter || character == toupper(letter)) count++;
    in_stream.get(character);
  }
  in_stream.close();
  
  return count;
}

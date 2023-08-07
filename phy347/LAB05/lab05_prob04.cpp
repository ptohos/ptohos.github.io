#include<iostream>

using namespace std;

// Class Declaration
class prime
{
 int a,k,i;
 public:
  prime(int);
  void calculate();
  void show();
};

prime::prime(int x){
  a=x;
}

void prime::calculate() {
 k=1;
 //{
   for (i=2; i<=a/2; i++)
     if(a%i==0) {
       k=0;
       break;
     }
     else{
       k=1;
     }
   // }
}

void prime::show() {
  if(k==1)
    cout<<"\n"<<a<<" is Prime Number.\n";
  else
    cout<<"\n"<<a<<" is Not Prime Numbers.\n";
}


int main()
{
  int a;
  cout<<"Enter the Number:";
  cin>>a;
  
  prime obj(a);
  obj.calculate();
  obj.show();
  return 0;
}

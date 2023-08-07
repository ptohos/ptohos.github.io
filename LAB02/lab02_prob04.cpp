#include<iostream>
#include<vector>
using namespace std;

int main()
{
  int n;
  cout<<"Enter the number: ";
  cin>>n;
  
  vector<int> prime(n+1,1);
  for(int i=2;i*i<=n;i++)
    {
      if(prime[i]==1)
	{
	  for(int j=i;i*j<=n;j++)
	    {
	      prime[i*j]=0;
	    }
	}
    }
  
  cout<<"Prime number upto "<<n<<" are: ";
  for(unsigned i=2;i<=prime.size();i++)
    {
      if(prime[i]==1)
	{
	  cout<<i<<" ";
	}
    }
  cout<<endl;
  
  return 0;
}

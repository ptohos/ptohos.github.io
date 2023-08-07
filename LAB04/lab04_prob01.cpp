#include<iostream>
#include<iomanip>
#include<cmath>

using namespace std;

void euler(float &x, float &y, float step); /* Euler function */
float deriv(float x, float y);  /*Derivative function*/

int main()
{
    float t0,x0,t,x,dt,tmax,k;
    printf("\nEnter t0,x0,dt,tmax: ");
    scanf("%f%f%f%f",&t0,&x0,&dt,&tmax);
    t=t0;
    x=x0;
    int nsteps = (tmax-t0)/dt;
    cout << "nsteps = " << nsteps << endl;

    printf("\n  t(s)\t  x(m)\n");
    while(t<=tmax)
    {
        printf("%0.3f\t%0.3f\n",t,x);
	euler(t,x,dt);
    }
}

void euler(float &x, float &y, float step)
{
  y = y + step*deriv(x,y);
  x = x + step;
}

  
float deriv(float x,float y) /* Derivative */
{
  float speed = 10.;
  return speed;
}

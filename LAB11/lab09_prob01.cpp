#include <iostream>
#include <iomanip>
#include <vector>
/* for a mac add this */
#include <Accelerate/Accelerate.h>

using namespace std;
int main() {
    char trans = 'N';
    int dim = 4;     int nrhs = 1;
    int LDA = dim; int LDB = dim;
    int info;

    int ipiv[4];
    vector<double> a, b;
    
    a.push_back(-2./3.);  a.push_back(+1./3.);  a.push_back(1.);  a.push_back(0.0000);
    a.push_back(+1./4.);  a.push_back(-3./4.);  a.push_back(1.);  a.push_back(+1./4.);
    a.push_back(+1./4.);  a.push_back(+1./4.);  a.push_back(1.);  a.push_back(+1./4.);
    a.push_back(0.);      a.push_back(+1./3.);  a.push_back(1.);  a.push_back(-2/3.); 

    b.push_back(0.); b.push_back(0.); b.push_back(1.); b.push_back(0.);

    cout << setw(6) << setprecision(4) << a[0] << " " << a[1] << " " << a[2] << " " << a[3] << endl; 
    cout << setw(6) << setprecision(4) << a[4] << " " << a[5] << " " << a[6] << " " << a[7] << endl; 
    cout << setw(6) << setprecision(4) << a[8] << " " << a[9] << " " << a[10] << " " << a[11] << endl; 
    cout << setw(6) << setprecision(4) << a[12] << " " << a[13] << " " << a[14] << " " << a[15] << endl; 

    dgetrf_(&dim, &dim, & a[0], &LDA, ipiv, &info);
    dgetrs_(&trans, &dim, &nrhs, & a[0], &LDA, ipiv, & b[0], &LDB, &info);
    std::cout << "solution is:";    
    std::cout << "["  << b[0] << ", " << b[1] << ", " << b[2] << ", " << b[3] << "]" << std::endl;
    std::cout << "Info = " << info << std::endl;

    return 0;
}

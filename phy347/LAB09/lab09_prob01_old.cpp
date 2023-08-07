#include <iostream>
#include <vector>
/* for a mac add this */
#include <Accelerate/Accelerate.h>

using namespace std;
int main() {
    char trans = 'N';
    int dim = 5;     int nrhs = 1;
    int LDA = dim; int LDB = dim;
    int info;

    int ipiv[5];
    vector<double> a, b;
    a.push_back(2); a.push_back(-1); a.push_back(0); a.push_back(0); a.push_back(0);
    a.push_back(-1); a.push_back(2); a.push_back(-1);a.push_back(0); a.push_back(0);
    a.push_back(0); a.push_back(-1); a.push_back(2);a.push_back(-1); a.push_back(0);
    a.push_back(0); a.push_back(0); a.push_back(-1);a.push_back(2); a.push_back(-1);
    a.push_back(0); a.push_back(0); a.push_back(0);a.push_back(-1); a.push_back(2);
    b.push_back(2.77778); b.push_back(0.524654); b.push_back(0.0990944); 
    b.push_back(0.0187165); b.push_back(0.00353509);
    /*
    dgetrf_(&dim, &dim, & *a.begin(), &LDA, ipiv, &info);
    dgetrs_(&trans, &dim, &nrhs, & *a.begin(), &LDA, ipiv, & *b.begin(), &LDB, &info);
    */
    dgetrf_(&dim, &dim, & a[0], &LDA, ipiv, &info);
    dgetrs_(&trans, &dim, &nrhs, & a[0], &LDA, ipiv, & b[0], &LDB, &info);
    std::cout << "solution is:";    
    std::cout << "["  << b[0] << ", " << b[1] << ", " << b[2] 
              << ", " << b[3] << ", " << b[4] << "]" << std::endl;
    std::cout << "Info = " << info << std::endl; 

    double aa[5][5] = {{ 2, -1,  0,  0,  0}, 
                       {-1,  2, -1,  0,  0},
                       { 0, -1,  2, -1,  0},
                       { 0,  0, -1,  2, -1},
                       { 0,  0,  0, -1,  2}};
    double bb[1][5] = {2.77778, 0.524654, 0.0990944, 0.0187165, 0.00353509};

    dgetrf_(&dim, &dim, &aa[0][0], &LDA, ipiv, &info);
    dgetrs_(&trans, &dim, &nrhs, &aa[0][0], &LDA, ipiv, &bb[0][0], &LDB, &info);

    std::cout << "solution is:";    
    std::cout << "[" << bb[0][0] << ", " << bb[0][1] << ", " << bb[0][2]
              << ", " << bb[0][3] << ", " << bb[0][4] << "]" << std::endl;
    std::cout << "Info = " << info << std::endl; 
    
    return 0;
}

#include <iostream>
#include <vector>
/* for a mac add this */
#include <Accelerate/Accelerate.h>

using namespace std;
int main() {
    char trans = 'N';
    int dim = 4;     int nrhs = 1;
    int LDA = dim; int LDB = dim;
    int info;
    double aa[4][4], bb[4][1];
    int ipiv[4];
    
    char JOBVL, JOBVR; 
    int N = 4;      // order of matrix A
    int LDAB = 4;   // leading dimension of A (column or raw)
    double WR[4];   // real values of eigenvectorvalues
    double WI[4];   // imaginary values of eigenvalues
    int    LDVL = 4; // for left eigenvectors
    double VL[4][4];
    int    LDVR = 4; // for right eigenvectors
    double VR[4][4];
    int    LWORK=32;
    double WORK[32]; // at least 4xN
    int    INFO;
    vector<double> vaa,vbb;
    
    JOBVL = 'V';  // do not calculate Left eigenvectors
    JOBVR = 'V';  // calculate right eigenvectors

    // Right transition 
    vaa.push_back(-0.6667); vaa.push_back(0.3333); vaa.push_back(0.3333); vaa.push_back(0.);
    vaa.push_back(1.); vaa.push_back( 1.); vaa.push_back( 1.); vaa.push_back(1.);
    vaa.push_back( 0.25); vaa.push_back(0.25); vaa.push_back(-0.75); vaa.push_back( 0.25);
    vaa.push_back(    0.);  vaa.push_back(0.3333); vaa.push_back( 0.3333); vaa.push_back(-0.6667);
    vbb.push_back(0.); vbb.push_back(1.); vbb.push_back(0.) ; vbb.push_back(0.);
    /*
    double RR[4][4] = {{1./3.,  1./4.,  1./4.,  0.},
		       {1./3.,  1./4.,  1./4.,  1./3.}, 
                       {1./3.,  1./4.,  1./4.,  1./3.},
                       {0.,     1./4.,  1./4.,  1./3.}};

    for (int i=0; i<4; i++){
      for (int j=0; j<4; j++){
	aa[i][j] = RR[i][j];
	if (i == j) aa[i][j]-= 1.;
	if (j == 0) aa[i][j] = 1.;
	vaa.push_back(aa[i][j]);
	
	if (j == 0) {
	  bb[i][j] = 0.;
	  if (i==0) bb[i][j] = 1.;
	  vbb.push_back(bb[i][j]);
	}
      }
      cout << aa[i][0] << " " << aa[i][1] << " " << aa[i][2] << " " << aa[i][3] << endl;
    }
    cout << bb[0][0] << " " << bb[1][0] << " " << bb[2][0] << "  " << bb[3][0] << endl;
    */
    dgetrf_(&dim, &dim, &vaa[0], &LDA, ipiv, &info);
    dgetrs_(&trans, &dim, &nrhs, &vaa[0], &LDA, ipiv, &vbb[0], &LDB, &info);
    std::cout << "Solutions" << endl;
    for (int i = 0; i<4; i++) {	
      std::cout << "[" << vbb[i] << "]" << std::endl;
      /*     
		<< ", " << bb[i][0] << ", " << bb[i][0]
                << ", " << bb[i][0] << "]" << std::endl;
      */
    }
   
    /*
    dgeev_(&JOBVL,&JOBVR,&N,&RR[0][0],&LDAB,&WR[0],&WI[0],
	   &VL[0][0],&LDVL,&VR[0][0],&LDVR,&WORK[0],&LWORK,&INFO);

    std::cout << "Right Eigenvectors " << std::endl;
    for (int i = 0; i<4; i++) {	
      std::cout << "[" << VR[i][0] << ", " << VR[i][0] << ", " << VR[i][0]
              << ", " << VR[i][0] << "]" << std::endl;
    }
    std::cout << "Left Eigenvectors " << std::endl;
    for (int i = 0; i<4; i++) {	
      std::cout << "[" << VL[i][0] << ", " << VL[i][1] << ", " << VL[i][2]
		<< ", " << VL[i][3] << "]" << std::endl;
    }
    std::cout << " Eigenvalues" << std::endl;
    std::cout << "[" << WR[0] << " " << WR[1] << " " << WR[2] << " " << WR[3] << "]" << std::endl;

    cout << "Total probability" << VR[0][0]+VR[1][0]+VR[2][0]+VR[3][0] << endl;


    // For left eigenvector calculation
    JOBVL = 'V';
    JOBVR = 'V';
    double LL[4][4] =  {{1./3.,  1./3.,  1./3., 0.},
			{1./4.,  1./4.,  1./4., 1./4.}, 
			{1./4.,  1./4.,  1./4., 1./4.},
			{0.,     1./4.,  1./4., 1./3.}};

    dgeev_(&JOBVL,&JOBVR,&N,&LL[0][0],&LDAB,&WR[0],&WI[0],
	   &VL[0][0],&LDVL,&VR[0][0],&LDVR,&WORK[0],&LWORK,&INFO);
    std::cout << "Info = " << info << std::endl; 
    std::cout << "Right Eigenvectors " << std::endl;
    for (int i = 0; i<4; i++) {	
      std::cout << "[" << VR[i][0] << ", " << VR[i][0] << ", " << VR[i][0]
              << ", " << VR[i][0] << "]" << std::endl;
    }
    std::cout << "Left Eigenvectors " << std::endl;
    for (int i = 0; i<4; i++) {	
      std::cout << "[" << VL[i][0] << ", " << VL[i][1] << ", " << VL[i][2]
		<< ", " << VL[i][3] << "]" << std::endl;
    }
    cout << "Total probability" << VL[0][0]+VL[0][1]+VL[0][2]+VL[0][3] << endl;
    
    std::cout << " Eigenvalues" << std::endl;
    std::cout << "[" << WR[0] << " " << WR[1] << " " << WR[2] << " " << WR[3] << "]" << std::endl;

    */    
    return 0;
}

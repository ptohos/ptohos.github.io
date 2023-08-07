// rnd_walk1.cxx
// Random walk in one dimension
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include "TROOT.h"
#include "TTree.h" // we will use a tree to store our values
#include "TApplication.h"
#include "TFile.h"

int rand(void);
void srand(unsigned int);

//void main(int argc, char **argv) {
void hm04_prob02(){
//structure for our random walk variables
  struct walk_t {
    int x; // the position after a step
    int nstep; // the step number
    int left; // number of steps to the left
    int right; // number of steps to the right
    int jloop; // number of outer loops
  };
  
  walk_t walk;
  int i_loop; //inner loop
  int j_loop; //outer loop
  int jloop_max=5000; // the max number of different trials
  unsigned int seed = 68910 ; // here is the starting value or seed
  int loop_max=100; // the maximum number of steps
  double rnd;
  TROOT root("hello", "computational physics");
  TFile *out_file = new TFile("rnd_walk68910.root","RECREATE"); // create root file
  // Declare tree
  TTree*ran_walk = new TTree("ran_walk", "tree with random walk variables");
  ran_walk->Branch("walk",&walk.x,"x/I:nstep/I:left/I:right/I:jloop/I");
  //set seed value
  srand(seed);
  // the outer loop, trying the walk jloop times
  for(j_loop=0;j_loop < jloop_max ;j_loop= j_loop+1) {
    walk.x=0;
    walk.nstep=0;
    walk.left=0;
    walk.right=0;
    walk.jloop=j_loop+1;
    for(i_loop=0;i_loop < loop_max ;i_loop= i_loop+1) {
      // here we get the step
      rnd=double(rand())/double(RAND_MAX);
      if((rnd-.5)<=0.)
	{
	  walk.x=walk.x-1;
	  walk.left=walk.left+1;
	}
      else
	{
	  walk.x=walk.x+1;
	  walk.right=walk.right+1;
	}
      walk.nstep=walk.nstep+1;
      // fill the tree
      ran_walk->Fill();
    }
  }
  out_file->Write();
}

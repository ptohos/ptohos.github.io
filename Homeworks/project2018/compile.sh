#!/bin/bash

echo "Compiling Pythia..."
gfortran -c -m64 -fPIC pythia-6.4.28.f
echo "Compiling main..."
gfortran -c -m64 -fPIC main.f
echo "Linking..."
gfortran  -Wall main.o pythia-6.4.28.o -o run_pythia.x


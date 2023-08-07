#! /bin/bash

# C-x C-m f gia metatropi apo dos se unix
sudo apt-get install git cmake dpkg-dev python-dev make g++ gcc binutils \
             libx11-dev libxpm-dev libxft-dev libxext-dev \
       	     gfortran libssl-dev libpcre3-dev xlibmesa-glu-dev \
       	     libglew1.5-dev libftgl-dev libmysqlclient-dev \
       	     libfftw3-dev libcfitsio-dev graphviz-dev \
             libavahi-compat-libdnssd-dev \
       	     libldap2-dev libxml2-dev libkrb5-dev libgsl0-dev libqt4-dev

echo "Installing root..."
RootVersion=v6-16-00
echo "version: " ${RootVersion}
sudo mkdir /usr/local/Codes
sudo mkdir /usr/local/Codes/root
MyRoot=/usr/local/Codes/root
cd $MyRoot
sudo git clone http://github.com/root-project/root.git src_${RootVersion}
cd src_${RootVersion}
sudo git checkout -b ${RootVersion} ${RootVersion}
cd ${MyRoot}
sudo mkdir ${RootVersion}       # you need to build it in a different directory
cd ${RootVersion}
sudo cmake ${MyRoot}/src_${RootVersion} -DRooFit=ON -Dminuit2=ON -Dbuiltin_fftw3=ON
sudo cmake --build . -- -j4       # watch the . after the build



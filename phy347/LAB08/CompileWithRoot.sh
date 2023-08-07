g++ -I `root-config --incdir` $1 `root-config --cflags --libs` \
    -L $ROOTSYS/lib -lHtml -lMinuit -lMathCore -o $2

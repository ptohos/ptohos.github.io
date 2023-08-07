# Makefile for pythia examples

FF = gfortran

# this is ok with gfortran from fink

#FFLAGS = -g -static -w -fno-second-underscore

# For MAC: use the following FFLAGS
FFLAGS = -gdwarf-2 -static -w -fno-second-underscore

OBJS = main.o ../pythia-6.4.28.o EXEC = pythia.x

all: $(EXEC)

$(EXEC): $(OBJS)
	$(FF) -o $(EXEC) $(OBJS) $(LIB)

.f.o: $(FF) $(FFLAGS) -c $<

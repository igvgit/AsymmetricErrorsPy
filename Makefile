# Edit the following two variables so that they describe where the "ase"
# package is installed on your computer. You should be able to find the files
# $ASE_INCLUDE_DIR/ase/AbsDistributionModel1D.hh and $ASE_LIB_DIR/libase.so
ASE_INCLUDE_DIR = /usr/local/include
ASE_LIB_DIR = /usr/local/lib

PYTHON_TOPDIR := $(shell python3 -c "import sys; print(sys.prefix)")
PYTHON_VERSION := $(shell python3 -c "import sys; print('%d.%d' % sys.version_info[0:2])")
PYTHON_INCLUDE_DIR = $(PYTHON_TOPDIR)/include/python$(PYTHON_VERSION)m
PYTHON_INCLUDE_DIR2 = $(PYTHON_TOPDIR)/include/python$(PYTHON_VERSION)
NUMPY_INCLUDE_DIR := $(shell python3 -c "import numpy; print(numpy.get_include())")

CPPFLAGS = -I. -I$(ASE_INCLUDE_DIR) -I$(PYTHON_INCLUDE_DIR) -I$(PYTHON_INCLUDE_DIR2) -I$(NUMPY_INCLUDE_DIR) -DSWIG -Wno-unused-parameter
LIBS = -L$(ASE_LIB_DIR) -lase -lm

OFILES = ase_wrap.o RandomGenerators.o

%.o : %.cc
	g++ -std=c++11 -c $(CPPFLAGS) -fPIC -MD $< -o $@
	@sed -i 's,\($*\.o\)[:]*\(.*\),$@: $$\(wildcard\2\)\n\1:\2,g' $*.d

all: _asepy.so

_asepy.so: $(OFILES)
	g++ -std=c++11 -shared -o $@ $^ $(LIBS)

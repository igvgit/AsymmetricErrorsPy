# Edit the following variable so that it describes where the "ase" package
# is installed on your computer. You should be able to find the file
# $ASE_INCLUDE_DIR/ase/AbsDistributionModel1D.hh
ASE_INCLUDE_DIR = /usr/local/include

all: ase_wrap.cc

ase_wrap.cc:
	swig -I. -I$(ASE_INCLUDE_DIR) -python -py3 -c++ -o ase_wrap.cc asepy.i

clean:
	rm -fr _asepy.so *.pyc __pycache__ core.* *.o *.d *~ */*~ .deps .libs

distclean:
	rm -fr _asepy.so ase_wrap.cc asepy.py *.pyc __pycache__ core.* *.o *.d *~ */*~ .deps .libs

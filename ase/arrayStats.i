%include stddecls.i

%{
#include "ase/arrayStats.hh"
%}

%apply (double* IN_ARRAY1, int DIM1) {
    (const double* arr, const unsigned sz)
}

%ignore ase::arrayCumulants;
%rename(arrayCumulants) ase::swigArrayCumulants;

%include "ase/arrayStats.hh"

%clear (const double* arr, const unsigned sz);

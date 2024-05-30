%include ase/AbsLocationScaleFamily.i

%{
#include "ase/Gaussian.hh"
%}

%feature("notabstract") ase::Gaussian;

%include "ase/Gaussian.hh"

%include ase/AbsLogLikelihoodCurve.i

%{
#include "ase/PoissonLogli.hh"
%}

%feature("notabstract") ase::PoissonLogli;

%include "ase/PoissonLogli.hh"

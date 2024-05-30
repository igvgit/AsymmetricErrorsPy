%include ase/AbsDistributionModel1D.i

%{
#include "ase/MixtureModel1D.hh"
%}

%feature("notabstract") ase::MixtureModel1D;

%include "ase/MixtureModel1D.hh"

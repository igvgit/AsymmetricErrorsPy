%include ase/AbsDistributionModel1D.i

%{
#include "ase/DistributionModel1DCopy.hh"
%}

%feature("notabstract") ase::DistributionModel1DCopy;

%include "ase/DistributionModel1DCopy.hh"

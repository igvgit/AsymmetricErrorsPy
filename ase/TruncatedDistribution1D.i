%include ase/AbsDistributionModel1D.i

%{
#include "ase/TruncatedDistribution1D.hh"
%}

%feature("notabstract") ase::TruncatedDistribution1D;

%include "ase/TruncatedDistribution1D.hh"

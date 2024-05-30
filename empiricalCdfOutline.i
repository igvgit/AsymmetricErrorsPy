%include numpy.i
%include ase/DistributionModels1D.i

%{
#include "empiricalCdfOutline.hh"
%}

namespace asepy {
    %newobject empiricalCdfOutline;
}

%include "empiricalCdfOutline.hh"

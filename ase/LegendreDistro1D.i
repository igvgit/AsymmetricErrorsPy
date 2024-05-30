%include stddecls.i
%include ase/AbsLocationScaleFamily.i

%{
#include "ase/LegendreDistro1D.hh"
%}

%feature("notabstract") ase::LegendreDistro1D;

%include "ase/LegendreDistro1D.hh"

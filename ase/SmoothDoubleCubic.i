%include stddecls.i

%{
#include "ase/SmoothDoubleCubic.hh"
%}

%include "ase/SmoothDoubleCubic.hh"

namespace ase {
    %template(SmoothDoubleCubic) SmoothDoubleCubic<double>;
    %template(SDCZoneFunctor) SDCZoneFunctor<double>;
    %template(LDSmoothDoubleCubic) SmoothDoubleCubic<long double>;
    %template(LDSDCZoneFunctor) SDCZoneFunctor<long double>;
}

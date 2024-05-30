%include stddecls.i

%{
#include "ase/SymbetaDoubleIntegral.hh"
%}

%include "ase/SymbetaDoubleIntegral.hh"

namespace ase {
    %template(SymbetaDoubleIntegral) SymbetaDoubleIntegral<double>;
    %template(SDIZoneFunctor) SDIZoneFunctor<double>;
    %template(LDSymbetaDoubleIntegral) SymbetaDoubleIntegral<long double>;
    %template(LDSDIZoneFunctor) SDIZoneFunctor<long double>;
}

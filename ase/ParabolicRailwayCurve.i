%include stddecls.i

%{
#include "ase/ParabolicRailwayCurve.hh"
%}

%include "ase/ParabolicRailwayCurve.hh"

namespace ase {
    %template(ParabolicRailwayCurve) ParabolicRailwayCurve<double>;
    %template(RailwayZoneFunctor) RailwayZoneFunctor<double>;
    %template(LDParabolicRailwayCurve) ParabolicRailwayCurve<long double>;
    %template(LDRailwayZoneFunctor) RailwayZoneFunctor<long double>;
}

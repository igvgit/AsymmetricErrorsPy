%include ase/Gaussian.i
%include ase/SymbetaDoubleIntegral.i
%include ase/ParabolicRailwayCurve.i
%include ase/SmoothDoubleCubic.i

%{
#include "ase/OPATGaussian.hh"
%}

%include "ase/OPATGaussian.hh"

namespace ase {
    %template(OPATGaussian0) OPATGaussian<SymbetaDoubleIntegral<long double> >;
    %template(OPATGaussian1) OPATGaussian<ParabolicRailwayCurve<long double> >;
    %template(OPATGaussian2) OPATGaussian<SmoothDoubleCubic<long double> >;
}

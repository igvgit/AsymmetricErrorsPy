%include ase/AbsLogLikelihoodCurve.i
%include PyFunctor1.i

%{
#include "ase/CubicHermiteInterpolatorEG.hh"
%}

%feature("notabstract") ase::CubicHermiteInterpolatorEG;

%include "ase/CubicHermiteInterpolatorEG.hh"

namespace ase {
    %extend CubicHermiteInterpolatorEG {
         %template(CubicHermiteInterpolatorEG) CubicHermiteInterpolatorEG<asepy::PyFunctor1>;
         %template(CubicHermiteInterpolatorEG) CubicHermiteInterpolatorEG<asepy::PyFunctor1,asepy::PyFunctor1>;
    } 
}

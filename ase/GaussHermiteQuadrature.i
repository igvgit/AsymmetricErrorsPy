%include PyFunctor1.i
%include ase/DistributionFunctors1D.i
%include ase/FunctorTimesShiftedX.i

%{
#include "ase/GaussHermiteQuadrature.hh"
%}

%ignore ase::GaussHermiteQuadrature::getAllAbscissae;
%ignore ase::GaussHermiteQuadrature::getAllWeights;

%include "ase/GaussHermiteQuadrature.hh"

namespace ase {
    %extend GaussHermiteQuadrature {
         %template(integrateProb) integrateProb2<RatioMomentFunctor1D>;
         %template(integrateProb) integrateProb2<asepy::PyFunctor1>;
         %template(integrateProb) integrateProb2<FunctorTimesShiftedXRatioHelper<NumericalConvolution> >;
         %template(integrateProb) integrateProb2<FunctorTimesShiftedXRatioHelper<GaussianConvolution> >;
         %template(integrate)     integrate2<asepy::PyFunctor1>;
    }
}

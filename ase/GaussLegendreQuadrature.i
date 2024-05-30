%include PyFunctor1.i
%include ase/DistributionFunctors1D.i
%include ase/FunctorTimesShiftedX.i

%{
#include "ase/GaussLegendreQuadrature.hh"
%}

%ignore ase::GaussLegendreQuadrature::getAllAbscissae;
%ignore ase::GaussLegendreQuadrature::getAllWeights;

%include "ase/GaussLegendreQuadrature.hh"

namespace ase {
    %extend GaussLegendreQuadrature {
         %template(integrate) integrate2<MomentFunctor1D>;
         %template(integrate) integrate2<asepy::PyFunctor1>;
         %template(integrate) integrate2<FunctorTimesShiftedXHelper<NumericalConvolution> >;
         %template(integrate) integrate2<FunctorTimesShiftedXHelper<GaussianConvolution> >;
    }
}

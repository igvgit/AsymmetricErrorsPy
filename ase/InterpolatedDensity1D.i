%include ase/AbsLocationScaleFamily.i
%include ase/NumericalConvolution.i
%include ase/GaussianConvolution.i
%include ase/DistributionFunctors1D.i
%include PyFunctor1.i

%{
#include "ase/InterpolatedDensity1D.hh"
%}

%feature("notabstract") ase::InterpolatedDensity1D;

%include "ase/InterpolatedDensity1D.hh"

namespace ase {
    %extend InterpolatedDensity1D {
         %template(InterpolatedDensity1D) InterpolatedDensity1D<asepy::PyFunctor1>;
         %template(InterpolatedDensity1D) InterpolatedDensity1D<asepy::PyFunctor1,asepy::PyFunctor1>;
         %template(InterpolatedDensity1D) InterpolatedDensity1D<NumericalConvolution>;
         %template(InterpolatedDensity1D) InterpolatedDensity1D<GaussianConvolution>;
         %template(InterpolatedDensity1D) InterpolatedDensity1D<DensityFunctor1D>;
    }
}

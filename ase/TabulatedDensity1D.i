%include ase/AbsLocationScaleFamily.i
%include ase/NumericalConvolution.i
%include ase/GaussianConvolution.i
%include ase/DistributionFunctors1D.i
%include PyFunctor1.i

%{
#include "ase/TabulatedDensity1D.hh"
%}

%feature("notabstract") ase::TabulatedDensity1D;

%include "ase/TabulatedDensity1D.hh"

namespace ase {
    %extend TabulatedDensity1D {
         %template(TabulatedDensity1D) TabulatedDensity1D<asepy::PyFunctor1>;
         %template(TabulatedDensity1D) TabulatedDensity1D<NumericalConvolution>;
         %template(TabulatedDensity1D) TabulatedDensity1D<GaussianConvolution>;
         %template(TabulatedDensity1D) TabulatedDensity1D<DensityFunctor1D>;
    }
}

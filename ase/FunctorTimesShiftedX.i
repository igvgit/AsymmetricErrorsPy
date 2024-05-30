%include ase/AbsDistributionModel1D.i
%include ase/NumericalConvolution.i
%include ase/GaussianConvolution.i

%{
#include "ase/FunctorTimesShiftedX.hh"
%}

%include "ase/FunctorTimesShiftedX.hh"

namespace ase {
    %template(FunctorTimesShiftedXHelperNConv) FunctorTimesShiftedXHelper<NumericalConvolution>;
    %template(FunctorTimesShiftedX) FunctorTimesShiftedX<NumericalConvolution>;

    %template(FunctorTimesShiftedXHelperGConv) FunctorTimesShiftedXHelper<GaussianConvolution>;
    %template(FunctorTimesShiftedX) FunctorTimesShiftedX<GaussianConvolution>;

    %template(FunctorTimesShiftedXRatioHelperNConv) FunctorTimesShiftedXRatioHelper<NumericalConvolution>;
    %template(FunctorTimesShiftedXRatio) FunctorTimesShiftedXRatio<NumericalConvolution>;

    %template(FunctorTimesShiftedXRatioHelperGConv) FunctorTimesShiftedXRatioHelper<GaussianConvolution>;
    %template(FunctorTimesShiftedXRatio) FunctorTimesShiftedXRatio<GaussianConvolution>;
}

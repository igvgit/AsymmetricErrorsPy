%include PyFunctor1.i

%include ase/DistributionFunctors1D.i
%include ase/NumericalConvolution.i
%include ase/GaussianConvolution.i
%include ase/DiscretizedConvolution.i
%include ase/DoubleFunctor1.i
%include ase/AbsLogLikelihoodCurve.i
%include ase/DerivativeFunctors.i
%include ase/DoubleCubicInner.i
%include ase/ParabolicRailwayCurve.i
%include ase/SmoothDoubleCubic.i
%include ase/SymbetaDoubleIntegral.i

%{
#include "scanFunctor1D.hh"
%}

namespace asepy {
    %newobject scanFunctor1D;
}

%apply (double* IN_ARRAY1, int DIM1) {
    (const double* coords, const unsigned npoints)
}

%include "scanFunctor1D.hh"

namespace asepy {
    %template(scanFunctor1D) scanFunctor1D<ase::DensityFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::DensityDerivativeFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::LogDensityFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::ShiftedDensityFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::CdfFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::ExceedanceFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::InvExceedanceFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::QuantileFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::EntropyFunctor1D>;
    %template(scanFunctor1D) scanFunctor1D<ase::NumericalConvolution>;
    %template(scanFunctor1D) scanFunctor1D<ase::GaussianConvolution>;
    %template(scanFunctor1D) scanFunctor1D<ase::DiscretizedConvolution>;
    %template(scanFunctor1D) scanFunctor1D<ase::DoubleFunctor1>;
    %template(scanFunctor1D) scanFunctor1D<ase::AbsLogLikelihoodCurve>;
    %template(scanFunctor1D) scanFunctor1D<ase::LogLikelihoodDerivative>;
    %template(scanFunctor1D) scanFunctor1D<ase::LogLikelihoodSecondDerivative>;

    %template(scanFunctor1D) scanFunctor1D<ase::TransitionCubic<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::TransitionCubic<double> > >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::TransitionCubic<double> > >;

    %template(scanFunctor1D) scanFunctor1D<ase::ParabolicRailwayCurve<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::RailwayZoneFunctor<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::ParabolicRailwayCurve<double> > >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::ParabolicRailwayCurve<double> > >;

    %template(scanFunctor1D) scanFunctor1D<ase::SmoothDoubleCubic<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::SDCZoneFunctor<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::SmoothDoubleCubic<double> > >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::SmoothDoubleCubic<double> > >;

    %template(scanFunctor1D) scanFunctor1D<ase::SymbetaDoubleIntegral<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::SDIZoneFunctor<double> >;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::SymbetaDoubleIntegral<double> > >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::SymbetaDoubleIntegral<double> > >;

    %template(scanFunctor1D) scanFunctor1D<ase::DoubleCubicInner>;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::DoubleCubicInner> >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::DoubleCubicInner> >;

    %template(scanFunctor1D) scanFunctor1D<ase::QuinticInner>;
    %template(scanFunctor1D) scanFunctor1D<ase::DerivativeFunctorHelper<ase::QuinticInner> >;
    %template(scanFunctor1D) scanFunctor1D<ase::SecondDerivativeFunctorHelper<ase::QuinticInner> >;

    %template(scanFunctor1D) scanFunctor1D<asepy::PyFunctor1>;
}

%clear (const double* coords, const unsigned npoints);

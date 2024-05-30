%include ase/TransitionCubic.i
%include ase/ParabolicRailwayCurve.i
%include ase/DoubleCubicInner.i
%include ase/SmoothDoubleCubic.i
%include ase/QuinticInner.i
%include ase/SymbetaDoubleIntegral.i

%{
#include "ase/DerivativeFunctors.hh"
%}

%include "ase/DerivativeFunctors.hh"

namespace ase {
    %template(DerivativeFunctorHelper_TransitionCubic) DerivativeFunctorHelper<TransitionCubic<double> >;
    %template(DerivativeFunctor) DerivativeFunctor<TransitionCubic<double> >;

    %template(SecondDerivativeFunctorHelper_TransitionCubic) SecondDerivativeFunctorHelper<TransitionCubic<double> >;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<TransitionCubic<double> >;

    %template(DerivativeFunctorHelper_ParabolicRailwayCurve) DerivativeFunctorHelper<ParabolicRailwayCurve<double> >;
    %template(DerivativeFunctor) DerivativeFunctor<ParabolicRailwayCurve<double> >;

    %template(SecondDerivativeFunctorHelper_ParabolicRailwayCurve) SecondDerivativeFunctorHelper<ParabolicRailwayCurve<double> >;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<ParabolicRailwayCurve<double> >;

    %template(DerivativeFunctorHelper_SmoothDoubleCubic) DerivativeFunctorHelper<SmoothDoubleCubic<double> >;
    %template(DerivativeFunctor) DerivativeFunctor<SmoothDoubleCubic<double> >;

    %template(SecondDerivativeFunctorHelper_SmoothDoubleCubic) SecondDerivativeFunctorHelper<SmoothDoubleCubic<double> >;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<SmoothDoubleCubic<double> >;

    %template(DerivativeFunctorHelper_SymbetaDoubleIntegral) DerivativeFunctorHelper<SymbetaDoubleIntegral<double> >;
    %template(DerivativeFunctor) DerivativeFunctor<SymbetaDoubleIntegral<double> >;

    %template(SecondDerivativeFunctorHelper_SymbetaDoubleIntegral) SecondDerivativeFunctorHelper<SymbetaDoubleIntegral<double> >;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<SymbetaDoubleIntegral<double> >;

    %template(DerivativeFunctorHelper_DoubleCubicInner) DerivativeFunctorHelper<DoubleCubicInner>;
    %template(DerivativeFunctor) DerivativeFunctor<DoubleCubicInner>;

    %template(SecondDerivativeFunctorHelper_DoubleCubicInner) SecondDerivativeFunctorHelper<DoubleCubicInner>;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<DoubleCubicInner>;

    %template(DerivativeFunctorHelper_QuinticInner) DerivativeFunctorHelper<QuinticInner>;
    %template(DerivativeFunctor) DerivativeFunctor<QuinticInner>;

    %template(SecondDerivativeFunctorHelper_QuinticInner) SecondDerivativeFunctorHelper<QuinticInner>;
    %template(SecondDerivativeFunctor) SecondDerivativeFunctor<QuinticInner>;
}

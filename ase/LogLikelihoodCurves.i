%include ase/AbsShiftableLogli.i

%{
#include "ase/LogLikelihoodCurves.hh"
%}

%feature("notabstract") ase::SymmetrizedParabola;
%feature("notabstract") ase::BrokenParabola;
%feature("notabstract") ase::TruncatedCubicLogli;
%feature("notabstract") ase::LogarithmicLogli;
%feature("notabstract") ase::GeneralisedPoisson;
%feature("notabstract") ase::ConstrainedQuartic;
%feature("notabstract") ase::MoldedQuartic;
%feature("notabstract") ase::MatchedQuintic;
%feature("notabstract") ase::MoldedDoubleQuartic;
%feature("notabstract") ase::SimpleDoubleQuartic;
%feature("notabstract") ase::MoldedDoubleQuintic;
%feature("notabstract") ase::SimpleDoubleQuintic;
%feature("notabstract") ase::Interpolated7thDegree;
%feature("notabstract") ase::VariableSigmaLogli;
%feature("notabstract") ase::VariableVarianceLogli;
%feature("notabstract") ase::VariableLogSigma;
%feature("notabstract") ase::MoldedCubicLogSigma;
%feature("notabstract") ase::QuinticLogSigma;
%feature("notabstract") ase::PDGLogli;
%feature("notabstract") ase::LogLogisticBeta;
%feature("notabstract") ase::DistributionLogli;
%feature("notabstract") ase::ConservativeSpline;
%feature("notabstract") ase::ConservativeSigma05;
%feature("notabstract") ase::ConservativeSigma10;
%feature("notabstract") ase::ConservativeSigma15;
%feature("notabstract") ase::ConservativeSigma20;
%feature("notabstract") ase::ConservativeSigmaMax;

%include "ase/LogLikelihoodCurves.hh"

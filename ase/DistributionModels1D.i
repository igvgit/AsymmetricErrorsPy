%include ase/OPATGaussian.i
%include ase/ParabolicRailwayCurve.i
%include ase/SmoothDoubleCubic.i

%{
#include "ase/DistributionModels1D.hh"
%}

%feature("notabstract") ase::DimidiatedGaussian;
%feature("notabstract") ase::DistortedGaussian;
%feature("notabstract") ase::RailwayGaussian;
%feature("notabstract") ase::DoubleCubicGaussian;
%feature("notabstract") ase::SkewNormal;
%feature("notabstract") ase::QVWGaussian;
%feature("notabstract") ase::LogNormal;
%feature("notabstract") ase::JohnsonSu;
%feature("notabstract") ase::JohnsonSb;
%feature("notabstract") ase::JohnsonSystem;
%feature("notabstract") ase::EdgeworthExpansion3;
%feature("notabstract") ase::GammaDistribution;
%feature("notabstract") ase::EmpiricalDistribution;
%feature("notabstract") ase::FechnerDistribution;
%feature("notabstract") ase::UniformDistribution;
%feature("notabstract") ase::ExponentialDistribution;

%ignore ase::EmpiricalDistribution::sample;

%include "ase/DistributionModels1D.hh"

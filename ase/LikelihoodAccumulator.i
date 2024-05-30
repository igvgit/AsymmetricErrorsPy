%include ase/AbsLogLikelihoodCurve.i

%{
#include "ase/LikelihoodAccumulator.hh"
%}

%feature("notabstract") ase::LikelihoodAccumulator;

%rename(__iadd__) ase::LikelihoodAccumulator::operator+=;
%rename(__isub__) ase::LikelihoodAccumulator::operator-=;

%ignore ase::LikelihoodAccumulator::operator[];
%ignore ase::LikelihoodAccumulator::at;

%include "ase/LikelihoodAccumulator.hh"

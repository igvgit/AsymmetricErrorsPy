%include stddecls.i

%{
#include "ase/LikelihoodCurveCopy.hh"
%}

%rename(__call__) ase::AbsLogLikelihoodCurve::operator();
%rename(__call__) ase::LogLikelihoodDerivative::operator();
%rename(__call__) ase::LogLikelihoodSecondDerivative::operator();
%rename(__call__) ase::LikelihoodCurveCopy::operator();

%rename(__idiv__) ase::AbsLogLikelihoodCurve::operator/=;
%rename(__imul__) ase::AbsLogLikelihoodCurve::operator*=;

%feature("notabstract") ase::LikelihoodCurveCopy;

%include "ase/AbsLogLikelihoodCurve.hh"
%include "ase/LikelihoodCurveCopy.hh"

namespace ase {
    %extend AbsLogLikelihoodCurve {
         ase::LikelihoodCurveCopy __add__(const AbsLogLikelihoodCurve& r)
         {
             return *($self) + r;
         }
         ase::LikelihoodCurveCopy __sub__(const AbsLogLikelihoodCurve& r)
         {
             return *($self) - r;
         }
         ase::LikelihoodCurveCopy __mul__(const double& r)
         {
             return *($self)*r;
         }
         ase::LikelihoodCurveCopy __rmul__(const double& r)
         {
             return *($self)*r;
         }
         ase::LikelihoodCurveCopy __truediv__(const double& r)
         {
             return *($self)/r;
         }
    } 
}

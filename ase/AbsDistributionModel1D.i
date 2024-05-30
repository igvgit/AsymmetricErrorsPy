%include stddecls.i
%include ase/AbsRNG.i

%{
#include "ase/AbsDistributionModel1D.hh"
%}

%include "ase/AbsDistributionModel1D.hh"

namespace ase {
    %extend AbsDistributionModel1D {
         std::vector<double> generate(AbsRNG& g, const unsigned npoints)
         {
             std::vector<double> result(npoints);
             for (unsigned i=0; i<npoints; ++i)
                 result[i] = $self->random(g);
             return result;
         }
    }
}

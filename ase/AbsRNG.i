%include stddecls.i

%{
#include "ase/AbsRNG.hh"
%}

%include "ase/AbsRNG.hh"

namespace ase {
    %extend AbsRNG {
         std::vector<double> generate(const unsigned npoints)
         {
             std::vector<double> result(npoints);
             for (unsigned i=0; i<npoints; ++i)
                 result[i] = (*$self)();
             return result;
         }
    }
}

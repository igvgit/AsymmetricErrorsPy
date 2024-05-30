%include stddecls.i

%{
#include "ase/TransitionCubic.hh"
%}

%include "ase/TransitionCubic.hh"

namespace ase {
    %template(TransitionCubic) TransitionCubic<double>;
}

%{
#include "ase/Interval.hh"
%}

%include "ase/Interval.hh"

namespace ase {
    %template(Interval) Interval<double>;
}

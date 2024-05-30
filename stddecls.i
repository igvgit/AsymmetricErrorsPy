%include std_string.i
%include std_vector.i
%include std_pair.i

%{
#include <vector>
#include <utility>
%}

// Instantiations of pairs of some standard types
namespace std {
   %template(UIntDoublePair)   pair<unsigned,double>;
   %template(DoubleDoublePair) pair<double,double>;
   %template(BoolDoublePair)   pair<bool,double>;
}

// Instantiations of vectors of some standard types
namespace std {
   %template(DoubleVector)     vector<double>;
}

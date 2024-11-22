%include stddecls.i

%{
#include "PyFunctor1.hh"
%}

%rename(__call__) asepy::PyFunctor1::operator();

%include "PyFunctor1.hh"

%include "ase/Interval.i"

%{
#include "ase/AsymmetricEstimate.hh"
%}

%include "ase/AsymmetricEstimate.hh"

namespace ase {
    %extend AsymmetricEstimate {
         std::string __repr__() const
         {
             std::ostringstream os;
             os << *$self;
             return os.str();
         }

         bool __eq__(const AsymmetricEstimate& other) const
         {
             return *$self == other;
         }

         bool __ne__(const AsymmetricEstimate& other) const
         {
             return *$self != other;
         }

         %pythoncode %{
             def fstr(self, formatSpecifier):
                 fmt = "{{{!s}}} + {{{!s}}} - {{{!s}}}".format(
                     formatSpecifier, formatSpecifier, formatSpecifier)
                 return fmt.format(self.location(), self.sigmaPlus(), self.sigmaMinus())
         %}
    }
}

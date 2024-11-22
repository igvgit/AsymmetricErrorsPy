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

         AsymmetricEstimate __mul__(const double& r) const
         {
             return *$self * r;
         }

         AsymmetricEstimate __rmul__(const double& r) const
         {
             return *$self * r;
         }

         AsymmetricEstimate __add__(const double& r) const
         {
             return *$self + r;
         }

         AsymmetricEstimate __radd__(const double& r) const
         {
             return *$self + r;
         }

         AsymmetricEstimate __sub__(const double& r) const
         {
             return *$self - r;
         }

         AsymmetricEstimate __neg__() const
         {
             return -*$self;
         }

         AsymmetricEstimate __pos__() const
         {
             return +*$self;
         }

         %pythoncode %{
             def fstr(self, formatSpecifier):
                 fmt = "{{{!s}}} + {{{!s}}} - {{{!s}}}".format(
                     formatSpecifier, formatSpecifier, formatSpecifier)
                 return fmt.format(self.location(), self.sigmaPlus(), self.sigmaMinus())

             # I had problems wrapping __truediv__ and __rsub__ with swig
             def __truediv__(self, other):
                 if (other == 0.0):
                     raise ZeroDivisionError("AsymmetricEstimate divided by zero")
                 return self * (1.0/other)

             def __rsub__(self, other):
                 return self * (-1.0) + other
         %}
    }
}

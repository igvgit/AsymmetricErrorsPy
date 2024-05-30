%module asepy

%{
#define SWIG_FILE_WITH_INIT
%}

%include "numpy.i"

%init %{
import_array();
%}

// std_sstream.i must be included before std_string.i (due to a bug in SWIG)
%include std_sstream.i
%include stddecls.i
%include exception.i
%include typemaps.i

%exception {
  try {
    $action
  } catch (const std::exception& e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
}

%newobject *::clone;

%newobject *::fromQuantilesBarePtr;
%ignore *::fromQuantiles;
%rename(fromQuantiles) *::fromQuantilesBarePtr;

%newobject *::fromModeAndDeltasBarePtr;
%ignore *::fromModeAndDeltas;
%rename(fromModeAndDeltas) *::fromModeAndDeltasBarePtr;

%include "ase/include_all.i"
%include "RandomGenerators.i"
%include "scanFunctor1D.i"
%include "PyFunctor1.i"
%include "empiricalCdfOutline.i"

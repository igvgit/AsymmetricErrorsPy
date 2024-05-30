#ifndef ASEPY_PYWRAPUTILS_HH_
#define ASEPY_PYWRAPUTILS_HH_

#include <stdexcept>

#include "Python.h"

namespace asepy {
    inline double getDoubleFromPyObj(PyObject* d)
    {
        if (PyErr_Occurred()) throw std::runtime_error(
            "In asepy::getDoubleFromPyObj: unhandled error at the time of call"); 
        const double tmp = PyFloat_AsDouble(d);
        if (PyErr_Occurred()) throw std::runtime_error(
            "In asepy::getDoubleFromPyObj: argument can not be converted to a double");
        return tmp;
    }

    class DecrefHandle
    {
    public:
        inline explicit DecrefHandle(PyObject* ptr) : ptr_(ptr) {}
        inline ~DecrefHandle() {Py_XDECREF(ptr_);}
        inline PyObject* release() {PyObject* p = ptr_; ptr_=0; return p;}

    private:
        PyObject* ptr_;
    };

    inline void validatePyCallable(PyObject* pFunc)
    {
        if (!pFunc) throw std::invalid_argument(
            "In asepy::validatePyCallable: null object encountered");
        if (!PyCallable_Check(pFunc)) throw std::invalid_argument(
            "In asepy::validatePyCallable: argument is not callable");
    }
}

#endif // ASEPY_PYWRAPUTILS_HH_

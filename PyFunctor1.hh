#ifndef ASEPY_PYFUNCTOR1_HH_
#define ASEPY_PYFUNCTOR1_HH_

#include <cassert>

#include "pyWrapUtils.hh"

namespace asepy {
    class PyFunctor1
    {
    public:
        inline explicit PyFunctor1(PyObject* callable)
            : pFunc_(0)
        {
            validatePyCallable(callable);
            pFunc_ = callable;
            Py_INCREF(pFunc_);
        }

        inline virtual ~PyFunctor1() {Py_XDECREF(pFunc_);}

        inline double operator()(const double x_in) const
        {
            // Build the arguments for the callable
            PyObject *pArgs = PyTuple_New(1);
            DecrefHandle h_pArgs(pArgs);
            PyObject* x = PyFloat_FromDouble(x_in);
            assert(x);
            PyTuple_SetItem(pArgs, 0, x);

            // Evaluate the callable
            PyObject* pValue = PyObject_CallObject(pFunc_, pArgs);
            if (!pValue) throw std::runtime_error(
                "In asepy::PyFunctor1::operator(): object call failed");
            DecrefHandle h_pValue(pValue);

            return getDoubleFromPyObj(pValue);
        }

    private:
        PyFunctor1(const PyFunctor1& r) = delete;
        PyFunctor1& operator=(const PyFunctor1& r) = delete;

        PyObject* pFunc_;
    };
}

#endif // ASEPY_PYFUNCTOR1_HH_

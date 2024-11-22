#ifndef ASEPY_PYFUNCTOR1_HH_
#define ASEPY_PYFUNCTOR1_HH_

#include <cassert>
#include <utility>
#include <cmath>

#include "ase/findRootUsingBisections.hh"
#include "ase/findMinimumGoldenSection.hh"

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

        // The first element of the returned pair will be "false"
        // in case the initial interval does not bracket the root.
        // In case the first element of the returned pair is "true",
        // the second could be the root, the discontinuity point,
        // or the singularity.
        inline std::pair<bool,double> findRoot(const double rhs,
                                               const double xmin,
                                               const double xmax,
                                               double tol = 0.0) const
        {
            if (tol == 0.0)
                tol = 2.0*std::numeric_limits<double>::epsilon();
            double rt = 0.0;
            const double status = ase::findRootUsingBisections(
                *this, rhs, xmin, xmax, tol, &rt);
            return std::pair<bool,double>(status, rt);
        }

        inline std::pair<bool,double> findMinimum(const double xleft,
                                                  const double xmiddle,
                                                  const double xright,
                                                  double tol = 0.0) const
        {
            if (tol == 0.0)
                tol = std::sqrt(std::numeric_limits<double>::epsilon());
            double argmin = 0.0;
            const double status = ase::findMinimumGoldenSection(
                *this, xleft, xmiddle, xright, tol, &argmin);
            return std::pair<bool,double>(status, argmin);
        }

        inline std::pair<bool,double> findMaximum(const double xleft,
                                                  const double xmiddle,
                                                  const double xright,
                                                  double tol = 0.0) const
        {
            if (tol == 0.0)
                tol = std::sqrt(std::numeric_limits<double>::epsilon());
            double argmax = 0.0;
            const double status = ase::findMinimumGoldenSection(
                *this, xleft, xmiddle, xright, tol, &argmax, (double*)0, true);
            return std::pair<bool,double>(status, argmax);
        }

    private:
        PyFunctor1(const PyFunctor1& r) = delete;
        PyFunctor1& operator=(const PyFunctor1& r) = delete;

        PyObject* pFunc_;
    };
}

#endif // ASEPY_PYFUNCTOR1_HH_

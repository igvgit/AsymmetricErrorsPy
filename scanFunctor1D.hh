#ifndef ASEPY_SCANDOUBLEFUNCTOR1_HH_
#define ASEPY_SCANDOUBLEFUNCTOR1_HH_

#include <cassert>

#include "NumpyTypecode.hh"

namespace asepy {
    template<class Functor>
    inline PyObject* scanFunctor1D(
        const Functor& fcn,
        const double xmin, const double xmax, const unsigned npoints)
    {
        const int typenum = NumpyTypecode<double>::code;
        npy_intp sh = npoints;
        PyObject* xarr  = PyArray_SimpleNew(1, &sh, typenum);
        PyObject* yarr  = PyArray_SimpleNew(1, &sh, typenum);
        PyObject* result = NULL;

        if (xarr == NULL || yarr == NULL)
            goto fail;
        else if (npoints)
        {
            double* xv = (double*)PyArray_DATA((PyArrayObject*)xarr);
            double* yv = (double*)PyArray_DATA((PyArrayObject*)yarr);
            double step = xmax - xmin;
            if (npoints > 1U)
                step /= (npoints - 1U);
            for (unsigned i=0; i<npoints; ++i)
            {
                double x = xmin + i*step;
                if (i && i+1U == npoints)
                    x = xmax;
                xv[i] = x;
                yv[i] = fcn(x);
            }

            result = Py_BuildValue("(OO)", xarr, yarr);
            if (result == NULL)
                goto fail;
        }

        return result;

    fail:
        Py_XDECREF(xarr);
        Py_XDECREF(yarr);
        return result;
    }

    template<class Functor>
    inline PyObject* scanFunctor1D(
        const Functor& fcn,
        const double* coords, const unsigned npoints)
    {
        const int typenum = NumpyTypecode<double>::code;
        npy_intp sh = npoints;
        PyObject* yarr  = PyArray_SimpleNew(1, &sh, typenum);

        if (yarr == NULL)
            goto fail;
        else if (npoints)
        {
            assert(coords);
            double* yv = (double*)PyArray_DATA((PyArrayObject*)yarr);
            for (unsigned i=0; i<npoints; ++i)
                yv[i] = fcn(coords[i]);
        }

        return yarr;

    fail:
        Py_XDECREF(yarr);
        return 0;
    }
}

#endif // ASEPY_SCANDOUBLEFUNCTOR1_HH_

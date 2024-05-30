#ifndef ASEPY_EMPIRICALCDFOUTLINE_HH_
#define ASEPY_EMPIRICALCDFOUTLINE_HH_

#include <stdexcept>

#include "ase/DistributionModels1D.hh"
#include "NumpyTypecode.hh"

namespace asepy {
    PyObject* empiricalCdfOutline(const ase::EmpiricalDistribution& ed,
                                  const double xmin, const double xmax)
    {
        if (!(xmin < xmax))
            throw std::invalid_argument("In asepy::empiricalCdfOutline: "
                                        "invalid interval definition");

        unsigned long drawCount = 2UL;
        const std::vector<double>& sample = ed.sample();
        const unsigned long sz = sample.size();

        if (xmin <= ed.minCoordinate() && xmax >= ed.maxCoordinate())
            drawCount += 2UL*sz;
        else
        {
            // The following can be made faster...
            for (unsigned long i=0; i<sz; ++i)
            {
                const double x = sample[i];
                if (x >= xmin && x <= xmax)
                    drawCount += 2UL;
            }
        }

        const int typenum = NumpyTypecode<double>::code;
        npy_intp sh = drawCount;
        PyObject* xarr  = PyArray_SimpleNew(1, &sh, typenum);
        PyObject* yarr  = PyArray_SimpleNew(1, &sh, typenum);
        PyObject* result = NULL;

        if (xarr == NULL || yarr == NULL)
            goto fail;
        else
        {
            double* xout = (double*)PyArray_DATA((PyArrayObject*)xarr);
            double* yout = (double*)PyArray_DATA((PyArrayObject*)yarr);
            unsigned long iout = 0;

            if (drawCount == 2UL)
            {
                xout[iout] = xmin;
                yout[iout++] = ed.cdf(xmin);
                xout[iout] = xmax;
                yout[iout++] = ed.cdf(xmax);
            }
            else
            {    
                bool first = true;
                double prevcdf = 0.0;

                for (unsigned long i=0; i<sz; ++i)
                {
                    const double x = sample[i];
                    if (x >= xmin && x <= xmax)
                    {
                        if (first)
                        {
                            prevcdf = static_cast<double>(i)/sz;
                            xout[iout] = xmin;
                            yout[iout++] = prevcdf;
                            first = false;
                        }
                        xout[iout] = x;
                        yout[iout++] = prevcdf;
                        prevcdf = static_cast<double>(i+1UL)/sz;
                        xout[iout] = x;
                        yout[iout++] = prevcdf;
                    }
                }
                assert(iout + 1U == drawCount);
                xout[iout] = xmax;
                yout[iout++] = prevcdf;
            }
            assert(iout == drawCount);

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
}

#endif // ASEPY_EMPIRICALCDFOUTLINE_HH_

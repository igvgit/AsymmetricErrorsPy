#!/usr/bin/env python3
"""
This script illustrates numerical convolution of two distributions
using one of the convolution classes, "NumericalConvolution"
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import matplotlib.pyplot as plt
from asepy_utils import scanDensity

distro1 = ase.SkewNormal(0.0, 1.0, 5.0)
distro2 = ase.DimidiatedGaussian(1.0, 0.5, 0.8)
nPt = 4
nIntervals = 1000

# The "NumericalConvolution" class performs the convolution by
# transforming the integration variable to a space in which the
# density of the second distribution ("distro2" here) becomes
# uniform on [0, 1]. The argument "nPt" specifies the number of
# points used by the "GaussLegendreQuadrature" class and should be
# supported by that class. The argument "nIntervals" specifies the
# number of subintervals into which the interval [0, 1] will be
# split. In general, the distribution "distro2" should be narrower
# than "distro1". If one or both densities are not smooth (as it is
# the case in this particular example), it makes sense to use large
# "nIntervals" and small "nPt". If both densities are smooth
# (i.e., infinitely differentiable), use large "nPt" instead
# (for example, 512) and set the "nIntervals" argument to 1 (this
# argument can also be omitted in which case the default value of 1
# will be used).
conv = ase.NumericalConvolution(distro1, distro2, nPt, nIntervals)

# The "NumericalConvolution" class is not a distribution, it is
# simply a functor. Here, we are making a distribution out of it
# by scanning the convolved density. The "derivativeH" argument
# is the step size used to make a numerical estimate of the density
# derivative. The density is then modeled by cubic Hermite splines.
xmin = -3
xmax = 7
nscan = 1001
derivativeH = 1.e-4
convDistro = ase.InterpolatedDensity1D(xmin, xmax, nscan, conv, derivativeH)

# Now, we can plot the densities
x, v1 = scanDensity(distro1, xmin, xmax, nscan)
v2 = scanDensity(distro2, x)
v3 = scanDensity(convDistro, x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, v1, 'r', label='Density 1: {}'.format(distro1.classname()))
ax.plot(x, v2, 'b', label='Density 2: {}'.format(distro2.classname()))
ax.plot(x, v3, 'k', label='Convolution')

plt.xlabel('X')
plt.ylabel('Density')
plt.title('Convolution Example')
plt.legend(loc=1)
plt.show()

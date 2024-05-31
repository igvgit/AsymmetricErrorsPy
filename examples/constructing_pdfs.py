#!/usr/bin/env python3
"""
This script illustrates various methods that can be used to construct
probability distribution models representing results with asymmetric errors
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 31 2024"

import math
import numpy as np
import asepy as ase
import matplotlib.pyplot as plt
from asepy_utils import scanDensity, scanPythonCallable, fullOPATPdfs

# The asepy package has a number of classes representing probability
# distributions. You can see the complete current list of this classes
# by running the script "asepyDistributionModels.py".
#
# There are usually several methods that can be used to construct
# probability distribution objects. Here, we will be illustrating
# them with the "SkewNormal" class representing the skew normal
# distribution, https://en.wikipedia.org/wiki/Skew_normal_distribution
#
# 1) The "natural" constructor which takes the parameters used in the
#    relevant mathematical formulae. The meaning and the number of
#    these parameters varies from class to class. For the SkewNormal,
#    these parameters are location, scale, and shape parameter alpha.
location = -1.0
scale = 0.5
alpha = 1.3
d1 = ase.SkewNormal(location, scale, alpha)

# All distribution classes have a boolean class member "isFullOPAT".
# If that member is True, it means that the class can be constructed
# utilizing parameters median, sigmaPlus, and sigmaMinus (and, potentially,
# some additional ones). Either sigmaPlus or sigmaMinus or both can be
# negative. You can get the list of fully OPAT compatible classes whose
# constructors have the signature "classname(median, sigmaPlus, sigmaMinus)"
# by calling the function "fullOPATPdfs" from the asepy_utils module:
print("Fully OPAT compatible classes with standard constructors:")
for cl in fullOPATPdfs():
    print(cl.__name__)

# 2) The constructor from a sequence of cumulants (mean, variance, skewness).
#    In this constructor, the skewness is not normalized, it is just the
#    third central moment. Typically, there is some numerical procedure
#    which, internally, determines the values of the natural parameters so
#    that the resulting distribution has the cumulants provided. For the
#    skew normal distribution, the skewness can not be arbitrary large in
#    magnitude, as it can not exceed the skewness of the half-Gaussian. 
cumulants = [0.5, 1.0, -0.3]
d2 = ase.SkewNormal(cumulants)
print("\nConstructor argument cumulants are", cumulants)
print("Cumulants of the constructed distribution are",
      [d2.cumulant(i) for i in range(1, 4)])

# 3) The class method "fromQuantiles". The signature of this method is
#    "fromQuantiles(median, sigmaPlus, sigmaMinus)". Here, parameter
#    "median" corresponds to the distribution median while the value
#    median - sigmaMinus corresponds to the 16th percentile (approximately,
#    the exact cdf value at that point is 0.1586552539... and is given
#    by the built-in constant ase.GCDF16) and the value median + sigmaPlus
#    corresponds to the 84th percentile (the cdf value ase.GCDF84).
median = 1.0
sigmaPlus = 0.5
sigmaMinus = 0.7
d3 = ase.SkewNormal.fromQuantiles(median, sigmaPlus, sigmaMinus)
print("\nCdf at the median is", d3.cdf(median), "expected 0.5")
print("Cdf at median - sigmaMinus is", d3.cdf(median - sigmaMinus),
      "expected", ase.GCDF16)
print("Cdf at median + sigmaPlus is", d3.cdf(median + sigmaPlus),
      "expected", ase.GCDF84)

# 4) The class method "fromModeAndDeltas" (if implemented). Normally,
#    this method is used internally by the package code to construct
#    log-likelihood models from density models. The signature of this
#    method is "fromModeAndDeltas(mode, deltaPlus, deltaMinus)". The
#    "mode" argument corresponds to the distribution mode while
#    deltaPlus is such a number that the log of the density at
#    mode + deltaPlus is less than the log of the density at mode by 0.5.
#    (and similarly for deltaMinus).
mode = 1.0
deltaPlus = 0.8
deltaMinus = 0.5
d4 = ase.SkewNormal.fromModeAndDeltas(mode, deltaPlus, deltaMinus)
lnAtMode = math.log(d4.density(mode))
lnAtPlus = math.log(d4.density(mode + deltaPlus))
lnAtMinus = math.log(d4.density(mode - deltaMinus))
print("\nlog density differences are", lnAtMode - lnAtPlus, "and",
      lnAtMode - lnAtMinus, "expected 0.5")

# You can also implement a probability density function in Python
# and then use two classes in the asepy package, InterpolatedDensity1D
# and TabulatedDensity1D, in order to construct full-fledged distribution
# objects (with methods for calculating cdf, quantile function, cumulants,
# generating random numbers, etc). Both of these classes utilize a discretized
# representation of the density on a regular grid. These classes differ
# in the manner by which they calculate the density between the grid
# points: TabulatedDensity1D performs simple linear interpolation while
# InterpolatedDensity1D employs cubic Hermite splines. InterpolatedDensity1D
# should be preferred in most situations, while TabulatedDensity1D can be
# useful for representing densities with sharp edges or with discontinuous
# derivatives.
#
# This method works well for distributions with compact support or for
# distributions whose tails decay quickly at infinity so that their support
# can be truncated without introducing substantial distortions.
#
# Here is an example which builds the beta distribution from its density.
# The density values do not have to be normalized as they will be
# normalized internally by the InterpolatedDensity1D class.
class UnnormalizedBetaDensity:
    def __init__(self, alpha, beta):
        self.alpham1 = alpha - 1.0
        self.betam1 = beta - 1.0
    def __call__(self, x):
        if x <= 0.0 or x >= 1.0:
            return 0.0
        else:
            return math.pow(x, self.alpham1)*math.pow(1.0 - x, self.betam1)

# Here, we will be calculating derivatives at the grid points numerically.
# It is also possible to provide another callable which calculates density
# derivatives. Naturally, the step size for calculating the derivatives
# (called "h" here) should be smaller than the cell size. Ideally, you
# should be familiar with the methods used to optimize this step size
# (see, for example, the section "Numerical Derivatives" of the "Numerical
# Recipes" book by Press, Teukolsky, Vetterling, and Flannery).
alpha = 1.5
beta = 2.4
density = UnnormalizedBetaDensity(alpha, beta)
xmin = 0.0
xmax = 1.0
gridLen = 1001
cellSize = (xmax - xmin)/(gridLen - 1)
h = 0.01*cellSize
d5 = ase.InterpolatedDensity1D(xmin, xmax, gridLen, ase.PyFunctor1(density), h)

# Compare the moments with their expected values
# (see https://en.wikipedia.org/wiki/Beta_distribution).
# You can try to change the grid length parameter above
# and see how this affects the precision of the moment
# calculation.
print("\nMean is", d5.cumulant(1), "expected", alpha/(alpha + beta))
v0 = alpha*beta/(alpha + beta)**2/(alpha + beta + 1)
print("Variance is", d5.cumulant(2), "expected", v0)
s0 = 2*(beta - alpha)/(alpha+beta+2)*math.sqrt((alpha+beta+1)/alpha/beta)
print("Skewness is", d5.cumulant(3), "expected", s0*math.pow(v0, 1.5))

# Plot the densities
coords, values = scanDensity(d5, -0.2, 1.2, 2801)
unnorm = scanPythonCallable(density, coords)
plt.plot(coords, values, 'b', label='Interpolated and normalized')
plt.plot(coords, unnorm, 'r', label='Original density function')
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Distribution implementation by InterpolatedDensity1D')
plt.legend()
plt.show()

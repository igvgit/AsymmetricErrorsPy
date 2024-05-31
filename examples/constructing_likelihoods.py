#!/usr/bin/env python3
"""
This script illustrates various methods that can be used to construct
log-likelihood models representing results with asymmetric errors
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 31 2024"

import asepy as ase
from asepy_utils import densityBasedLogliCurve

# Two types of log-likelihood models are implemented in asepy:
# the ones directly represented by their log-likelihood functions
# and the ones which can be constructed from probability distribution
# models by calculating the log of the probability density.
# The script "asepyLogliModels.py" will print the current list of
# implemented log-likelihood models with standard constructors.
#
# The models directly represented by their log-likelihood functions
# usually have a constructor with the following signature:
# "classname(location, sigmaPlus, sigmaMinus)". The log-likelihood
# curve constructed in this manner will have the value of 0 at
# "location" and the value of -0.5 at location - sigmaMinus and at
# location + sigmaPlus. Here is an example:
location = 1.0
sigmaPlus = 2.0
sigmaMinus = 3.0
ll1 = ase.GeneralisedPoisson(location, sigmaPlus, sigmaMinus)
print("Log-likelihood 1 at", location, "is", ll1(location))
print("Log-likelihood 1 at", location + sigmaPlus, "is", ll1(location + sigmaPlus))
print("Log-likelihood 1 at", location - sigmaMinus, "is", ll1(location - sigmaMinus))

# To construct a density-based log-likelihood model, we can call
# the convenience function "densityBasedLogliCurve" from the
# asepy_utils module:
ll2 = densityBasedLogliCurve(ase.SkewNormal, location, sigmaPlus, sigmaMinus)
print("\nLog-likelihood 2 at", location, "is", ll2(location))
print("Log-likelihood 2 at", location + sigmaPlus, "is", ll2(location + sigmaPlus))
print("Log-likelihood 2 at", location - sigmaMinus, "is", ll2(location - sigmaMinus))

# An arbitrary log-likelihood curve can be implemented by calculating
# a set of discretized log-likelihood values on a grid and
# interpolating between the grid points with cubic Hermite splines.
# For that, we can utilize the "CubicHermiteInterpolatorEG" class.
def my_curve(x):
    return -0.5*((x - 0.5)/2.0)**2

minParam = -5.0
maxParam = 5.0
gridLen = 1001
cellSize = (maxParam - minParam)/(gridLen - 1)
h = 0.01*cellSize # Step size used for numerical differentiation
ll3 = ase.CubicHermiteInterpolatorEG(minParam, maxParam, gridLen,
                                     ase.PyFunctor1(my_curve), h)
print("\nLog-likelihood 3 is maximized at", ll3.argmax())
print("Log-likelihood 3 positive error is", ll3.sigmaPlus())
print("Log-likelihood 3 negative error is", ll3.sigmaMinus())

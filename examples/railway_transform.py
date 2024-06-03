#!/usr/bin/env python3
"""
The code below illustrates the transformation used to construct
railway Gaussian distribution
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

import asepy as ase
import matplotlib.pyplot as plt

# Transformation parameters. Change them and see what happens.
sigmaPlus = 1.0
sigmaMinus = 0.5

# Default choice for the widths of the transition regions
hleft, hright = ase.RailwayGaussian.transitionRegionChoice(sigmaPlus, sigmaMinus)

# Plotting parameters. You might want to adjust them if you
# adjust sigmaPlus and sigmaMinus.
xmin = -2.0
xmax = 4.0
nscan = 601

# Construct the transform and its derivatives
curve = ase.ParabolicRailwayCurve(sigmaPlus, sigmaMinus, hleft, hright)
deriv = ase.DerivativeFunctor(curve)
secondDeriv = ase.SecondDerivativeFunctor(curve)

# Check that the transform works as desired
print("Transform at -1.0 is", curve(-1.0), "expect", -sigmaMinus)
print("Transform at 0.0 is", curve(0.0), "expect 0.0")
print("Transform at 1.0 is", curve(1.0), "expect", sigmaPlus)

# Railway Gaussian distribution will exhibit a Jacobian spike
# if the transformation curve has an extremum. This will always
# happen if sigmaPlus and sigmaMinus are of opposite signs but
# can also happen for same sign sigmas if one of them is much
# larger in magnitude than the other.
if (curve.hasExtremum()):
    print("Found curve extremum at", curve.extremum())

# Make the plots
x, y = ase.scanFunctor1D(curve, xmin, xmax, nscan)
yder = ase.scanFunctor1D(deriv, x)
der2 = ase.scanFunctor1D(secondDeriv, x)

plt.plot(x, y, 'r', label='Transform')
plt.plot(x, yder, 'b', label='Derivative')
plt.plot(x, der2, 'k', label='Second Derivative')

plt.xlabel(r'$\nu$')
plt.ylabel('R')
plt.title('Railway Coordinate Transform')
plt.grid()
plt.legend()
plt.show()

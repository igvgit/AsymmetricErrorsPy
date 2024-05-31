#!/usr/bin/env python3
"""
This script illustrates curve interpolation by the
"CubicHermiteInterpolatorEG" class when the curve is specified by
its values at a few points and the derivatives are not provided
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import matplotlib.pyplot as plt
from asepy_utils import scanPythonCallable, scanLogLikelihood

def fcn(x):
    return x**3 - 2*x**2 - 10*x - 1

xmin = -3
xmax = 5
nscan = 801
x, y = scanPythonCallable(fcn, xmin, xmax, nscan)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'r', label='Actual curve (cubic)')

nPoints = ( 2,   3,   4,   5 )
colors  = ('k', 'g', 'b', 'c')

for npt, color in zip(nPoints, colors):
    dummy, y = scanPythonCallable(fcn, xmin, xmax, npt)
    interpolator = ase.CubicHermiteInterpolatorEG(xmin, xmax, y)
    yscan = scanLogLikelihood(interpolator, x)
    ax.plot(x, yscan, color, label='Using {} values'.format(npt))

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolation without specified derivatives')
plt.legend()
plt.show()

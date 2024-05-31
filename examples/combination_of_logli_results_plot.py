#!/usr/bin/env python3
"""
This script illustrates the combination of results example in the section
"Combination of Results using likelihood" of the "Asymmetric Errors" paper.
Here, we plot the curves and the resulting combined curve.
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
from asepy_utils import scanLogLikelihood

# Likelihood model to use for all curves in this example
model = ase.VariableVarianceLogli

# Input estimates
r1 = ase.AsymmetricEstimate(1.9, 0.7, 0.5, ase.L)
r2 = ase.AsymmetricEstimate(2.4, 0.6, 0.8, ase.L)
r3 = ase.AsymmetricEstimate(3.1, 0.5, 0.4, ase.L)

# Construct the likelihood curves. The reason we are not
# simply iterating over inputs is that each curve will utilize
# its own plotting range. And the reason for separate
# plotting ranges is that the support of variable variance
# model is bounded -- the variance must be kept positive.
# The overall union of the ranges (in this case, [1.0, 4.0])
# will not work for all curves.
c1 = model(r1.location(), r1.sigmaPlus(), r1.sigmaMinus())
c2 = model(r2.location(), r2.sigmaPlus(), r2.sigmaMinus())
c3 = model(r3.location(), r3.sigmaPlus(), r3.sigmaMinus())

# Combine the curves. If we were iterating, it would be
# convenient to create and use a LikelihoodAccumulator object.
# Here, we can just add the curves using the "+" operator.
acc = c1 + c2 + c3
result = ase.AsymmetricEstimate(acc.argmax(), acc.sigmaPlus(),
                                acc.sigmaMinus(), ase.L)
print("Combined result:", result.fstr(":.3f"))

# Plot the input curves
nscan = 1001
x, y = scanLogLikelihood(c1, 1.0, 3.8, nscan)
plt.plot(x, y, 'b')
x, y = scanLogLikelihood(c2, 1.0, 3.5, nscan)
plt.plot(x, y, 'b')
x, y = scanLogLikelihood(c3, 2.3, 4.0, nscan)
plt.plot(x, y, 'b')

# Plot the combined curve. Shift it vertically so that the maximum is at 0.
x, y = scanLogLikelihood(acc, 2.2, 3.4, nscan)
plt.plot(x, y - acc.maximum(), 'r')

# Draw a line at -0.5
plt.plot(np.linspace(1.0, 4.0, 2), np.full(2, -0.5), 'k--')

plt.xlabel('a')
plt.ylabel('ln L')
plt.title('Combining three asymmetric errors')
plt.show()

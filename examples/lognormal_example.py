#!/usr/bin/env python3
"""
This example plots a distribution density (log-normal here)
and a variable transformation which can be used to transform
the standard normal into this density
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
from asepy_utils import scanDensity, qqmapFromStandardNormal

# Script parameters
mu = 0.0
sigmaPlus = 1.0
sigmaMinus = 0.6
xmin = -2.0
xmax = 4.0
nscan = 1201

# Build the distribution using the class method "fromQuantiles"
distro = ase.LogNormal.fromQuantiles(mu, sigmaPlus, sigmaMinus)

# Check the quantiles of the constructed distribution
q16 = distro.quantile(ase.GCDF16)
q50 = distro.quantile(0.5)
q84 = distro.quantile(ase.GCDF84)
resultRepresented = ase.AsymmetricEstimate(q50, q84-q50, q50-q16, ase.P)
print("Result represented:", resultRepresented.fstr(":.3f"))

# Plot the density
x, y = scanDensity(distro, xmin, xmax, nscan)
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel(r'$\rho(x)$')
plt.title('Log-normal Density')
plt.show()

# Construct and plot the transformation from the standard normal
xmin = -3.0
xmax = 3.0
z = np.linspace(xmin, xmax, nscan)
x = qqmapFromStandardNormal(distro, z)

plt.plot(z, x)
plt.xlabel('z')
plt.ylabel('x')
plt.title('Log-normal Transform')
plt.show()

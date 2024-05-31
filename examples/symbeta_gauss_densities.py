#!/usr/bin/env python3
"""
The code below plots a collection of symmetric beta Gaussian densities
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import matplotlib.pyplot as plt
from asepy_utils import scanDensity

# Positive and negative errors for all cases
sp = 1.0
sm = 0.6

# Plotting parameters
xmin = -2.0
xmax = 4.0
nscan = 1201

# Values of parameters "p" and "h" for which the plots are made.
# See the section "The Symmetric Beta Gaussian" in the Appendix A
# of the "Asymmetric Errors" paper for the meaning of these parameters.
pvals =  (2,   2,   2,   1,   3)
hvals =  (0.5, 1.0, 2.0, 1.0, 1.0)
colors = ('r', 'g', 'b', 'm', 'c')

for p, h, c in zip(pvals, hvals, colors):
    distro = ase.SymmetricBetaGaussian(0.0, sp, sm, p, h)
    coords, values = scanDensity(distro, xmin, xmax, nscan)
    plt.plot(coords, values, c, label="$p$ = {}, $h$ = {}".format(p, h))

plt.xlabel('R')
plt.ylabel(r'$\rho$(R)')
plt.title('Symmetric Beta Gaussian Densities')
plt.legend()
plt.show()

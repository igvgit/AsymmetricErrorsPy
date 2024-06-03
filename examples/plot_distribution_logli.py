#!/usr/bin/env python3
"""
Usage: plot_distribution_logli.py classname mu rightSigma leftSigma deltaLnL?

If not provided, the argument deltaLnL will be set to 0.5.

Examples:

plot_distribution_logli.py SkewNormal 0 1 1.5
plot_distribution_logli.py SymmetricBetaGaussian_2_20 0 2 1
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.4"
__date__ ="June 3 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import math, sys
from asepy_utils import scanLogLikelihood, densityBasedLogliCurve

def make_plot(classname, mu, rightSigma, leftSigma, deltaLnL):
    # Some hadwired parameters
    nsigmas = 3.0
    nscan = round(200*nsigmas + 1)
    #
    distroClass = getattr(ase, classname)
    c = densityBasedLogliCurve(distroClass, mu, rightSigma, leftSigma, deltaLnL)
    xmin = mu - leftSigma*nsigmas
    xmax = mu + rightSigma*nsigmas
    if (xmin < c.parMin()):
        xmin = c.parMin()
    if (xmax > c.parMax()):
        xmax = c.parMax()
    coords, values = scanLogLikelihood(c, xmin, xmax, nscan)
    plt.plot(coords, values)
    plt.xlabel('Parameter')
    plt.ylabel('Log-likelihood')
    #
    title = '{}, $\mu = {}$, $\sigma^+ = {}$, $\sigma^- = {}$'.format(
        classname, mu, rightSigma, leftSigma)
    plt.suptitle(title)
    print("c(mu) =", c(mu))
    print("c'(mu) =", c.derivative(mu))
    print("c''(mu) =", c.secondDerivative(mu))
    print("c(mu + rightSigma) =", c(mu + rightSigma))
    print("c(mu - leftSigma) =", c(mu - leftSigma))
    plt.grid()
    plt.show()

def main(argv):
    # Parse command line options
    argc = len(argv)
    if (argc == 0):
        # Convention used here: command invoked without any arguments
        # prints its usage instruction and exits successfully
        print(__doc__)
        return 0
    elif (argc == 4 or argc == 5):
        # We have the correct number of arguments
        i = 0
        classname = argv[i]; i+=1
        mu = float(argv[i]); i+=1
        rightSigma = float(argv[i]); i+=1
        leftSigma = float(argv[i]); i+=1
        if argc == 5:
            deltaLnL = float(argv[i]);
        else:
            deltaLnL = 0.5;
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    make_plot(classname, mu, rightSigma, leftSigma, deltaLnL)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

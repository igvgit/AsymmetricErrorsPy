#!/usr/bin/env python3
"""
Usage: plot_likelihood_curve.py classname mu rightSigma leftSigma

Examples:

plot_likelihood_curve.py MoldedDoubleQuintic 1.0 2.5 1.3
plot_likelihood_curve.py ConservativeSigma10 1.0 2.0 3.0
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.3"
__date__ ="June 3 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import sys
from asepy_utils import scanLogLikelihood

def make_plot(classname, mu, rightSigma, leftSigma):
    # Some hadwired parameters
    nsigmas = 3.0
    nscan = round(200*nsigmas + 1)
    #
    cl = getattr(ase, classname)
    c = cl(mu, rightSigma, leftSigma)
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
    title = "{}({}, {}, {})".format(classname, mu, rightSigma, leftSigma)
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
    elif (argc == 4):
        # We have the correct number of arguments
        i = 0
        classname = argv[i]; i+=1
        mu = float(argv[i]); i+=1
        rightSigma = float(argv[i]); i+=1
        leftSigma = float(argv[i]); i+=1
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    make_plot(classname, mu, rightSigma, leftSigma)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

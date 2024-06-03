#!/usr/bin/env python3
"""
Usage: plot_likelihood_derivative.py order classname mu rightSigma leftSigma

The "order" argument specifies the order of log-likelihood derivative.
Must be 0, 1, or 2.

Examples:

plot_likelihood_derivative.py 1 MoldedDoubleQuintic 1.0 2.5 1.3
plot_likelihood_derivative.py 2 ConservativeSigma10 1.0 2.0 3.0
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.2"
__date__ ="Feb 08 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import sys
from asepy_utils import scanLogLikelihood, scanLogLikelihoodDerivative, scanLogLikelihoodSecondStep0

def make_plot(classname, scanner, label, mu, rightSigma, leftSigma):
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
    coords, values = scanner(c, xmin, xmax, nscan)
    plt.plot(coords, values)
    plt.xlabel('Parameter')
    plt.ylabel(label)
    #
    title = "{}({}, {}, {})".format(classname, mu, rightSigma, leftSigma)
    plt.suptitle(title)
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
    elif (argc == 5):
        # We have the correct number of arguments
        i = 0
        order = int(argv[i]); i+=1
        classname = argv[i]; i+=1
        mu = float(argv[i]); i+=1
        rightSigma = float(argv[i]); i+=1
        leftSigma = float(argv[i]); i+=1
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    if order == 0:
        scanner = scanLogLikelihood
        label = "Log-likelihood"
    elif order == 1:
        scanner = scanLogLikelihoodDerivative
        label = "Log-likelihood derivative"
    elif order == 2:
        scanner = scanLogLikelihoodSecondStep0
        label = "Log-likelihood second derivative"
    else:
        print(__doc__)
        return 1
    make_plot(classname, scanner, label, mu, rightSigma, leftSigma)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""
Usage: check_cumulants.py xmin xmax npt nsplit classname p0 p1 ...

xmin, xmax   are the integration limits for numerical calculation of
             the distribution moments by Gauss-Legendre quadratures.
             For some distributions Gauss-Hermite quadratures are used
             instead and these limits are ignored. The quadrature type
             is determined automatically for each distribution model.

npt          number of points to use in the quadrature rule.

nsplit       number of subintervals on which Gauss-Legendre quadratures
             are performed (ignored for Gauss-Hermite).

classname    is the name of "ase" distribution model: "Gaussian",
             "DimidiatedGaussian", "DistortedGaussian", "SkewNormal",
             "LogNormal", "JohnsonSystem", etc.

p0 p1 ...    are the parameters passed to the class constructor (it may
             require more than two).

Example with the Gauss-Legendre quadrature:
check_cumulants.py -5 50 4 1100 JohnsonSu 1 1 2 20

Example with the Gauss-Hermite quadrature:
check_cumulants.py 0 0 128 0 DistortedGaussian 1.0 2.0 2.1
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.4"
__date__ ="May 30 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import sys

from asepy_utils import distributionCumulants, numericCumulants
from asepy_utils import distortedNumericCumulants

def check_cumulants(classname, xmin, xmax, npt, nsplit, arglist):
    cl = getattr(ase, classname)
    distro = cl(*arglist)
    title = "{}({})".format(classname, ", ".join([str(a) for a in arglist]))
    cum0 = distributionCumulants(distro)
    if classname == "DistortedGaussian":
        cum1 = distortedNumericCumulants(distro, npt)
    else:
        cum1 = numericCumulants(distro, xmin, xmax, npt, nsplit)
    print("Cumulants for", title)
    print("Built-in cumulants:", cum0)
    print("Numeric cumulants:", cum1)
    print("Difference:", cum0 - cum1)

def main(argv):
    # Parse command line options
    argc = len(argv)
    if (argc == 0):
        # Convention used here: command invoked without any arguments
        # prints its usage instruction and exits successfully
        print(__doc__)
        return 0
    elif (argc >= 7):
        # We might have the correct number of arguments
        i = 0
        xmin = float(argv[i]); i+=1
        xmax = float(argv[i]); i+=1
        npt = int(argv[i]); i+=1
        nsplit = int(argv[i]); i+=1
        classname = argv[i]; i+=1
        arglist = [float(a) for a in argv[i:]]
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    check_cumulants(classname, xmin, xmax, npt, nsplit, arglist)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

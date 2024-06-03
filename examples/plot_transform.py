#!/usr/bin/env python3
"""
Usage: plot_transform.py classname p0 p1 ...

classname    is the name of "ase" distribution model: "Gaussian",
             "DimidiatedGaussian", "DistortedGaussian", "SkewNormal",
             "LogNormal", "JohnsonSystem", etc.
             
p0 p1 ...    are the parameters passed to the class constructor
             (it may require more than two).

Examples:

plot_transform.py JohnsonSystem 1 1.5 2 20
plot_transform.py TruncatedDistribution1D -1 3 Gaussian 1 1.5
plot_transform.py MixtureModel1D 0.3 "Gaussian -2 1" 0.7 "Gaussian 2 1"
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 2 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import sys
from asepy_utils import parse_distro, qqmapFromStandardNormal

def make_plot(classname, arglist):
    # Some hadwired parameters
    plotRange = 3.2
    nScan = round(200*plotRange) + 1
    #
    distro = parse_distro(classname, arglist)
    z = np.linspace(-plotRange, plotRange, nScan)
    y = qqmapFromStandardNormal(distro, z)
    plt.plot(z, y)
    #
    title = "{}({})".format(classname, ", ".join([str(a) for a in arglist]))
    plt.title(title)
    plt.xlabel('z')
    plt.ylabel('Transform')
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
    elif (argc >= 3):
        # We might have the correct number of arguments
        i = 0
        classname = argv[i]; i+=1
        arglist = argv[i:]
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    make_plot(classname, arglist)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

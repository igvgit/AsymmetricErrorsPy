#!/usr/bin/env python3
"""
Usage: plot_distribution.py xmin xmax classname p0 p1 ...

xmin, xmax   are the limits for density and cdf plotting.

classname    is the name of "ase" distribution model: "Gaussian",
             "DimidiatedGaussian", "DistortedGaussian", "SkewNormal",
             "LogNormal", "JohnsonSystem", etc.
             
p0 p1 ...    are the parameters passed to the class constructor
             (it may require more than two).

Examples:

plot_distribution.py -5 15 JohnsonSystem 1 1.5 2 20
plot_distribution.py -3 5 TruncatedDistribution1D -1 3 Gaussian 1 1.5
plot_distribution.py -5 5 MixtureModel1D 0.3 "Gaussian -2 1" 0.7 "Gaussian 2 1"
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.5"
__date__ ="May 30 2024"

import asepy as ase
import matplotlib.pyplot as plt
import sys
from asepy_utils import parse_distro, scanDensity, scanCdf

def make_plot(classname, xmin, xmax, arglist):
    # Some hadwired parameters
    nscan = 1001
    nrandom = 10000
    nbins = 50
    #
    distro = parse_distro(classname, arglist)
    fig, axs = plt.subplots(1, 2)
    coords, values = scanDensity(distro, xmin, xmax, nscan)
    vscale = 1.0
    if nrandom > 0:
        rng = ase.MersenneTwister64()
        randomSet = distro.generate(rng, nrandom)
        axs[0].hist(randomSet, bins=nbins, range=(xmin, xmax))
        vscale = nrandom*(xmax - xmin)/nbins
    axs[0].plot(coords, vscale*values, 'r')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Density')
    #
    if nrandom > 0:
        ecdf = ase.EmpiricalDistribution(randomSet)
        xe, ye = ase.empiricalCdfOutline(ecdf, xmin, xmax)
        axs[1].plot(xe, ye, 'y', linewidth=6)
    cdfvalues = scanCdf(distro, coords)
    axs[1].plot(coords, cdfvalues, 'r')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Cdf')
    try:
        mode = distro.mode()
    except:
        pass
    else:
        print("The mode is at", mode)
    #
    title = "{}({})".format(classname, ", ".join([str(a) for a in arglist]))
    fig.suptitle(title)
    fig.set_size_inches((10, 5))
    fig.tight_layout()
    plt.show()

def main(argv):
    # Parse command line options
    argc = len(argv)
    if (argc == 0):
        # Convention used here: command invoked without any arguments
        # prints its usage instruction and exits successfully
        print(__doc__)
        return 0
    elif (argc >= 5):
        # We might have the correct number of arguments
        i = 0
        xmin = float(argv[i]); i+=1
        xmax = float(argv[i]); i+=1
        classname = argv[i]; i+=1
        arglist = argv[i:]
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    make_plot(classname, xmin, xmax, arglist)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

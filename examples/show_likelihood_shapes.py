#!/usr/bin/env python3
"""
Usage: show_likelihood_shapes.py rightSigma pdffile classname0 classname1 ...

This script assumes mu = 0 and leftSigma = 1. The class names can
be either names of log-likelihood curve classes (that is, classes
derived from AbsLogLikelihoodCurve) or distribution model classes
which implement the method "fromModeAndDeltas". The "BrokenParabola"
class will be added automatically (for a reference).

The "pdffile" argument can be specified as "none". In this case the
curves will just be shown on the display.

Examples:

./show_likelihood_shapes.py 2 none VariableSigmaLogli VariableVarianceLogli PDGLogli MoldedDoubleQuintic MoldedCubicLogSigma

./show_likelihood_shapes.py 0.5 none LogLogisticBeta SkewNormal SymmetricBetaGaussian_2_20

./show_likelihood_shapes.py 2 none ConservativeSigma05 ConservativeSigma10 ConservativeSigma15 ConservativeSigma20 ConservativeSigmaMax
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.3"
__date__ ="May 30 2024"

import asepy as ase
import numpy as np
import matplotlib.pyplot as plt
import sys
from asepy_utils import scanLogLikelihood, intervalOverlap, densityBasedLogliCurve
from asepy_utils import scanLogLikelihoodDerivative, scanLogLikelihoodSecondStep0

def make_plot(classes, sigmaPlus, filename):
    # Some hadwired parameters
    mu = 0.0
    sigmaMinus = 1.0
    sdScale = 1.0
    if sigmaPlus < 1.0:
        sdScale = 1.0/sigmaPlus/sigmaPlus
    #
    wideSigmas = 3.1
    wideLogliLimits = (-wideSigmas*wideSigmas, 0.5)
    wideSecDerLimits = (-1.0*sdScale, 6.0*sdScale)
    wideDerivFactor = 5.0
    #
    narrowSigmas = 1.1
    narrowLogliLimits = (-0.7*narrowSigmas*narrowSigmas, 0.1)
    narrowSecDerLimits = (-0.5*sdScale, 3.0*sdScale)
    narrowDerivFactor = 2.0
    #
    colors = ('k', 'r', 'g', 'b', 'y', 'm', 'c', 'r--', 'g--', 'b--', 'y--', 'm--', 'c--')
    if len(classes) > len(colors):
        raise RuntimeError("Too many classes to plot")
    #
    fig, axs = plt.subplots(3, 2, sharex='col')
    axs[2, 0].set_xlabel('Parameter')
    axs[2, 1].set_xlabel('Parameter')
    axs[0, 0].set_ylabel('Log-likelihood')
    axs[1, 0].set_ylabel('Log-likelihood derivative')
    axs[2, 0].set_ylabel('Negative second derivative')
    for row in range(3):
        for col in range(2):
            axs[row, col].grid()
    title = 'Log-likelihood curves, $\sigma^+/\sigma^-$ = {}'.format(sigmaPlus/sigmaMinus)
    fig.suptitle(title)
    fig.set_size_inches((8, 9.5))
    fig.tight_layout()

    curveNum = 0
    ymin20 = 0.0
    ymax20 = 0.0
    for cl, c in zip(classes, colors):
        curve = None
        # Attempt to build the log-likelihood curve
        if issubclass(cl, ase.AbsDistributionModel1D):
            if not hasattr(cl, 'fromModeAndDeltas'):
                message = ("Can not build log-likelihood curve from the {} distribution as "
                           "it does not support construcion from mode and descent deltas.")
                raise RuntimeError(message.format(distroClass.__name__))
            try:
                curve = densityBasedLogliCurve(cl, mu, sigmaPlus, sigmaMinus)
            except:
                pass
        else:
            try:
                curve = cl(mu, sigmaPlus, sigmaMinus)
            except:
                pass
        #
        if not (curve is None):
            for wide in (True, False):
                if wide:
                    col = 0
                    nSigmas = wideSigmas
                    ylllims = wideLogliLimits
                    ysdlims = wideSecDerLimits
                    derFactor = wideDerivFactor
                else:
                    col = 1
                    nSigmas = narrowSigmas
                    ylllims = narrowLogliLimits
                    ysdlims = narrowSecDerLimits
                    derFactor = narrowDerivFactor
                parMin = -nSigmas*sigmaMinus
                parMax = nSigmas*sigmaPlus
                pmin, pmax = intervalOverlap(parMin, parMax, curve.parMin(), curve.parMax())
                nScan = round(100*(pmax - pmin)) + 1
                #
                # Plot log-likelihoods
                parValues, loglis = scanLogLikelihood(curve, pmin, pmax, nScan)
                axs[0, col].plot(parValues, loglis, c, label=cl.__name__)
                if curveNum == 0:
                    axs[0, col].set_ylim(ylllims)
                #
                # Plot derivatives
                derivs = scanLogLikelihoodDerivative(curve, parValues)
                axs[1, col].plot(parValues, derivs, c, label=cl.__name__)
                if curveNum == 0:
                    derMax = curve.derivative(pmin)
                    derMin = curve.derivative(pmax)
                    ydlims = (derMin*2.0, derMax*derFactor)
                    axs[1, col].set_ylim(ydlims)
                #
                # Plot second derivatives
                sders = scanLogLikelihoodSecondStep0(curve, parValues)
                axs[2, col].plot(parValues, -sders, c, label=cl.__name__)
                # if curveNum == 0:
                #     axs[2, col].set_ylim(ysdlims)
                if wide:
                    for p in (pmin, pmax):
                        sd = curve.secondDerivative(p)
                        if sd > ymax20:
                            ymax20 = sd
                        if sd < ymin20:
                            ymin20 = sd
        curveNum += 1
    #
    if ymin20 < wideSecDerLimits[0] or ymax20 > wideSecDerLimits[1]:
        axs[2, 0].set_ylim(wideSecDerLimits)
    axs[1, 0].legend()
    if filename == "none" or filename == "None":
        plt.show()
    else:
        plt.savefig(filename, format="pdf", bbox_inches="tight")
        plt.close()

def main(argv):
    # Parse command line options
    argc = len(argv)
    if (argc == 0):
        # Convention used here: command invoked without any arguments
        # prints its usage instruction and exits successfully
        print(__doc__)
        return 0
    elif (argc >= 2):
        # We might have the correct number of arguments
        rightSigma = float(argv[0])
        if rightSigma <= 0.0:
            print("rightSigma parameter must be positive")
            return 1
        filename = argv[1]
        classes = [getattr(ase, name) for name in argv[2:]]
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Always use BrokenParabola as a reference
    classes.insert(0, ase.BrokenParabola)
    # Call the code which does the job
    make_plot(classes, rightSigma, filename)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

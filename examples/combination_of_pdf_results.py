#!/usr/bin/env python3
"""
This script illustrates the combination of results example in the
section "Combination of pdf results" of the "Asymmetric Errors" paper
using all pdf models implemented in the package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.3"
__date__ ="May 30 2024"

import asepy as ase
from asepy_utils import combineTwoPdfResultsOneModel, fromQuantilesPdfs

# The default safety interval will not work for Edgeworth
# expansion with this example. It has to be reduced.
ase.EdgeworthExpansion3.setClassSafeSigmaRange(2.5)

def combineAndPrint(r1, r2):
    for cl in fromQuantilesPdfs():
        print("\nModel:", cl.__name__)
        r = combineTwoPdfResultsOneModel(r1, r2, cl)
        print("Result:", r.fstr(":.3f"))

print("** Calculating first row in Table 3")
sigmaPlus = 7.5710678118654752
sigmaMinus = sigmaPlus - 1.0
r1 = ase.AsymmetricEstimate(32.571067811865475, sigmaPlus, sigmaMinus, ase.P)
r2 = ase.AsymmetricEstimate(18.428932188134525, sigmaPlus, sigmaMinus, ase.P)
combineAndPrint(r1, r2)

print("\n** Calculating second row in Table 3")
r1 = ase.AsymmetricEstimate(41.142135623730950, sigmaPlus, sigmaMinus, ase.P)
r2 = ase.AsymmetricEstimate(12.857864376269050, sigmaPlus, sigmaMinus, ase.P)
combineAndPrint(r1, r2)

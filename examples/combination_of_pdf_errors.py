#!/usr/bin/env python3
"""
This script shows how to reproduce the example in the section "Combination
of pdf errors" of the "Asymmetric Errors" paper using all pdf models
implemented in the package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.3"
__date__ ="May 30 2024"

import asepy as ase
from asepy_utils import combineTwoPdfErrorsOneModel, fromQuantilesPdfs

# The default safety interval will not work for Edgeworth
# expansion with this example. It has to be reduced.
ase.EdgeworthExpansion3.setClassSafeSigmaRange(2.0)

def formatResult(r):
    return "{:.2f}, {:.2f}, {:.3f}".format(
        r.sigmaMinus(), r.sigmaPlus(), r.location())

def combineAndPrint(rx, ry):
    for cl in fromQuantilesPdfs():
        print("\nModel:", cl.__name__)
        try:
            r = combineTwoPdfErrorsOneModel(rx, ry, cl)
        except Exception as e:
            print(str(e))
        else:
            print("Result (sm, sp, delta):", formatResult(r))

cases = ((1.0, 1.0, 0.8, 1.2),
         (0.8, 1.2, 0.8, 1.2),
         (0.5, 1.5, 0.8, 1.2),
         (0.5, 1.5, 0.5, 1.5))
for row, (smx, spx, smy, spy) in enumerate(cases):
    print("\n*** Calculating row", row+3, "in Table 2 ***")
    rx = ase.AsymmetricEstimate(0.0, spx, smx, ase.P)
    ry = ase.AsymmetricEstimate(0.0, spy, smy, ase.P)
    print("Inputs: {}, {}".format(rx.fstr(":.3f"), ry.fstr(":.3f")))
    combineAndPrint(rx, ry)

#!/usr/bin/env python3
"""
This script shows how to reproduce the example in the section
"A lifetime measurement" of the "Asymmetric Errors" paper using
all log-likelihood models implemented in the package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase

from asepy_utils import logliCurve, logliResult, \
    combineMultipleLogliResultsOneModel, DensityBasedLogli, \
    distrosUsableInLikelihoods, allStandardLogliModels

from ProfileLogliOfASum import ProfileLogliOfASum

def combineLogliErrors(inputs, classObj):
    for nset in inputs:
        try:
            curves = []
            for n in nset:
                ll = ase.PoissonLogli(n)
                r = logliResult(ll)
                curves.append(logliCurve(r, classObj))
            ll = ProfileLogliOfASum(curves)
            r = logliResult(ll)
            print(nset, "result:", r.fstr(":.3f"))
        except Exception as e:
            print(nset, repr(e))

n_table6 = 9
ll = ase.PoissonLogli(n_table6)
r = logliResult(ll)
print("True result is", r.fstr(":.3f"))

inputs = ((4, 5),
          (3, 6),
          (2, 7),
          (1, 8),
          (3, 3, 3),
          (1, 1, 1, 1, 1, 1, 1, 1, 1))

for cl in allStandardLogliModels():
    print("\nModel:", cl.__name__)
    combineLogliErrors(inputs, cl)

for distro in distrosUsableInLikelihoods():
    print("\nLog-likelihood of:", distro.__name__)
    adapter = DensityBasedLogli(distro)
    r = combineLogliErrors(inputs, adapter)

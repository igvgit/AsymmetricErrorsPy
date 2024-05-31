#!/usr/bin/env python3
"""
This script illustrates the combination of results example in the section
"Combination of Results using likelihood" of the "Asymmetric Errors" paper
using all log-likelihood models implemented in the package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase

from asepy_utils import combineMultipleLogliResultsOneModel, \
    DensityBasedLogli, distrosUsableInLikelihoods, allStandardLogliModels

r1 = ase.AsymmetricEstimate(1.9, 0.7, 0.5, ase.L)
r2 = ase.AsymmetricEstimate(2.4, 0.6, 0.8, ase.L)
r3 = ase.AsymmetricEstimate(3.1, 0.5, 0.4, ase.L)
results = (r1, r2, r3)

for cl in allStandardLogliModels():
    print("\nModel:", cl.__name__)
    try:
        r = combineMultipleLogliResultsOneModel(results, cl)
    except Exception as e:
        print(repr(e))
    else:
        print("Result:", r.fstr(":.3f"))

for distro in distrosUsableInLikelihoods():
    print("\nLog-likelihood of:", distro.__name__)
    try:
        adapter = DensityBasedLogli(distro)
        r = combineMultipleLogliResultsOneModel(results, adapter)
    except Exception as e:
        print(repr(e))
    else:
        print("Result:", r.fstr(":.3f"))

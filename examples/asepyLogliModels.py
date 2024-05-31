#!/usr/bin/env python3
"""
Print the names of all asepy log-likelihood models
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

from asepy_utils import allStandardLogliModels, distrosUsableInLikelihoods

print("Classes representing log-likelihood curves in the asepy package:")
print("----------------------------------------------------------------")

for cl in allStandardLogliModels():
    print(cl.__name__)

for distro in distrosUsableInLikelihoods():
    print("DistributionLogli({})".format(distro.__name__))

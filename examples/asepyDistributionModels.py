#!/usr/bin/env python3
"""
Print the names of all asepy probability distribution models
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy
import inspect

print("Classes representing probability distributions in the asepy package:")
print("--------------------------------------------------------------------")

for name, cl in inspect.getmembers(asepy, inspect.isclass):
    if issubclass(cl, asepy.AbsDistributionModel1D):
        if not (name == "AbsDistributionModel1D" or
                name == "AbsLocationScaleFamily" or
                name == "DistributionModel1DCopy" or
                name[:12] == "OPATGaussian"):
            print(name)

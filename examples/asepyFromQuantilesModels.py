#!/usr/bin/env python3
"""
Print the names of asepy probability distribution models that can be
constructed from quantiles (as needed, for example, in combining pdf errors)
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

from asepy_utils import fromQuantilesPdfs

print("Pdf models that can be constructed from quantiles:")
print("--------------------------------------------------")
for cl in fromQuantilesPdfs():
    print(cl.__name__)

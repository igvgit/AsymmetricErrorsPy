#!/usr/bin/env python3
"""
Print the names of asepy "fully OPAT compatible" pdf models
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

from asepy_utils import fullOPATPdfs

print("Fully OPAT compatible Pdf models")
print("--------------------------------")
for cl in fullOPATPdfs():
    print(cl.__name__)

#!/usr/bin/env python3
"""
The code below shows how to combine log-likelihood results with
the asepy package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 2 2024"

import asepy as ase
from asepy_utils import combineTwoLogliResults, combineMultipleLogliResults, \
    combineTwoLogliResultsOneModel, combineMultipleLogliResultsOneModel, \
    DensityBasedLogli

# Top-level asepy interface for combining log-likelihood results
# consists of four functions defined in the asepy_utils module:
#
# 1) combineTwoLogliResults -- general function for combining two results.
#                              It allows you to specify different models
#                              for each input. Run the script
#                              "asepyLogliModels.py" to see the list of
#                              available log-likelihood models.
#
# 2) combineTwoLogliResultsOneModel -- simplified function for combining
#                                      two results, useful in case you want
#                                      to use the same log-likelihood model
#                                      for both inputs.
#
# 3) combineMultipleLogliResults -- general function for combining
#                                   an arbitrary number of log-likelihood
#                                   results.
#
# 4) combineMultipleLogliResultsOneModel -- simplified function for combining
#                                           an arbitrary number of results.
#
# Now, let's construct some results and illustrate the usage of the
# relevant functions. Note that the type of results should be "ase.L".
r1 = ase.AsymmetricEstimate(8.2, 1.2, 0.8, ase.L)
r2 = ase.AsymmetricEstimate(7.1, 0.5, 0.7, ase.L)
r3 = ase.AsymmetricEstimate(5.3, 2.1, 1.5, ase.L)

# Combine r1 and r2 utilizing one log-likelihood model for both inputs
# (here, BrokenParabola)
combined1 = combineTwoLogliResultsOneModel(r1, r2, ase.BrokenParabola)
print("Combined result 1 is", combined1.fstr(":.3f"))

# Combine r1 and r2 utilizing separate models
combined2 = combineTwoLogliResults(r1, ase.MoldedDoubleQuartic,
                                   r2, ase.MoldedDoubleQuintic)
print("Combined result 2 is", combined2.fstr(":.3f"))

# Combine r1, r2, and r3 utilizing one log-likelihood model for all inputs
inputs = (r1, r2, r3)
combined3 = combineMultipleLogliResultsOneModel(inputs, ase.BrokenParabola)
print("Combined result 3 is", combined3.fstr(":.3f"))

# Combine r1, r2, and r3 utilizing separate models
inputModels = (ase.MoldedDoubleQuartic, ase.MoldedDoubleQuintic,
               ase.VariableLogSigma)
combined4 = combineMultipleLogliResults(inputs, inputModels)
print("Combined result 4 is", combined4.fstr(":.3f"))

# Log-likelihood models can also be constructed out of pdfs, using
# log of the density. In order to construct such a model usable with
# all of the functions described above, utilize the "DensityBasedLogli"
# adapter class defined in the asepy_utils module:
model = DensityBasedLogli(ase.SkewNormal)
combined5 = combineTwoLogliResultsOneModel(r1, r2, model)
print("Combined result 5 is", combined5.fstr(":.3f"))

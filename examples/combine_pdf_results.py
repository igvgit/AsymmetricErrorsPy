#!/usr/bin/env python3
"""
The code below shows how to combine pdf results with the asepy package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

import asepy as ase
from asepy_utils import combineTwoPdfResults, combineTwoPdfResultsOneModel, \
    combineMultiplePdfResults, combineMultiplePdfResultsOneModel

# Top-level asepy interface for combining pdf results consists of four
# functions defined in the asepy_utils module:
#
# 1) combineTwoPdfResults -- general function for combining two
#                            results. It allows you to specify
#                            different models for each input as
#                            well as for the output.
#
# 2) combineTwoPdfResultsOneModel -- simplified function for combining two
#                                    results, useful in case you want to
#                                    use the same pdf model for everything.
#
# 3) combineMultiplePdfResults -- general function for combining
#                                 an arbitrary number of results.
#
# 4) combineMultiplePdfResultsOneModel -- simplified function for combining
#                                         an arbitrary number of results.
#
# Combining pdf results is in some sense simpler than combining pdf
# errors because in this case all uncertainies are expected to be positive
# and there is no reason to consider OPAT compatibility of the models.
# All models printed by the "asepyFromQuantilesModels.py" script are
# potential candidates.
#
# Now, let's construct some results and illustrate the usage of the
# relevant functions.
r1 = ase.AsymmetricEstimate(8.2, 1.2, 0.8, ase.P)
r2 = ase.AsymmetricEstimate(7.1, 0.5, 0.7, ase.P)
r3 = ase.AsymmetricEstimate(5.3, 2.1, 1.5, ase.P)

# Combine r1 and r2 utilizing one pdf model for everything
# (here, SkewNormal)
combined1 = combineTwoPdfResultsOneModel(r1, r2, ase.SkewNormal)
print("Combined result 1 is", combined1.fstr(":.3f"))

# Combine r1 and r2 utilizing separate models for them. The last
# argument specifies the model to use for the combined result.
combined2 = combineTwoPdfResults(r1, ase.DimidiatedGaussian,
                                 r2, ase.DistortedGaussian,
                                 ase.RailwayGaussian)
print("Combined result 2 is", combined2.fstr(":.3f"))

# Combine r1, r2, and r3 utilizing one pdf model for everything
inputResults = (r1, r2, r3)
combined3 = combineMultiplePdfResultsOneModel(inputResults, ase.SkewNormal)
print("Combined result 3 is", combined3.fstr(":.3f"))

# Combine r1, r2, and r3 utilizing separate models
inputModels = (ase.DimidiatedGaussian, ase.DistortedGaussian, ase.SkewNormal)
combinedModel = ase.QVWGaussian
combined4 = combineMultiplePdfResults(inputResults, inputModels, combinedModel)
print("Combined result 4 is", combined4.fstr(":.3f"))

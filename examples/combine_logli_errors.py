#!/usr/bin/env python3
"""
The code below shows how to combine log-likelihood errors with the
asepy package. Note that combining log-likelihood (i.e., statistical)
asymmetric errors is rather unusual, at least in the HEP practice.
Please make sure that you are doing the right thing.
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 3 2024"

import asepy as ase
from asepy_utils import combineTwoLogliErrors, combineMultipleLogliErrors, \
    combineTwoLogliErrorsOneModel, combineMultipleLogliErrorsOneModel, \
    DensityBasedLogli

# Top-level asepy interface for combining log-likelihood errors
# consists of four functions defined in the asepy_utils module:
#
# 1) combineTwoLogliErrors -- general function for combining two errors.
#                             It allows you to specify different models
#                             for each input. Run the script
#                             "asepyLogliModels.py" to see the list of
#                             available log-likelihood models.
#
# 2) combineTwoLogliErrorsOneModel -- simplified function for combining
#                                     two results, useful in case you want
#                                     to use the same log-likelihood model
#                                     for both inputs.
#
# 3) combineMultipleLogliErrors -- general function for combining
#                                  an arbitrary number of log-likelihood
#                                  errors.
#
# 4) combineMultipleLogliErrorsOneModel -- simplified function for combining
#                                          an arbitrary number of errors.
#
# Now, let's construct some errors and illustrate the usage of the
# relevant functions. Note that the type of estimates should be "ase.L".
e1 = ase.AsymmetricEstimate(0.0, 1.2, 0.8, ase.L)
e2 = ase.AsymmetricEstimate(0.0, 0.5, 0.7, ase.L)
e3 = ase.AsymmetricEstimate(0.0, 2.1, 1.5, ase.L)

# Combine e1 and e2 utilizing one log-likelihood model for both inputs
# (here, BrokenParabola)
combined1 = combineTwoLogliErrorsOneModel(e1, e2, ase.BrokenParabola)
print("Combined error 1 is", combined1.fstr(":.3f"))

# Combine e1 and e2 utilizing separate models
combined2 = combineTwoLogliErrors(e1, ase.MoldedDoubleQuartic,
                                   e2, ase.MoldedDoubleQuintic)
print("Combined error 2 is", combined2.fstr(":.3f"))

# Combine e1, e2, and e3 utilizing one log-likelihood model for all inputs
inputs = (e1, e2, e3)
combined3 = combineMultipleLogliErrorsOneModel(inputs, ase.BrokenParabola)
print("Combined error 3 is", combined3.fstr(":.3f"))

# Combine e1, e2, and e3 utilizing separate models
inputModels = (ase.MoldedDoubleQuartic, ase.MoldedDoubleQuintic,
               ase.VariableLogSigma)
combined4 = combineMultipleLogliErrors(inputs, inputModels)
print("Combined error 4 is", combined4.fstr(":.3f"))

# Log-likelihood models can also be constructed out of pdfs, using
# log of the density. In order to construct such a model usable with
# all of the functions described above, utilize the "DensityBasedLogli"
# adapter class defined in the asepy_utils module:
model = DensityBasedLogli(ase.SkewNormal)
combined5 = combineTwoLogliErrorsOneModel(e1, e2, model)
print("Combined error 5 is", combined5.fstr(":.3f"))

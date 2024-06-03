#!/usr/bin/env python3
"""
The code below shows how to combine two pdf errors with the asepy package
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

import asepy as ase
from asepy_utils import combineTwoPdfErrors, combineTwoPdfErrorsOneModel, \
    OPATError

# Consider the case of combining two pdf (i.e., systematic) errors
# produced in the OPAT analysis. Suppose that, when you vary some
# nuisance parameter by 1 sigma up, the parameter of interest increases
# by 1.2, and when you vary that nuisance parameter by 1 sigma down,
# the parameter of interest decreases by 0.8. In this case your
# positive error is 1.2 and negative error is 0.8, usually notated
# mathematically as ^{+1.2}_{-0.8}. Asepy package represents such
# errors by
e1 = ase.AsymmetricEstimate(0.0, 1.2, 0.8, ase.P)

# There is also a function "OPATError" in the asepy_utils module
# designed specifically to represent the results of an OPAT analysis.
# It will automatically set the location parameter of the AsymmetricEstimate
# to 0, the type to ase.P, and, if both OPAT shifts are negative, it
# will convert them to positive (with a swap). So, suppose that you also
# have another nuisance parameter, and the results of its variation are
# represented by
e2 = OPATError(0.5, 0.7)

# The simplest way to combine these errors is to assume that both
# the input estimates and the combined result follow the same pdf
# model. When all errors are of the same sign and the positive
# errors are comparable to the negative errors in magnitude, you have
# a wide choice of models. Run the script "asepyFromQuantilesModels.py"
# to see all pdf models that can be used in this context. Here,
# we choose one for the sake of this example.
pdfmodel = ase.SkewNormal

# This kind of combination can be performed with the help of the
# "combineTwoPdfErrorsOneModel" function from the asepy_utils module:
combinedError1 = combineTwoPdfErrorsOneModel(e1, e2, pdfmodel)

# Pretty-print the combined error using 3 digits after the dot.
# Note that the central value of the combined error is no longer 0.
# To debias your parameter of interest estimate, you need to shift
# your estimate by that central value.
print("Combined error 1 is", combinedError1.fstr(":.3f"))

# You are not limited to using the same pdf model for everything.
# In fact, you can choose separate models for both inputs as well as
# for the combination. Choosing different models can be advantageous
# if, let say, in your OPAT analysis you investigated more points
# than just 1 sigma up and down. In this case you can find a model
# whose transformation from the standard normal (function
# "qqmapFromStandardNormal" in the asepy_utils module) fits your
# OPAT analysis points better. Or your modeling preferences can
# be based on some other information you might have. Ideally, the
# pdf of the result model should be consistent with the convolution
# of the input pdfs, and that might affect your choice of the
# result model. The code below shows how to combine errors using
# different models with the "combineTwoPdfErrors" function from
# the asepy_utils module.
model1 = ase.SymmetricBetaGaussian_1_10
model2 = ase.SymmetricBetaGaussian_2_20
resultModel = ase.LogNormal
combinedError2 = combineTwoPdfErrors(e1, model1, e2, model2, resultModel)
print("Combined error 2 is", combinedError2.fstr(":.3f"))

# If one of the asymmetric errors you are combining has positive
# and negative errors of different signs (i.e., OPAT analysis deviations
# are in the same direction), you should utilize a "fully OPAT compatible"
# model for that error. Run the script "asepyFullOPATModels.py" to see
# the list of such models. Below, we construct such an error and rerun
# the combination using it instead of e1.
e3 = ase.AsymmetricEstimate(0.0, -1.2, 0.8, ase.P)

# SkewNormal used earlier would no longer work with
# the "combineTwoPdfErrorsOneModel" function. Must use
# one of the fully OPAT compatible models instead.
combinedError3 = combineTwoPdfErrorsOneModel(e3, e2, ase.RailwayGaussian)
print("Combined error 3 is", combinedError3.fstr(":.3f"))

# If you use a different model for the result, your result model does
# not have to be "fully OPAT compatible". The snippet below works
# because all variants of "SymmetricBetaGaussian" are fully OPAT compatible
# even though the LogNormal is not.
combinedError4 = combineTwoPdfErrors(e3, model1, e2, model2, resultModel)
print("Combined error 4 is", combinedError4.fstr(":.3f"))

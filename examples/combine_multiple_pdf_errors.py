#!/usr/bin/env python3
"""
The code below shows how to combine multiple pdf errors with the asepy
package. The basic principles are the same as for combining two pdf
errors. It can be useful to review the script "combine_two_pdf_errors.py"
if you have not done that already, comments in this script are not as
detailed.
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="June 1 2024"

import asepy as ase
from asepy_utils import combineMultiplePdfErrors, \
    combineMultiplePdfErrorsOneModel, OPATError

# Case 1: all errors are positive. An arbitrary number of errors
# can be specified, we are using three in this example.
e1 = OPATError(1.2, 0.8)
e2 = OPATError(0.5, 0.7)
e3 = OPATError(2.1, 1.5)
allErrors = (e1, e2, e3)

# If you want to use the same pdf model for all of the errors as well
# as for the combination, in this case you can choose any of the models
# printed by the "asepyFromQuantilesModels.py" script. The function
# to use is "combineMultiplePdfErrorsOneModel" from the asepy_utils
# module. The first argument of that function is the list or tuple
# of errors and the second one is the model to use.
combinedError1 = combineMultiplePdfErrorsOneModel(allErrors, ase.LogNormal)
print("Combined error 1 is", combinedError1.fstr(":.3f"))

# If you want to use different pdf models, you need to specify the
# models for each input as well as for the combination. Then you can
# use the "combineMultiplePdfErrors" function.
model1 = ase.SymmetricBetaGaussian_1_10
model2 = ase.SymmetricBetaGaussian_2_20
model3 = ase.SymmetricBetaGaussian_3_30
inputModels = (model1, model2, model3) # These will be used with
                                       # e1, e2, e3, respectively
resultModel = ase.QVWGaussian
combinedError2 = combineMultiplePdfErrors(allErrors, inputModels, resultModel)
print("Combined error 2 is", combinedError2.fstr(":.3f"))

# Case 2: some errors are negative
e4 = OPATError(-1.2, 0.8)
e5 = OPATError(0.5, 0.7)
e6 = OPATError(2.1, -1.5)
newErrors = (e4, e5, e6)

# In this case, if you want to use the same pdf model for everything,
# it must be fully OPAT compatible (run "asepyFullOPATModels.py" to
# print the list)
combinedError3 = combineMultiplePdfErrorsOneModel(newErrors,
                                                  ase.DoubleCubicGaussian)
print("Combined error 3 is", combinedError3.fstr(":.3f"))

# If you want to specify models separately, the inputs with negative
# errors must correspond to fully OPAT compatible models
mod1 = ase.RailwayGaussian
mod2 = ase.SkewNormal  # This one does not have to be fully OPAT compatible
newModels = (mod1, mod2, mod1)
combinedError4 = combineMultiplePdfErrors(newErrors, newModels, resultModel)
print("Combined error 4 is", combinedError4.fstr(":.3f"))

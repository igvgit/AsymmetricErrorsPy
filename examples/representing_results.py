#!/usr/bin/env python3
"""
This script illustrates the usage of AsymmetricEstimate class for
representing results with asymmetric errors
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 31 2024"

import asepy as ase

# The asepy package class "AsymmetricEstimate" is used to represent
# results with asymmetric uncertainties.
#
# The AsymmetricEstimate constructor has four arguments: the central
# value, the positive error, the negative error, and the type of error.
# The type can have two possible values: ase.P (for pdf, or systematic
# uncertainties) and ase.L (for likelihood, or statistical uncertainties).
# Here is an example:
mu = 1.234
sigmaPlus = 5.678
sigmaMinus = 3.456
r1 = ase.AsymmetricEstimate(mu, sigmaPlus, sigmaMinus, ase.L)

# Systematic uncertainties can arise from an OPAT (one parameter
# at a time) analysis and can be negative. Statistical uncertainties
# are required to be non-negative. The following will work fine:
sigmaPlus = -5.678
r2 = ase.AsymmetricEstimate(mu, sigmaPlus, sigmaMinus, ase.P)

# At the same time, the following will generate an exception:
try:
    r3 = ase.AsymmetricEstimate(mu, sigmaPlus, sigmaMinus, ase.L)
except Exception as e:
    print("Exception generated for a negative statistical uncertainty:")
    print(repr(e))
else:
    print("Negative statistical uncertainties are OK !???")

# The result objects can be simply printed:
print("Result 1 is", r1)
print("Result 2 is", r2)

# The Python API adds the method "fstr" (formatted string) which
# allows for simultaneous formatting of the central value and of
# both uncertainties using the same python format specifier.
# The result type is not included in this string representation.
# The results with non-negative uncertainties have more natural
# string representations.
print("Formatted result 1 string is", r1.fstr(":.2f"))
print("Formatted result 2 string is", r2.fstr(":.2f"))

# Of course, various result components can be examined individually:
print("Result 1 central value is", r1.location())
print("Result 1 positive error is", r1.sigmaPlus())
print("Result 1 negative error is", r1.sigmaMinus())
print("Result 1 type is", r1.errorType())

# If both uncertainties have the same sign, couple convenience
# methods can be called as well: "width" (absolute value of the
# symmetrized uncertainty) and "asymmetry". The asymmetry is
# defined as (sigmaPlus - sigmaMinus)/(sigmaPlus + sigmaMinus)
# if both uncertainties are positive and as
# (|sigmaMinus| - |sigmaPlus|)/(|sigmaPlus| + |sigmaMinus|)
# if both uncertainties are negative. If the uncertainties have
# opposite signs, these methods will throw exceptions.
print("Result 1 width is", r1.width())
print("Result 1 asymmetry is", r1.asymmetry())

r4 = ase.AsymmetricEstimate(0.0, -2.0, -1.0, ase.P)
print("Result 4 is", r4)
print("Result 4 width is", r4.width())
print("Result 4 asymmetry is", r4.asymmetry())

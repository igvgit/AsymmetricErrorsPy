#!/usr/bin/env python3
"""
This script demonstrates how to generate random numbers according to
a distribution supported by asepy
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 31 2024"

import asepy as ase

# The first thing to do is to instantiate a random number generator.
# asepy comes equipped with three generator classes:
#
# 1) DRand48 class is a wrapper for the standard C generator
#    function drand48(). This generator always makes a fixed
#    sequence of pseudo-random numbers.
#
# 2) MersenneTwister32 is a wrapper for the standard C++ generator
#    class std::mt19937.
#
# 3) MersenneTwister64 is a wrapper for the standard C++ generator
#    class std::mt19937_64.
#
# If you want MersenneTwister32 and MersenneTwister64 to generate
# a fixed sequence of numbers (for repeatable program runs), give
# their constructors a positive seed argument. Ideally, the seed
# should be a large prime (but less than 2**31). To generate sequences,
# that vary every time the program runs, use the seed value of 0
# or omit the seed argument.
seed = 224284387
rng = ase.MersenneTwister64(seed)

# You can now call rng() to generate random numbers on the
# interval [0, 1) one by one. To obtain random numbers distributed
# according to some distribution, construct that distribution.
# Here is an example:
distro = ase.SkewNormal(-1.0, 0.5, 1.3)

# You can now call the "random" method of the distribution
# object to generate random numbers one by one:
for i in range(5):
    print("Next random number is", distro.random(rng))

# You can also call the "generate" method to make a sequence
# of random numbers:
seq = distro.generate(rng, 4)
print("Generated", len(seq), "random numbers at once:", seq)

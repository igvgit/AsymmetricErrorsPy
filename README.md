# AsymmetricErrorsPy
Python API for modeling asymmetric errors. This code accompanies the
"Asymmetric Errors" paper by R. Barlow, A.R. Brazzale, and I. Volobouev.
To install this package on your computer, download or clone the repository
or the latest package release from GitHub (check
[these tips](https://zapier.com/blog/how-to-download-from-github/)
if you are not sure how to do that),
unpack the downloaded archive if necessary, and then follow the instructions
in the [INSTALL](./INSTALL) file. In order to learn how to exploit
the capabilities of this software, follow the tutorial examples in
the [examples](./examples) directory.

## Probability Distribution Models
In its Appendix A, the "Asymmetric Errors" paper provides
mathematical descriptions for a number of probability distributions
that can be used to model asymmetric pdf (i.e., systematic) errors.
In this package, these distributions are implemented with a number
of classes, all of them inheriting their interface from the
[AbsDistributionModel1D](https://github.com/igvgit/AsymmetricErrors/blob/main/ase/AbsDistributionModel1D.hh)
base class. The following table lists classes
corresponding to various Appendix A subsections:
| Appendix A Subsection                |  Class Name           |
| ------------------------------------ | --------------------- |
| The Dimidiated Gaussian              | DimidiatedGaussian    |
| The Distorted Gaussian               | DistortedGaussian     |
| The “Railway” Gaussian               | RailwayGaussian       |
| The Double Cubic Gaussian            | DoubleCubicGaussian   |
| The Symmetric Beta Gaussian          | SymmetricBetaGaussian |
| The Quantile Variable Width Gaussian | QVWGaussian           |
| The Fechner distribution             | FechnerDistribution   |
| The Edgeworth expansion              | EdgeworthExpansion3   |
| The Skew Normal                      | SkewNormal            |
| The Johnson system                   | JohnsonSystem         |
| The Log-normal                       | LogNormal             |

Declarations and constructor signatures for these classes can be found in the
[DistributionModels1D.hh](https://github.com/igvgit/AsymmetricErrors/blob/main/ase/DistributionModels1D.hh)
header file (Python and C++ constructor signatures are identical).

The creation methods of the "SymmetricBetaGaussian" model have
non-standard signatures, as this model requires additional parameters _p_ and _h_.
To facilitate iterations over model sequences, this package introduces a number
of classes with predefined values of _p_ and _h_ all which are named like 
"SymmetricBetaGaussian_P_N", for example, "SymmetricBetaGaussian_2_15".
Here, "P" in the class name refers to the value of _p_ and "N" refers
to the value of _h_*10. Thus, for the "SymmetricBetaGaussian_2_15"
model, _p_ = 2 and _h_ = 1.5.

The package also includes a number of models which are not necessarily useful for representing
asymmetric errors but could be employed for other purposes.
Here is a table of such models, current at the time of this writing:
|  Class Name             |  Description     |
|-------------------------|------------------|
| EmpiricalDistribution   | Empirical distribution corresponding to a sample of unweighted points |
| ExponentialDistribution | The exponential distribution |
| GammaDistribution       | The Gamma distribution |
| Gaussian                | The Gaussian distribution (symmetric) |
| InterpolatedDensity1D   | A distribution whose discretized density curve is interpolated by cubic Hermite splines |
| LegendreDistro1D        | A distribution whose density is specified by a Legendre polynomial series expansion |
| MixtureModel1D          | A mixture of other distributions |
| TabulatedDensity1D      | A distribution whose discretized density curve is interpolated linearly between the points |
| TruncatedDistribution1D | A distribution obtained by truncating the support interval of another distribution |
| UniformDistribution     | The uniform distribution on a compact interval |

Run the script [asepyDistributionModels.py](./examples/asepyDistributionModels.py)
in the "examples" directory to print the current list of implemented
distribution models.

## Log-likelihood Models
In its Appendix B, the "Asymmetric Errors" paper provides
mathematical descriptions for a number of log-likelihood
curves that can be used to model asymmetric statistical errors.
In this package, these curves are implemented with a number
of classes, all of them inheriting their interface from the
[AbsLogLikelihoodCurve](https://github.com/igvgit/AsymmetricErrors/blob/main/ase/AbsLogLikelihoodCurve.hh)
base class. The following table lists classes
corresponding to various Appendix B subsections:
| Appendix B Subsection                |  Class Name(s)        |
| ------------------------------------ | --------------------- |
| The cubic | TruncatedCubicLogli |
| The broken parabola | BrokenParabola |
| The symmetrized parabola | SymmetrizedParabola |
| The constrained quartic | ConstrainedQuartic |
| The molded quartic | MoldedQuartic |
| The matched quintic | MatchedQuintic  |
| The interpolated 7th degree polynomial | Interpolated7thDegree |
| The double quartic | SimpleDoubleQuartic, MoldedDoubleQuartic |
| The double quintic | SimpleDoubleQuintic, MoldedDoubleQuintic |
| The conservative spline | ConservativeSpline, ConservativeSigma05, ConservativeSigma10, ConservativeSigma15, ConservativeSigma20, ConservativeSigmaMax |
| The log logistic-beta | LogLogisticBeta |
| The logarithmic | LogarithmicLogli |
| The generalised Poisson | GeneralisedPoisson |
| The linear sigma | VariableSigmaLogli |
| The linear variance | VariableVarianceLogli |
| The linear sigma in the log space | VariableLogSigma |
| The double cubic sigma in the log space | MoldedCubicLogSigma |
| The quintic sigma in the log space | QuinticLogSigma |
| The PDG method | PDGLogli |
| The Edgeworth expansion | Not implemented |
| The skew normal | DistributionLogli(SkewNormal) |

In addition to the skew-normal distribution, a number of other
distribution models can be used for building log-likelihood curves
by calculating the log of the density. The method used to
construct such log-likelihoods is described in the the script
[constructing_likelihoods.py](./examples/constructing_likelihoods.py)
found in the "examples" directory.

Run the script [asepyLogliModels.py](./examples/asepyLogliModels.py)
in the "examples" directory to print the current list of implemented
log-likelihood models.

Special log-likelihood models implemented in the package include
|  Class Name                |  Description     |
|----------------------------|------------------|
| CubicHermiteInterpolatorEG | A discretized log-likelihood curve interpolated by cubic Hermite splines |
| PoissonLogli               | Log-likelihood for the parameter of the Poisson distribution |

These models might not have standard constructors and could
be skipped in the output of the "asepyLogliModels.py" script.

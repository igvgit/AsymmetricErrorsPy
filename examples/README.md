The scripts in this directory present the Python API of the code
accompanying the "Asymmetric Errors" paper in a tutorial fashion.
Read them, run them, modify them, and see what happens.

## Basic Top-level API

I recommend exploring the basic usage of the package API in the
following order:

* [representing_results.py](./representing_results.py)
This script demonstrates how results with asymmetric errors are
represented in the software.

* [combine_two_pdf_errors.py](./combine_two_pdf_errors.py)
Example scripts illustrating the utility functions that can be used to combine
two pdf (i.e., systematic) uncertainties.

* [combine_multiple_pdf_errors.py](./combine_multiple_pdf_errors.py)
Example scripts showing how to combine multiple pdf (i.e., systematic) uncertainties.

* [combine_pdf_results.py](./combine_pdf_results.py)
Example scripts showing how to combine results with pdf uncertainties.

* [combine_logli_results.py](./combine_logli_results.py)
Example scripts showing how to combine results with log-likelihood
(i.e., statistical) uncertainties.

* [combine_logli_results_plot.py](./combine_logli_results_plot.py)
Example scripts showing how to plot input log-likelihood curves
in a combination together with their combined result.

* [combine_logli_errors.py](./combine_logli_errors.py)
Example scripts showing how to combine asymmetric log-likelihood errors.

## Which Models are Available?

* [asepyDistributionModels.py](./asepyDistributionModels.py)
This script prints the list of all distribution (pdf) models
provided by the software.

* [asepyFromQuantilesModels.py](./asepyFromQuantilesModels.py)
This script prints the list of all distributions models that can be
constructed from quantiles (as needed, for example, in combining pdf errors).

* [asepyFullOPATModels.py](./asepyFullOPATModels.py)
This script prints the list of all distributions models that are fully
compatible with results of an OPAT (one parameter at a time) analysis
of systematic uncertainties.

* [asepyLogliModels.py](./asepyLogliModels.py)
Print the list of available log-likelihood models.

## Using Multiple Models

Use of multiple pdf and log-likelihood models in various combination scenarios
is illustrated by the following scripts:

* [combination_of_pdf_errors.py](./combination_of_pdf_errors.py)

* [combination_of_pdf_results.py](./combination_of_pdf_results.py)

* [combination_of_logli_errors.py](./combination_of_logli_errors.py)

* [combination_of_logli_results.py](./combination_of_logli_results.py)

## Exploring Model Properties

* [lognormal_example.py](./lognormal_example.py)
This example shows how to plot a probability distribution density
(in this case, of log-normal, but you are invited to modify that)
and a function which transform a standard normal into this distribution.

* [plot_distribution_logli.py](./plot_distribution_logli.py)
This example shows how to construct and plot log-likelihood models
produced by calculating logs of probability densities. If you
run this script without any command line arguments, it prints its
usage instructions.

* [plot_distribution.py](./plot_distribution.py)
This example shows how to plot probability distribution density and cdf.
If you run this script without any command line arguments, it prints its
usage instructions.

* [plot_likelihood_curve.py](./plot_likelihood_curve.py)
This example shows how to plot a log-likelihood model. If you run this
script without any command line arguments, it prints its usage instructions.

* [plot_likelihood_derivative.py](./plot_likelihood_derivative.py)
This example shows how to plot log-likelihood model derivatives.
If you run this script without any command line arguments, it prints
its usage instructions.

* [plot_transform.py](./plot_transform.py)
This example shows how to plot a function (OPAT curve, also known
as the Q-Q plot) which transforms the standard normal into
the desired distribution. If you run this script without any command
line arguments, it prints its usage instructions.

* [railway_transform.py](./railway_transform.py)
This script demonstrates a transform used to construct the railway Gaussian
distribution, together with its derivatives.

* [show_likelihood_shapes.py](./show_likelihood_shapes.py)
This script allows you to plot a mumber of log-likelihood models
simultaneously, together with their first and second derivatives.
If you run this script without any command line arguments, it prints
its usage instructions.

* [symbeta_gauss_densities.py](./symbeta_gauss_densities.py)
This scripts plots symmetric beta Gaussian densities corresponding to
a number of different shape parameters.

* [symbeta_transforms.py](./symbeta_transforms.py)
This scripts shows variable transforms used to generate symmetric beta
Gaussian distributions for a number of different shape parameters.

## Constructing Pdfs and Log-likelihoods

If you need to exploit some software capabilities beyond the top-level
combination functionality provided by the "asepy_utils" module, you will
most likely need to construct pdfs and/or log-likelihoods. The relevant
methods are presented by the scripts

* [constructing_likelihoods.py](./constructing_likelihoods.py)
This script illustrates various methods that can be used to construct
objects representing log-likelihoods.

* [constructing_pdfs.py](./constructing_pdfs.py)
This script illustrates construction of objects representing probability
distributions.

## Diving Deeper

* [check_cumulants.py](./check_cumulants.py)
This script can be used to check built-in formulae for calculating
distribution cumulants against their numerical estimates. If you run
this script without any command line arguments, it prints its usage
instructions.

* [example_convolution.py](./example_convolution.py)
An illustration of numerical convolution of two probability distributions.

* [example_interpolation.py](./example_interpolation.py)
This script demonstrates how the fidelity of mathematical function approximation
(e.g., of a log-likelihood model) by cubic Hermite splines depends on the number
of points used.

* [generating_random_numbers.py](./generating_random_numbers.py)
This scripts shows how to generate random numbers according to a given
probability distribution.

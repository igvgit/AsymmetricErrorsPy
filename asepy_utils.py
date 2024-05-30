import asepy as ase
import numpy as np
import inspect
import math

# Various scan... functions below can be used in two different ways:
#
# scan... object xmin xmax npoints
#
# This version returns a two-element tuple (xcoords, yvalues) that can be
# used for plotting (both xcoords and yvalues are numpy arrays).
#
# scan... object xcoords
#
# xcoords can be a sequence of doubles (list or tuple) or a numpy array.
# This version returns a numpy arrays of yvalues corresponding to xcoords.
#
def scanPythonCallable(fcn, *args):
    return ase.scanFunctor1D(ase.PyFunctor1(fcn), *args)

def scanLogLikelihood(curve, *args):
    return ase.scanFunctor1D(curve, *args)

def scanLogLikelihoodDerivative(curve, *args):
    deriv = ase.LogLikelihoodDerivative(curve)
    return ase.scanFunctor1D(deriv, *args)

def scanLogLikelihoodSecondDerivative(curve, step, *args):
    deriv2 = ase.LogLikelihoodSecondDerivative(curve, step)
    return ase.scanFunctor1D(deriv2, *args)

def scanLogLikelihoodSecondStep0(curve, *args):
    deriv2 = ase.LogLikelihoodSecondDerivative(curve, 0.0)
    return ase.scanFunctor1D(deriv2, *args)

def scanDensity(distro, *args):
    fcn = ase.DensityFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def scanDensityDerivative(distro, *args):
    fcn = ase.DensityDerivativeFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def scanCdf(distro, *args):
    fcn = ase.CdfFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def scanExceedance(distro, *args):
    fcn = ase.ExceedanceFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def scanInvExceedance(distro, *args):
    fcn = ase.InvExceedanceFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def scanQuantile(distro, *args):
    fcn = ase.QuantileFunctor1D(distro)
    return ase.scanFunctor1D(fcn, *args)

def intervalOverlap(xmin, xmax, ymin, ymax):
    if (xmax <= xmin):
        raise RuntimeError("Invalid first interval")
    if (ymax <= ymin):
        raise RuntimeError("Invalid second interval")
    if (xmax <= ymin or ymax <= xmin):
        raise RuntimeError("Intervals do not overlap")
    assert xmax > ymin and ymax > xmin
    return max(xmin, ymin), min(xmax, ymax)

def distributionCumulants(distro, n=None):
    if n is None:
        n = 4
    return np.array([distro.cumulant(i+1) for i in range(n)], dtype=np.double)

def numericCumulants(distro, xmin, xmax, quadPoints, quadIntervals):
    q0 = distro.quantile(0.0)
    q1 = distro.quantile(1.0)
    xmin, xmax = intervalOverlap(q0, q1, xmin, xmax)
    meanFcn = ase.MomentFunctor1D(distro, 0.0, 1)
    quad = ase.GaussLegendreQuadrature(quadPoints)
    mean = quad.integrate(meanFcn, xmin, xmax, quadIntervals)
    cumulants = np.empty(4, dtype=np.double)
    cumulants[0] = mean
    for n in range(1, 4):
        momFcn = ase.MomentFunctor1D(distro, mean, n+1)
        cumulants[n] = quad.integrate(momFcn, xmin, xmax, quadIntervals)
    cumulants[3] -= 3.0*cumulants[1]*cumulants[1]
    return cumulants

def gaussianRatioCumulants(distro, quadPoints, mu, sigma):
    g = ase.Gaussian(mu, sigma)
    meanFcn = ase.RatioMomentFunctor1D(distro, g, 0.0, 1)
    quad = ase.GaussHermiteQuadrature(quadPoints)
    mean = quad.integrateProb(mu, sigma, meanFcn)
    cumulants = np.empty(4, dtype=np.double)
    cumulants[0] = mean
    for n in range(1, 4):
        momFcn = ase.RatioMomentFunctor1D(distro, g, mean, n+1)
        cumulants[n] = quad.integrateProb(mu, sigma, momFcn)
    cumulants[3] -= 3.0*cumulants[1]*cumulants[1]
    return cumulants    

# The following function works only for small asymmetries
def distortedNumericCumulants(distro, quadPoints):
    assert distro.classname() == "DistortedGaussian"
    mu = distro.location()
    splus = distro.sigmaPlus()
    sminus = distro.sigmaMinus()
    assert (splus > 0.0 and sminus > 0.0)
    sigma = max(splus, sminus)
    return gaussianRatioCumulants(distro, quadPoints, mu, sigma)

def leadingPdfCumulants(e, classObj):
    assert e.errorType() == ase.P
    distro = classObj.fromQuantiles(e.location(), e.sigmaPlus(), e.sigmaMinus())
    return distributionCumulants(distro, 3)

def leadingOPATCumulants(e, classObj):
    assert e.errorType() == ase.P
    assert classObj.isFullOPAT
    distro = classObj(e.location(), e.sigmaPlus(), e.sigmaMinus())
    return distributionCumulants(distro, 3)

def leadingModelCumulants(e, classObj, requireOPAT):
    if requireOPAT or classObj.isFullOPAT:
        return leadingOPATCumulants(e, classObj)
    else:
        return leadingPdfCumulants(e, classObj)

class DescentDeltaRatio:
    def __init__(self, distroClass, deltaLnL=0.5):
        self.distroClass = distroClass
        self.deltaLnL = deltaLnL
    #
    def __call__(self, skew):
        cums = (0.0, 1.0, skew)
        d = self.distroClass(cums)
        deltaPlus = d.descentDelta(True, self.deltaLnL)
        deltaMinus = d.descentDelta(False, self.deltaLnL)
        return deltaPlus/deltaMinus

class QuantileSigmaRatio:
    def __init__(self, distroClass):
        self.distroClass = distroClass
    #
    def __call__(self, skew):
        cums = (0.0, 1.0, skew)
        d = self.distroClass(cums)
        median = d.quantile(0.5)
        qplus = d.quantile(ase.GCDF84)
        qminus = d.quantile(ase.GCDF16)
        assert qminus < median
        return (qplus - median)/(median - qminus)

class MinusFcn:
    def __init__(self, fcn):
        self.fcn = fcn
    def __call__(self, x):
        return -1.0*self.fcn(x)

def densityBasedLogliCurve(distroClass, mu, rightSigma, leftSigma, deltaLnL=0.5):
    if not hasattr(distroClass, 'fromModeAndDeltas'):
        message = ("Can not build log likelihood curve from the {} distribution as "
                   "it does not support construcion from mode and descent deltas.")
        raise RuntimeError(message.format(distroClass.__name__))
    # Note that the sigmas are swapped in the next call
    distro = distroClass.fromModeAndDeltas(0.0, leftSigma, rightSigma, deltaLnL)
    return ase.DistributionLogli(distro, mu)

class DensityBasedLogli:
    def __init__(self, distroClass, deltaLnL=0.5):
        self.distroClass = distroClass
        self.deltaLnL = deltaLnL
    #
    def __call__(self, mu, rightSigma, leftSigma):
        return densityBasedLogliCurve(
            self.distroClass, mu, rightSigma, leftSigma, self.deltaLnL)

# Q-Q plot of some distribution w.r.t. standard normal
def qqmapFromStandardNormal(distro, points):
    g = ase.Gaussian(0.0, 1.0)
    return [distro.quantile(g.cdf(x)) for x in points]

# Example code for adding two random variables using cumulants
def addTwoVarsUsingCumulants(distro1, distro2, classOut):
    cum1 = distributionCumulants(distro1, 3)
    cum2 = distributionCumulants(distro2, 3)
    return classOut(cum1 + cum2)

# Example code for combining two pdf results
def combineTwoPdfResults(r1, class1, r2, class2, classOut, verbose=0):
    m1, v1, s1 = leadingPdfCumulants(r1, class1)
    if verbose > 1:
        print("r1 cumulants are:", m1, v1, s1)
    assert v1 > 0.0
    inv1 = 1.0/v1
    m2, v2, s2 = leadingPdfCumulants(r2, class2)
    if verbose > 1:
        print("r2 cumulants are:", m2, v2, s2)
    assert v2 > 0.0
    inv2 = 1.0/v2
    wsum = inv1 + inv2
    w1 = inv1/wsum
    w2 = inv2/wsum
    mout = w1*m1 + w2*m2
    vout = w1*w1*v1 + w2*w2*v2
    sout = w1*w1*w1*s1 + w2*w2*w2*s2
    if verbose > 0:
        print("Combined cumulants are:", mout, vout, sout)
    distro = classOut([mout, vout, sout])
    med = distro.quantile(0.5)
    sPlus = distro.quantile(ase.GCDF84) - med
    sMinus = med - distro.quantile(ase.GCDF16)
    return ase.AsymmetricEstimate(med, sPlus, sMinus, ase.P)

# Code for combining two pdf results using the same model for everything
def combineTwoPdfResultsOneModel(r1, r2, classObj, verbose=0):
    return combineTwoPdfResults(r1, classObj, r2, classObj, classObj, verbose)

# Example code for combining multiple pdf results
def combineMultiplePdfResults(results, classes, classOut):
    nResults = len(results)
    assert nResults > 0
    assert len(classes) == nResults
    if nResults == 1:
        return results[0]
    #
    means = np.empty(nResults, dtype=np.double)
    variances = np.empty(nResults, dtype=np.double)
    skewnesses = np.empty(nResults, dtype=np.double)
    weights = np.empty(nResults, dtype=np.double)
    #
    for cnt, (r, cl) in enumerate(zip(results, classes)):
        mu, v, s = leadingPdfCumulants(r, cl)
        assert v > 0.0
        means[cnt] = mu
        variances[cnt] = v
        skewnesses[cnt] = s
        weights[cnt] = 1.0/v
    #
    wsum = np.sum(weights)
    weights /= wsum
    mout = np.dot(weights, means)
    w2 = weights*weights
    vout = np.dot(w2, variances)
    w3 = weights*w2
    sout = np.dot(w3, skewnesses)
    distro = classOut([mout, vout, sout])
    med = distro.quantile(0.5)
    sPlus = distro.quantile(ase.GCDF84) - med
    sMinus = med - distro.quantile(ase.GCDF16)
    return ase.AsymmetricEstimate(med, sPlus, sMinus, ase.P)

# Code for combining multiple pdf results using the same model for everything
def combineMultiplePdfResultsOneModel(results, classObj):
    nResults = len(results)
    assert nResults > 0
    return combineMultiplePdfResults(results, [classObj]*nResults, classObj)

# Example code for combining two pdf errors
def combineTwoPdfErrors(r1, class1, r2, class2, classOut, requireOPAT=False):
    m1, v1, s1 = leadingModelCumulants(r1, class1, requireOPAT)
    # print("r1 cumulants are:", m1, v1, s1)
    assert v1 > 0.0
    inv1 = 1.0/v1
    m2, v2, s2 = leadingModelCumulants(r2, class2, requireOPAT)
    # print("r2 cumulants are:", m2, v2, s2)
    assert v2 > 0.0
    mout = m1 + m2
    vout = v1 + v2
    sout = s1 + s2
    # print("Combined cumulants are:", mout, vout, sout)
    distro = classOut([mout, vout, sout])
    med = distro.quantile(0.5)
    sPlus = distro.quantile(ase.GCDF84) - med
    sMinus = med - distro.quantile(ase.GCDF16)
    return ase.AsymmetricEstimate(med, sPlus, sMinus, ase.P)

# Code for combining two pdf errors using the same model for everything
def combineTwoPdfErrorsOneModel(r1, r2, classObj, requireOPAT=False):
    return combineTwoPdfErrors(r1, classObj, r2, classObj, classObj, requireOPAT)

# Example code for combining multiple pdf errors
def combineMultiplePdfErrors(results, classes, classOut, requireOPAT=False):
    nResults = len(results)
    assert nResults > 0
    assert len(classes) == nResults
    if nResults == 1:
        return results[0]
    #
    means = np.empty(nResults, dtype=np.double)
    variances = np.empty(nResults, dtype=np.double)
    skewnesses = np.empty(nResults, dtype=np.double)
    #
    for cnt, (r, cl) in enumerate(zip(results, classes)):
        mu, v, s = leadingModelCumulants(r, cl, requireOPAT)
        assert v > 0.0
        means[cnt] = mu
        variances[cnt] = v
        skewnesses[cnt] = s
    #
    mout = np.sum(means)
    vout = np.sum(variances)
    sout = np.sum(skewnesses)
    distro = classOut([mout, vout, sout])
    med = distro.quantile(0.5)
    sPlus = distro.quantile(ase.GCDF84) - med
    sMinus = med - distro.quantile(ase.GCDF16)
    return ase.AsymmetricEstimate(med, sPlus, sMinus, ase.P)

# Code for combining multiple pdf errors using the same model for everything
def combineMultiplePdfErrorsOneModel(results, classObj, requireOPAT=False):
    nResults = len(results)
    assert nResults > 0
    return combineMultiplePdfErrors(results, [classObj]*nResults, classObj, requireOPAT)

def logliResult(curve):
    return ase.AsymmetricEstimate(curve.argmax(), curve.sigmaPlus(),
                                  curve.sigmaMinus(), ase.L)

def logliCurve(result, classObj):
    assert result.errorType() == ase.L
    return classObj(result.location(), result.sigmaPlus(), result.sigmaMinus())

# Combine two likelihood results
def combineTwoLogliResults(r1, class1, r2, class2):
    c1 = logliCurve(r1, class1)
    c2 = logliCurve(r2, class2)
    return logliResult(c1 + c2)

# Combine two likelihood results using the same model for both
def combineTwoLogliResultsOneModel(r1, r2, classObj):
    return combineTwoLogliResults(r1, classObj, r2, classObj)

# Combine multiple likelihood results
def combineMultipleLogliResults(results, classes):
    nResults = len(results)
    assert nResults > 0
    assert len(classes) == nResults
    if nResults == 1:
        return results[0]
    acc = ase.LikelihoodAccumulator()
    for r, cl in zip(results, classes):
        acc.accumulate(logliCurve(r, cl))
    return logliResult(acc)

# Combine multiple likelihood results using the same model for everything
def combineMultipleLogliResultsOneModel(results, classObj):
    nResults = len(results)
    assert nResults > 0
    return combineMultipleLogliResults(results, [classObj]*nResults)

def symmetrizeLogliResult(r):
    c = logliCurve(r, ase.SymmetrizedParabola)
    return logliResult(c)

# List all distribution models that can be used to construct log-likelihood
# curves using the "densityBasedLogliCurve" function in this module.
# You would typically want to exclude "FechnerDistribution" class from
# this list as the resulting log-likelihood is a duplicate of the standard
# "BrokenParabola" log-likelihood model.
def distrosUsableInLikelihoods(skipFechner = True):
    distros = []
    for name, cl in inspect.getmembers(ase, inspect.isclass):
        if issubclass(cl, ase.AbsDistributionModel1D):
            if hasattr(cl, 'fromModeAndDeltas'):
                if name == "FechnerDistribution" and skipFechner:
                    continue
                if name == "SymmetricBetaGaussian":
                    continue
                distros.append(cl)
    return distros

# List all log-likelihood models that have a standard constructor:
# model(location, sigmaPlus, sigmaMinus). Note that this does not include
# existing models with non-standard constructors (ConservativeSpline,
# DistributionLogli, etc) or models that remain abstract.
def allStandardLogliModels():
    models = []
    for name, cl in inspect.getmembers(ase, inspect.isclass):
        if issubclass(cl, ase.AbsLogLikelihoodCurve):
            try:
                curve = cl(0.0, 1.0, 1.1)
            except:
                pass
            else:
                models.append(cl)
    return models

# "Full OPAT" pdfs have 3-argument constructors (from location,
#  sigmaPlus, and sigmaMinus) for which sigmas can be negative
def fullOPATPdfs():
    opats = []
    for name, cl in inspect.getmembers(ase, inspect.isclass):
        if issubclass(cl, ase.AbsDistributionModel1D):
            try:
                if cl.isFullOPAT:
                    pdf = cl(0.0, 1.0, 1.1)
                    opats.append(cl)
            except:
                pass
    return opats

# Pdfs that can be constructed from quantiles using the
# 3-parameter method "fromQuantiles"
def fromQuantilesPdfs():
    classes = []
    for name, cl in inspect.getmembers(ase, inspect.isclass):
        if issubclass(cl, ase.AbsDistributionModel1D):
            try:
                pdf = cl.fromQuantiles(0.0, 1.0, 1.1)
            except:
                pass
            else:
                classes.append(cl)
    return classes

def findRootUsingBisections(fcn, rhs, x0, x1, tol):
    if tol <= np.finfo(float).eps:
        raise ValueError("Tolerance argument is too small")
    f0 = fcn(x0)
    if f0 == rhs:
        return x0
    f1 = fcn(x1)
    if f1 == rhs:
        return x1
    increasing = f0 < rhs and rhs < f1
    decreasing = f0 > rhs and rhs > f1
    if not (increasing or decreasing):
        raise ValueError("The root is not bounded by input arguments")
    sqrtol = math.sqrt(tol)
    maxiter = 2000
    for it in range(maxiter):
        xmid = (x0 + x1)/2.0
        fmid = fcn(xmid)
        if fmid == rhs:
            return xmid
        if abs(x0 - x1)/(abs(xmid) + sqrtol) <= tol:
            return xmid
        if increasing:
            if fmid > rhs:
                x1 = xmid
            else:
                x0 = xmid
        else:
            if fmid > rhs:
                x0 = xmid
            else:
                x1 = xmid
    raise RuntimeError("Iterations failed to converge")

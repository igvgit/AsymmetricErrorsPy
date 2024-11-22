import math
import numpy as np

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

class ProfileLogliOfASum:
    def __init__(self, curves, damping=1.0, eps=None, maxiter=None):
        nCurves = len(curves)
        assert nCurves > 0
        self.curves = curves
        self._argmaxs = np.array([curve.argmax() for curve in curves], dtype=np.double)
        self._argsum = np.sum(self._argmaxs)
        self._maximum = sum([curve(a) for a, curve in zip(self._argmaxs, curves)])
        self.damping = damping*1.0
        assert self.damping > 0.0
        assert self.damping <= 1.0
        if eps is None:
            self.eps = 64.0*math.sqrt(nCurves)*np.finfo(float).eps
        else:
            self.eps = eps*1.0
        assert self.eps > 0.0
        self.sqreps = math.sqrt(self.eps)
        if maxiter is None:
            self.maxiter = 2000
        else:
            self.maxiter = int(maxiter)
        assert self.maxiter > 0
        # Memoized values
        self._lastSum = self._argsum
        self._lastArgs = self._argmaxs
        self._lastLogli = self._maximum

    def _nextApprox(self, sumValue, a0):
        nCurves = len(self.curves)
        assert a0.size == nCurves
        sz = nCurves + 1
        mat = np.zeros((sz, sz), dtype=np.double)
        mat[:,nCurves] = 1.0
        mat[nCurves,:] = 1.0
        rhs = np.empty(sz, dtype=np.double)
        for i, curve in enumerate(self.curves):
            mat[i][i] = curve.secondDerivative(a0[i])
            rhs[i] = -curve.derivative(a0[i])
        mat[nCurves,nCurves] = 0.0
        rhs[nCurves] = sumValue - np.sum(a0)
        deltas = np.linalg.solve(mat, rhs)
        return a0 + self.damping*deltas[:nCurves]

    def _flt_equal(self, f1, f2):
        return abs(f1 - f2)/(abs((f1 + f2)/2.0) + self.sqreps) < self.eps

    def _converged(self, sumValue, a):
        if not self._flt_equal(sumValue, np.sum(a)):
            return False
        derivs = [curve.derivative(ai) for ai, curve in zip(a, self.curves)]
        derivs.sort()
        return self._flt_equal(derivs[0], derivs[-1])

    # "startWithLast" should be set to "True" for likelihood scans
    def __call__(self, sumValue, startWithLast=False):
        if sumValue == self._lastSum:
            return self._lastLogli - self._maximum

        if len(self.curves) == 1:
            # Update memoized values before returning.
            # Update _lastLogli first, as this call can
            # potentially raise an exception.
            self._lastLogli = self.curves[0](sumValue)
            self._lastSum = sumValue
            self._lastArgs = [sumValue,]
            return self._lastLogli - self._maximum

        if startWithLast:
            a0 = self._lastArgs
        else:
            a0 = self._argmaxs

        # Linearize the constrained maximum equation and
        # solve it by iteration
        for it in range(self.maxiter):
            a0 = self._nextApprox(sumValue, a0)
            if self._converged(sumValue, a0):
                self._lastLogli = sum([curve(ai) for ai, curve in zip(a0, self.curves)])
                self._lastSum = sumValue
                self._lastArgs = a0
                return self._lastLogli - self._maximum

        self._iter_failure("operator()")

    def _iter_failure(self, where):
        raise RuntimeError("Iterations failed to converge in "
                           "{}. Damping = {}, eps = {}, maxiter = {}.".format(
                               where, self.damping, self.eps, self.maxiter))

    def _directedSigma(self, deltaLogLikelihood, direction):
        assert deltaLogLikelihood > 0.0
        nCurves = len(self.curves)
        del1 = deltaLogLikelihood*1.0/nCurves
        if direction > 0:
            sigmas = [c.sigmaPlus(del1) for c in self.curves]
        else:
            sigmas = [c.sigmaMinus(del1) for c in self.curves]
        s0 = min(sigmas)
        assert s0 > 0.0
        a0 = self._argsum + direction*s0
        nll0 = -self(a0)
        assert nll0 <= deltaLogLikelihood
        if nll0 == deltaLogLikelihood:
            return s0
        step = s0
        factor = 1.1
        converged = False
        for it in range(self.maxiter):
            atry = a0 + direction*step
            nlltry = -self(atry, True)
            if abs(nlltry - deltaLogLikelihood) < self.eps:
                return direction*(atry - self._argsum)
            if nlltry > deltaLogLikelihood:
                converged = True
                break
            else:
                a0 = atry
                nll0 = nlltry
                step = step*factor
        if not converged:
            self._iter_failure("_directedSigma")
        fcn = _ProfileSumLogliProxy(self)
        a = findRootUsingBisections(fcn, deltaLogLikelihood, a0, atry, self.eps)
        return direction*(a - self._argsum)

    def argmax(self):
        return self._argsum

    def maximum(self):
        return self._maximum

    def sigmaPlus(self, deltaLogLikelihood=0.5):
        if len(self.curves) == 1:
            return self.curves[0].sigmaPlus(deltaLogLikelihood)
        else:
            return self._directedSigma(deltaLogLikelihood, 1)

    def sigmaMinus(self, deltaLogLikelihood=0.5):
        if len(self.curves) == 1:
            return self.curves[0].sigmaMinus(deltaLogLikelihood)
        else:
            return self._directedSigma(deltaLogLikelihood, -1)

class _ProfileSumLogliProxy:
    def __init__(self, profileLogli):
        self.profileLogli = profileLogli

    def __call__(self, sumValue):
        return -self.profileLogli(sumValue, True)

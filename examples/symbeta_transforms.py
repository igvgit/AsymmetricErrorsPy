#!/usr/bin/env python3
"""
The code below illustrates the transformations used to construct
symmetric beta Gaussian distributions
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.1"
__date__ ="May 30 2024"

import asepy as ase
import matplotlib.pyplot as plt

# Positive and negative errors for all cases
sp = 1.0
sm = 0.6

# Plotting parameters
xmin = -3.0
xmax = 3.0
nscan = 601

# Create the figure layout
fig, axs = plt.subplots(3, 2, sharex='col')
axs[2, 0].set_xlabel(r'$\nu$')
axs[2, 1].set_xlabel(r'$\nu$')
axs[0, 0].set_ylabel('R')
axs[1, 0].set_ylabel('R')
axs[2, 0].set_ylabel('R')
fig.suptitle('Symmetric Beta Transforms')
fig.set_size_inches((5, 7))

# Procedure used to make the plots on each pane
def plot_curve(row, col, p, h, legendOnly=False):
    curve = ase.SymbetaDoubleIntegral.fromSigmas(p, h, sp, sm)
    deriv = ase.DerivativeFunctor(curve)
    secondDeriv = ase.SecondDerivativeFunctor(curve)
    x, y = ase.scanFunctor1D(curve, xmin, xmax, nscan)
    yder = ase.scanFunctor1D(deriv, x)
    der2 = ase.scanFunctor1D(secondDeriv, x)
    if legendOnly:
        up = 1000.0
        axs[row, col].plot(x, y+up, 'r', label='Transform')
        axs[row, col].plot(x, yder+up, 'b', label='Derivative')
        axs[row, col].plot(x, der2+up, 'k', label='Second Derivative')
        axs[row, col].legend(loc='center')
        axs[row, col].tick_params(colors='white')
        for name in ('left', 'right', 'bottom', 'top'):
            axs[row, col].spines[name].set_color('white')
    else:
        axs[row, col].plot(x, y, 'r', label='Transform')
        axs[row, col].plot(x, yder, 'b', label='Derivative')
        axs[row, col].plot(x, der2, 'k', label='Second Derivative')
        axs[row, col].text(-2.5, 2.5, "$p$ = {}, $h$ = {}".format(p, h), fontsize='large')
    axs[row, col].set_ylim(-2.0, 3.5)

# Create the plots
plot_curve(0, 0, 2, 0.5)
plot_curve(1, 0, 2, 1.0)
plot_curve(2, 0, 2, 2.0)
plot_curve(2, 1, 1, 1.0)
plot_curve(1, 1, 3, 1.0)
plot_curve(0, 1, 3, 1.0, True)

fig.tight_layout()
plt.show()

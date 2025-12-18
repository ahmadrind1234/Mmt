""" Beam Deflection Calculator (Euler–Bernoulli Beam Theory) Author: You Description: This script computes shear force, bending moment, slope, and deflection for a simply supported beam under common loading cases.

Units (consistent):

Length: meters (m)

Force: Newton (N)

Young's Modulus: Pascals (Pa)

Second moment of area: m^4


This code is suitable for a GitHub repository and can be extended for UI or web applications. """

import numpy as np import matplotlib.pyplot as plt

-----------------------------

Beam Parameters

-----------------------------

L = 5.0              # Beam length (m) E = 200e9            # Young's modulus (Pa) (Steel) I = 8.33e-6          # Second moment of area (m^4) w = 2000             # Uniformly distributed load (N/m)

Discretization

n = 500 x = np.linspace(0, L, n)

-----------------------------

Reactions (Simply Supported Beam with UDL)

-----------------------------

RA = w * L / 2 RB = w * L / 2

-----------------------------

Shear Force and Bending Moment

-----------------------------

V = RA - w * x M = RA * x - (w * x**2) / 2

-----------------------------

Deflection Calculation

Using Double Integration Method

-----------------------------

EI * d^2y/dx^2 = M(x)

d2y_dx2 = M / (E * I)

dy_dx = np.cumsum(d2y_dx2) * (x[1] - x[0]) y = np.cumsum(dy_dx) * (x[1] - x[0])

Apply boundary conditions: y(0)=0 and y(L)=0

Correct integration constants

C1 = -y[-1] / L

y_corrected = y + C1 * x

-----------------------------

Maximum Deflection (Theoretical)

-----------------------------

max_deflection_theory = (5 * w * L**4) / (384 * E * I)

-----------------------------

Results

-----------------------------

print("Maximum numerical deflection (m):", np.min(y_corrected)) print("Maximum theoretical deflection (m):", -max_deflection_theory)

-----------------------------

Plotting

-----------------------------

plt.figure() plt.plot(x, y_corrected) plt.xlabel("Length (m)") plt.ylabel("Deflection (m)") plt.title("Beam Deflection (Simply Supported Beam with UDL)") plt.grid(True) plt.show()

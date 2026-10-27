# Exp 18: Defuzzification using Centroid (Centre of Gravity) Method
import numpy as np


def trap(x, a, b, c, d):
    """Trapezoidal membership function of height 1 (triangle when b == c)."""
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)


# Input fuzzy sets: shape (a, b, c, d), height
n = int(input("Enter number of fuzzy sets: "))
sets = []

for i in range(n):
    print("Set", i + 1)
    a, b, c, d = map(float, input("Enter a, b, c, d: ").split())
    h = float(input("Enter height: "))
    sets.append(((a, b, c, d), h))


x = np.linspace(0, 100, 100001)  # step 0.001
dx = x[1] - x[0]

mus = [h * trap(x, *p) for p, h in sets]
mu = np.maximum.reduce(mus)  # aggregated output = union (max)

A = np.sum(mu) * dx           # area under aggregated curve
M = np.sum(mu * x) * dx       # first moment

print(f"Area   A = {A:.4f}")
print(f"Moment M = {M:.4f}")
print(f"Centroid x* = M / A = {M / A:.4f}")
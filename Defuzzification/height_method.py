# Exp 20: Defuzzification using Height (Max-Membership) Method
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

hmax = mu.max()
peak = x[np.isclose(mu, hmax, atol=1e-9)]

print(f"Maximum membership (height) = {hmax:.4f}")
print(f"First of maxima             = {peak.min():.4f}")
print(f"Last of maxima              = {peak.max():.4f}")
print(f"Mean of maxima              = {peak.mean():.4f}")
print(f"Height method x* = {peak.mean():.4f}")
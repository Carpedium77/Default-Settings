# Exp 19: Defuzzification using Centre of Sums Method
import numpy as np

def trap(x, a, b, c, d):
    """Trapezoidal membership function of height 1 (triangle when b == c)."""
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)


# Input fuzzy sets: shape (a, b, c, d), height
n = int(input("Enter number of fuzzy sets: "))
sets = []

for i in range(n):
    print("Set C", i + 1)
    a, b, c, d = map(float, input("Enter a, b, c, d: ").split())
    h = float(input("Enter height: "))
    sets.append(((a, b, c, d), h))


x = np.linspace(0, 100, 100001)  # step 0.001
dx = x[1] - x[0]
mus = [h * trap(x, *p) for p, h in sets]


# Each set's own area and centroid; overlaps counted twice (sum, not max)
num = den = 0

for k, m in enumerate(mus, 1):
    Ak = np.sum(m) * dx
    xk = np.sum(m * x) * dx / Ak

    print(f"C{k}: area = {Ak:.4f}, centroid = {xk:.4f}")

    num += Ak * xk
    den += Ak

print(f"\nCentre of sums x* = {num:.4f} / {den:.4f} = {num / den:.4f}")
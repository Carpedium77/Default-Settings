# Exp 16: Composition of Fuzzy Relations

import numpy as np

m = int(input("Enter number of rows in R: "))
n = int(input("Enter number of columns in R: "))
p = int(input("Enter number of columns in S: "))

R = []
S = []

print("Enter elements of R row-wise:")
for i in range(m):
    row = list(map(float, input().split()))
    R.append(row)

print("Enter elements of S row-wise:")
for i in range(n):
    row = list(map(float, input().split()))
    S.append(row)

R = np.array(R)
S = np.array(S)


def max_min(R, S):
    T = np.zeros((R.shape[0], S.shape[1]))

    for i in range(R.shape[0]):
        for k in range(S.shape[1]):
            T[i, k] = max(
                min(R[i, j], S[j, k])
                for j in range(R.shape[1])
            )

    return T


def max_product(R, S):
    T = np.zeros((R.shape[0], S.shape[1]))

    for i in range(R.shape[0]):
        for k in range(S.shape[1]):
            T[i, k] = max(
                R[i, j] * S[j, k]
                for j in range(R.shape[1])
            )

    return T


print("Relation R (X x Y):\n", R)
print("Relation S (Y x Z):\n", S)

print("\nMax-Min composition T = R o S:\n", max_min(R, S))
print("\nMax-Product composition T = R . S:\n",
      np.round(max_product(R, S), 2))
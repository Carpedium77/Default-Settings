# Exp 15: Fuzzy Set Operations

n = int(input("Enter number of elements: "))

A = {}
B = {}

for i in range(n):
    x = input(f"Enter element {i + 1}: ")
    A[x] = float(input(f"Enter membership value of {x} in A: "))
    B[x] = float(input(f"Enter membership value of {x} in B: "))


ops = {
    "Union (A U B) = max":                  lambda a, b: max(a, b),
    "Intersection (A n B) = min":           lambda a, b: min(a, b),
    "Complement of A = 1 - a":              lambda a, b: 1 - a,
    "Difference A|B = min(a, 1 - b)":       lambda a, b: min(a, 1 - b),
    "Algebraic sum = a + b - ab":           lambda a, b: a + b - a * b,
    "Algebraic product = ab":               lambda a, b: a * b,
    "Bounded sum = min(1, a + b)":          lambda a, b: min(1.0, a + b),
    "Bounded difference = max(0, a - b)":   lambda a, b: max(0.0, a - b),
}


print("A =", A)
print("B =", B, "\n")

for name, op in ops.items():
    result = {x: round(op(A[x], B[x]), 2) for x in A}
    print(f"{name:36s}: {result}")


# De Morgan's law check: (A U B)' = A' n B'
lhs = {x: round(1 - max(A[x], B[x]), 2) for x in A}
rhs = {x: round(min(1 - A[x], 1 - B[x]), 2) for x in A}

print("\nDe Morgan (A U B)' = A' n B' holds:", lhs == rhs)
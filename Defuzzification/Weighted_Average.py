# Exp 17: Weighted Average Defuzzification

n = int(input("Enter number of fuzzy sets: "))

sets = {}

for i in range(n):
    name = input(f"Enter set name {i+1}: ")
    xc = float(input(f"Enter centre of {name}: "))
    h = float(input(f"Enter height of {name}: "))
    sets[name] = (xc, h)

num = sum(xc * h for xc, h in sets.values())
den = sum(h for xc, h in sets.values())

for name, (xc, h) in sets.items():
    print(f"{name}: centre = {xc}, height = {h}, product = {xc * h:.2f}")

print(f"\nSum(h * x) = {num:.2f}, Sum(h) = {den:.2f}")

if den != 0:
    print(f"Weighted average x* = {num / den:.4f}")
else:
    print("Weighted average cannot be calculated because total height is zero.")
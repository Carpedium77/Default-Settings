
m = int(input("Enter number of data bits: "))
data = list(map(int, input("Enter data bits: ")))

r = 0
while 2 ** r < m + r + 1:
    r += 1

n = m + r
code = [0] * (n + 2)

# Place data bits
j = 0
for i in range(1, n + 1):
    if i & (i - 1):
        code[i] = data[j]
        j += 1

# Calculate Hamming parity bits
for i in range(r):
    p = 2 ** i
    for j in range(1, n + 1):
        if j & p:
            code[p] ^= code[j]

# Calculate overall parity bit
for i in range(1, n + 1):
    code[n + 1] ^= code[i]

print("Generated Hamming code:", "".join(map(str, code[1:])))

# Introduce errors
pos = int(input(f"Enter first error position (0 for no error, 1-{n+1}): "))
pos2 = int(input("Enter second error position (0 for none): "))

if pos < 0 or pos > n + 1 or pos2 < 0 or pos2 > n + 1 or (pos != 0 and pos == pos2):
    print("Invalid error position.")
else:
    if pos:
        code[pos] ^= 1
    if pos2:
        code[pos2] ^= 1

    print("Received code:", "".join(map(str, code[1:])))

    # Calculate syndrome
    syndrome = 0
    for i in range(r):
        p = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & p:
                parity ^= code[j]
        if parity:
            syndrome += p

    # Check overall parity
    overall = 0
    for i in range(1, n + 2):
        overall ^= code[i]

    if syndrome == 0 and overall == 0:
        print("No error detected.")
    elif syndrome != 0 and overall == 1:
        print("Single-bit error detected at position", syndrome)
        code[syndrome] ^= 1
        print("Corrected code:", "".join(map(str, code[1:])))
    elif syndrome == 0 and overall == 1:
        print("Error detected in overall parity bit at position", n + 1)
        code[n + 1] ^= 1
        print("Corrected code:", "".join(map(str, code[1:])))
    else:
        print("Double-bit error detected. Cannot correct.")

barker = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
data = input("Enter binary data (2, 3 or 4 digits): ")

while not (len(data) in [2, 3, 4] and set(data) <= {"0", "1"}):
    data = input("Invalid input. Enter binary data (2, 3 or 4 digits): ")

input_bits = [int(b) for b in data]
print("\n----- TRANSMITTER -----")
transmitted = []

for i, bit in enumerate(input_bits):
    chip = [b ^ bit for b in barker]
    transmitted.append(chip)
    print(f"Digit {i+1} = {bit} -> XOR with Barker -> Chip: {''.join(map(str, chip))}")

print("\n----- CHANNEL -----")
print("Transmitted chip stream sent to receiver (assumed no noise).")
print("\n----- RECEIVER -----")
received_bits = []

for i, chip in enumerate(transmitted):
    despread = [c ^ b for c, b in zip(chip, barker)]
    if all(x == 0 for x in despread):
        recovered_bit = 0
    elif all(x == 1 for x in despread):
        recovered_bit = 1
    else:
        recovered_bit = None
    received_bits.append(recovered_bit)
    print(
        f"Chip {i+1}: {''.join(map(str, chip))} "
        f"-> XOR with Barker -> Despread: {''.join(map(str, despread))} "
        f"-> Recovered bit: {recovered_bit}"
    )

print("\n----- SUMMATION -----")
print(f"Original Input : {''.join(map(str, input_bits))}")
print(f"Recovered Output: {''.join(str(b) for b in received_bits)}")

if input_bits == received_bits:
    print("Comment: Initial input matches output -> CORRECT")
else:
    print("Comment: Initial input does NOT match output -> ERROR")

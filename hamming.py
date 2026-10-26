import numpy as np

m = int(input("Enter the number of data bits :"))
data = list(map(int , input("Enter the data bits :")))
r=0

while 2 ** r < r + m + 1:
  r += 1

n = m + r
code = [0] * (n+2)
j=0
for i in range(1 , n+1):
  if i & (i-1):
    code[i] = data[j]
    j+=1

for i in range(r):
  p = 2 ** i
  for j in range(1, n+1):
    if j & p:
      code[p] ^= code[j]

for i in range(1 , n+1):
  code[n+1] ^= code[i]

print("Generated Hamming code : " , "".join(map(str,code[1:])))

pos = int(input("Introduce the first error pos :"))
pos2 =  int(input("Introduce the second error pos : "))

if pos < 0 or pos > n+1 or pos2 < 0 or pos2 > n+1 or (pos != 0 and pos == pos2):
  print("Invalid Error")

else :
  if pos:
    code[pos] ^= 1
  if pos2:
    code[pos2] ^= 1

  print("Recieved Hamming code :" , "".join(map(str,code[1:])))

  syndrome = 0
  for i in range(r):
    p = 2 ** i
    parity = 0
    for j in range(1,n+1):
      if j & p:
        parity ^= code[j]

      if parity :
        syndrome += p

  overall = 0
  for i in range (1,n+2):
    overall ^= code[i]

  if syndrome == 0 and overall == 0:
    print("No error introduced!")
  elif syndrome != 0 and overall == 1:
    print("Single bit error introduced" , syndrome)
    code[syndrome] ^= 1
    print("Corrected code :" , "".join(map(str,code[1:])))
  elif syndrome == 0 and overall == 1:
    print("Error detected in overall parity bit at position :",syndrome)
    code[syndrome] ^= 1
    print("Corrected code :" , "".join(map(str,code[1:])))
  else :
    print("Double bit error detected and can't correct!!!")

  

    
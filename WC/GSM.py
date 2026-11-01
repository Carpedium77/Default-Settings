
# Experiment 3: GSM Security Algorithms (A3, A5, A8)
import hashlib
import os

def A3(ki, rand):
    return hashlib.sha256(ki + rand + b"A3").digest()[:4]

def A8(ki, rand):
    return hashlib.sha256(ki + rand + b"A8").digest()[:8]

def A5(kc, frame, data):
    ks = hashlib.sha256(kc + frame.to_bytes(4, "big")).digest()
    return bytes(d ^ ks[i % len(ks)] for i, d in enumerate(data))

print("=" * 55)
print("   GSM SECURITY SIMULATION : A3 / A8 / A5")
print("=" * 55)

Ki = bytes.fromhex(input("Enter Ki (32 hex digits): "))
RAND = bytes.fromhex(input("Enter RAND (32 hex digits): "))

SRES_net = A3(Ki, RAND)
Kc_net = A8(Ki, RAND)
print("\n[Network] RAND sent to MS   :", RAND.hex())
print("[Network] Expected SRES     :", SRES_net.hex())
SRES_ms = A3(Ki, RAND)
Kc_ms = A8(Ki, RAND)
print("\n[Mobile] SRES computed (A3):", SRES_ms.hex())
print("[Mobile] Kc computed    (A8):", Kc_ms.hex())
print("\nAuthentication :", "SUCCESS (SRES match)" if SRES_ms == SRES_net else "FAILED")


msg = input("\nEnter message to encrypt: ").encode()
frame = int(input("Enter frame number: "))
ct = A5(Kc_ms, frame, msg)
pt = A5(Kc_net, frame, ct)
print("\nPlaintext      :", msg.decode())
print("Frame number   :", frame)
print("Ciphertext (A5):", ct.hex())
print("Decrypted      :", pt.decode())

# 5. Impostor tries using a wrong secret key
fake = A3(os.urandom(16), RAND)
print("\nImpostor SRES :", fake.hex(),"->", "SUCCESS" if fake == SRES_net else "FAILED (rejected)")
print("=" * 55)

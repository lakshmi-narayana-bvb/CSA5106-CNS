
def gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = gcd(b, a % b)
    return g, y, x - (a // b) * y

# Given public key
e = 31
n = 3599

# Find p and q
for p in range(2, n):
    if n % p == 0:
        q = n // p
        break

# Calculate phi
phi = (p - 1) * (q - 1)

# Find private key
g, x, y = gcd(e, phi)
d = x % phi

# Encryption and decryption
m = 65
c = pow(m, e, n)
plain = pow(c, d, n)

print("p =", p)
print("q =", q)
print("Phi =", phi)
print("Public Key =", (e, n))
print("Private Key =", (d, n))
print("Plaintext =", m)
print("Ciphertext =", c)
print("Decrypted Text =", plain)


import math

# RSA public key
n = 3599
e = 31

# Given blocks
blocks = [65, 118, 177, 236]

for block in blocks:
    factor = math.gcd(block, n)

    if 1 < factor < n:
        p = factor
        q = n // p

        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)

        print("Common Factor:", factor)
        print("p =", p)
        print("q =", q)
        print("Private Key:", (d, n))
        break
else:
    print("No useful common factor found")

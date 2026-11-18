import numpy as np

MOD = 26

def mod_inverse(a, m=MOD):
    """Find the modular multiplicative inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_block(K, P_vec):
    """Encrypt a column vector P_vec using key matrix K modulo 26."""
    return np.dot(K, P_vec) % MOD

def known_plaintext_attack(P, C):
    """
    Recover key matrix K using K = C * P^(-1) mod 26.
    Columns of P and C represent plaintext and ciphertext vectors.
    """
    # 1. Calculate determinant of 2x2 matrix P
    det = int(round(np.linalg.det(P))) % MOD
    
    # 2. Find modular inverse of determinant
    inv_det = mod_inverse(det, MOD)
    if inv_det is None:
        return None  # Matrix P is not invertible mod 26

    # 3. Compute adjugate matrix of P and multiply by inv_det mod 26
    adj_P = np.array([
        [P[1, 1], -P[0, 1]],
        [-P[1, 0], P[0, 0]]
    ])
    P_inv = (inv_det * adj_P) % MOD

    # 4. Recover K = C * P_inv mod 26
    recovered_K = np.dot(C, P_inv) % MOD
    return recovered_K

def chosen_plaintext_attack(secret_K):
    """
    Recover key matrix K by querying the encryption oracle with 
    the identity matrix vectors ("BA" -> [1, 0]^T and "AB" -> [0, 1]^T).
    """
    n = secret_K.shape[0]
    identity_P = np.eye(n, dtype=int)
    recovered_K = np.zeros((n, n), dtype=int)

    for col in range(n):
        P_vec = identity_P[:, col]
        # The ciphertext vector directly reveals the column of K
        recovered_K[:, col] = encrypt_block(secret_K, P_vec)

    return recovered_K

def main():
    # Original Secret Key Matrix (Invertible mod 26, det = 3*5 - 3*2 = 9)
    secret_K = np.array([,
        [2, 5]
    ])

    print("Original Secret Key Matrix K:")
    print(secret_K, "\n")

    # --- 1. KNOWN-PLAINTEXT ATTACK (KPA) ---
    print("=== 1. Known-Plaintext Attack (KPA) ===")
    # Intercepted plaintext "HELP" -> [7, 4]^T ("HE") and [11, 15]^T ("LP")
    P = np.array([,
        [4, 15]
    ])
    
    # Generate corresponding ciphertext matrix C
    C = np.dot(secret_K, P) % MOD

    kpa_key = known_plaintext_attack(P, C)
    if kpa_key is not None:
        print("Recovered Key Matrix via KPA:")
        print(kpa_key, "\n")
    else:
        print("KPA Failed: Plaintext matrix is not invertible mod 26.\n")

    # --- 2. CHOSEN-PLAINTEXT ATTACK (CPA) ---
    print("=== 2. Chosen-Plaintext Attack (CPA) ===")
    cpa_key = chosen_plaintext_attack(secret_K)
    print("Recovered Key Matrix via CPA (No matrix inversion needed):")
    print(cpa_key)

if __name__ == "__main__":
    main()

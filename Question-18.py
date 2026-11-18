# Permuted Choice 1 (PC-1): Extracts 56 bits from the 64-bit initial key
# First 28 entries form C0 (Subset A), last 28 entries form D0 (Subset B)
PC1 = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,  # End of first 28 bits (C0)
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4   # End of second 28 bits (D0)
]

# Permuted Choice 2 (PC-2): Compresses 56 bits (Ci || Di) into a 48-bit subkey
# Indices 1..28 reference Ci; Indices 29..56 reference Di
PC2 = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,  # First 24 bits: strictly from Ci (1..28)
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32   # Second 24 bits: strictly from Di (29..56)
]

# Number of left circular shifts per round
SHIFT_SCHEDULE = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]


def left_circular_shift_28(val: int, shifts: int) -> int:
    """Performs a left circular shift on a 28-bit integer."""
    val &= 0x0FFFFFFF
    return ((val << shifts) | (val >> (28 - shifts))) & 0x0FFFFFFF


def apply_pc1(initial_key: int) -> tuple[int, int]:
    """Applies PC-1 to extract two disjoint 28-bit subsets C0 and D0."""
    c0 = 0
    d0 = 0
    for i in range(28):
        bit = (initial_key >> (64 - PC1[i])) & 1
        c0 = (c0 << 1) | bit
    for i in range(28, 56):
        bit = (initial_key >> (64 - PC1[i])) & 1
        d0 = (d0 << 1) | bit
    return c0, d0


def apply_pc2(c: int, d: int) -> int:
    """Applies PC-2 to generate the 48-bit round subkey from Ci and Di."""
    combined = ((c & 0x0FFFFFFF) << 28) | (d & 0x0FFFFFFF)
    subkey = 0
    for pos in PC2:
        bit = (combined >> (56 - pos)) & 1
        subkey = (subkey << 1) | bit
    return subkey


def verify_disjoint_subsets() -> None:
    """Verifies the disjoint subset property programmatically."""
    subset_c_indices = set(PC1[:28])
    subset_d_indices = set(PC1[28:])

    is_disjoint = subset_c_indices.isdisjoint(subset_d_indices)
    first_half_valid = all(1 <= pos <= 28 for pos in PC2[:24])
    second_half_valid = all(29 <= pos <= 56 for pos in PC2[24:])

    print("--- Structural Verification ---")
    print(f"1. PC-1 splits initial key into two disjoint 28-bit subsets: {'VERIFIED' if is_disjoint else 'FAILED'}")
    print(f"2. First 24 bits of every subkey come strictly from Subset C (bits 1-28): {'VERIFIED' if first_half_valid else 'FAILED'}")
    print(f"3. Second 24 bits of every subkey come strictly from Subset D (bits 29-56): {'VERIFIED' if second_half_valid else 'FAILED'}\n")


def main() -> None:
    # Standard 64-bit DES test key (including 8 parity bits)
    initial_key = 0x133457799BBCDFF1
    print(f"Initial 64-bit Key: 0x{initial_key:016X}\n")

    # Step 1: Verify the mathematical property of PC-1 and PC-2
    verify_disjoint_subsets()

    # Step 2: Partition initial key into disjoint 28-bit registers C0 and D0
    c, d = apply_pc1(initial_key)
    print(f"Initial 28-bit Subset C0: 0x{c:07X}")
    print(f"Initial 28-bit Subset D0: 0x{d:07X}\n")

    # Step 3: Generate and display all 16 round subkeys
    print("Round | Subkey (48-bit)  | First 24 bits (from C) | Second 24 bits (from D)")
    print("------+------------------+------------------------+------------------------")

    for round_num, shifts in enumerate(SHIFT_SCHEDULE, start=1):
        c = left_circular_shift_28(c, shifts)
        d = left_circular_shift_28(d, shifts)

        subkey = apply_pc2(c, d)
        first_24 = (subkey >> 24) & 0xFFFFFF
        second_24 = subkey & 0xFFFFFF

        print(f"  {round_num:2d}  |  0x{subkey:012X}  |        0x{first_24:06X}        |        0x{second_24:06X}")


if __name__ == "__main__":
    main()

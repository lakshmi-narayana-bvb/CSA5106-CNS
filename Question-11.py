import math


def calculate_playfair_keys():
    grid_size = 25

    # Calculate exact 25! (Python handles big integers natively)
    total_keys = math.factorial(grid_size)

    # Calculate exact exponent of 2 using base-2 logarithm
    log2_keys = math.log2(total_keys)

    # Round to the nearest whole power of 2
    approx_power = round(log2_keys)

    print(f"Total possible Playfair keys (25!): {total_keys}")
    print(f"Scientific notation: {total_keys:.4e}")
    print(f"Exact power of 2: 2^{log2_keys:.2f}")
    print(f"Approximate power of 2: 2^{approx_power}")


if __name__ == "__main__":
    calculate_playfair_keys()

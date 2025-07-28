def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
a = 252
b = 105
print(f"GCD of {a} and {b} is:", gcd_euclidean(a, b))

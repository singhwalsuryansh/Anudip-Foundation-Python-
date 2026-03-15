# ============================================================
# Problem 23: Reverse a Number Using While Loop
# ============================================================
# Approach: Repeatedly extract the last digit with % 10 and
#           build the reversed number by multiplying by 10.
#
# Example:
#   Input:  6789
#   Output: Reversed: 9876
# ============================================================

def reverse_number_while(n):
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n != 0:
        last_digit = n % 10         # extract last digit
        reversed_n = reversed_n * 10 + last_digit  # shift left and add
        n //= 10                    # remove last digit
    return -reversed_n if negative else reversed_n

# ---- Read input ----
n = int(input("Enter a number: "))

print(f"Original: {n}")
print(f"Reversed: {reverse_number_while(n)}")

# ============================================================
# Sample Output:
#   Enter a number: 6789
#   Original: 6789
#   Reversed: 9876
# ============================================================

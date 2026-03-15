# ============================================================
# Problem 16: Validate Username and Password
# ============================================================
# Rules:
#   Username: 5-15 chars, only letters and digits, starts with letter
#   Password: min 8 chars, must have uppercase, lowercase, and digit
#
# Example:
#   Username: John123  → Valid
#   Password: Secure99 → Valid
# ============================================================

def validate_username(username):
    if not (5 <= len(username) <= 15):
        return False, "Username must be 5-15 characters long."
    if not username[0].isalpha():
        return False, "Username must start with a letter."
    if not username.isalnum():
        return False, "Username can only contain letters and digits."
    return True, "Valid username."

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    if not has_lower:
        return False, "Password must contain at least one lowercase letter."
    if not has_digit:
        return False, "Password must contain at least one digit."
    return True, "Valid password."

# ---- Read input ----
username = input("Enter username: ")
password = input("Enter password: ")

u_valid, u_msg = validate_username(username)
p_valid, p_msg = validate_password(password)

print(f"\nUsername: {u_msg}")
print(f"Password: {p_msg}")

if u_valid and p_valid:
    print("Login credentials are VALID.")
else:
    print("Login credentials are INVALID.")

# ============================================================
# Sample Output:
#   Enter username: John123
#   Enter password: Secure99
#   Username: Valid username.
#   Password: Valid password.
#   Login credentials are VALID.
# ============================================================

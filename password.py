import string
import random

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True,
                      exclude_similar=True, exclude_ambiguous=True):
    similar_chars = 'il1Lo0O'
    ambiguous_chars = '{}[]()/\\\'"`~,;:.<>'

    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Remove similar and ambiguous characters
    if exclude_similar:
        char_pool = ''.join(c for c in char_pool if c not in similar_chars)
    if exclude_ambiguous:
        char_pool = ''.join(c for c in char_pool if c not in ambiguous_chars)

    if not char_pool:
        return "❌ Error: No valid characters left to generate a password!"

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def get_strength(length):
    if length < 6:
        return "Weak 🔴"
    elif length < 10:
        return "Moderate 🟡"
    else:
        return "Strong 🟢"

print("🔐 Creative Password Generator")
try:
    length = int(input("🔢 Enter desired password length: "))
    if length <= 0:
        print("❗ Please enter a positive number.")
    else:
        # Optional settings
        use_upper = input("🔠 Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("🔡 Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("🔢 Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("🔣 Include symbols? (y/n): ").lower() == 'y'
        exclude_similar = input("🚫 Exclude similar characters (like l,1,O,0)? (y/n): ").lower() == 'y'
        exclude_ambiguous = input("🚫 Exclude ambiguous symbols (like { } [ ])? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols,
                                     exclude_similar, exclude_ambiguous)

        print("\n🧾 Your Generated Password:")
        print(f">>> {password}")
        print("📊 Strength:", get_strength(length))

except ValueError:
    print("❗ Invalid input. Please enter a numeric value for length.")

import re

def load_common_passwords(filename):
    try:
        with open(filename, "r", encoding="latin-1") as file:
            return {line.strip().lower() for line in file} #Read file, remove spaces, and convert to lowercase
    except FileNotFoundError:
        print("Error: rockyou.txt not found! Download it from /usr/share/wordlists/ or GitHub: https://github.com/danielmiessler/Seclists")
        return set()
    
# Load passwords from file
common_passwords = load_common_passwords("rockyou.txt")

def check_password_strength(password):

    # Check if password is common
    if password in common_passwords:
         return "Common password found. Please enter a different password."

    # Define password strength criteria
    length = len(password) >= 8
    upper_lower = bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'\d', password))
    special_chars = bool(re.search(r'[@$!%*?&]', password))

    # Calculate the score
    score = sum([length, upper_lower, numbers, special_chars])

    # Determine password strength
    if score == 4:
        return "Strong password man!"
    elif score == 3:
        return "It's okay, could probably do better."
    else:
            return "ts weak as hell boi"
    
while True:
    # Get user input
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

    if strength == "Strong password man!":
         break
import random
import string

print("🔐 Welcome to the Password Generator!")

# Ask user how long they want their password to be 
length = int(input("Enter Password Length : "))

# Define Possible Characters
letters = string.ascii_letters
digits  = string.digits
symbols = string.punctuation

# Combine all characters
all_char = letters + digits + symbols

# Generate password by randomly choosing characters
password = ''.join(random.choice(all_char) for _ in range(length))

# Show the result
print("Your strong password is : ", password)
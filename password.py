import random
import string

# Define a string of all possible characters to use in the password
all_chars = string.ascii_letters + string.digits + string.punctuation

# Generate a random password of a given length
length=int(input("Enter number of digits you need for password:"))
password_chars = random.choices(all_chars, k=length)
password = ''.join(password_chars)

# Print the generated password
print(password)

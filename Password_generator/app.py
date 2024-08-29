#!/usr/bin/bash python3
import random, string

# Get users requirement
length = int(input("Enter the password length: "))
chars = ""

# generate password
include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
 
if include_lowercase:
    chars += string.ascii_lowercase
if include_uppercase:
    chars += string.ascii_uppercase
if include_digits:
    chars += string.digits
if include_special:
    chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
print(password)
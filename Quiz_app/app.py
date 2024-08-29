#!/usr/bin/bash python3

# Initiate a Dictionary for storing questions and result
Bank = {"Name of School": "No name", "Director Name": "Dr. ABC"}

# Get User info and initiate the score
username = input("Hello\nPlease Enter your name: ")
score = 0

# give questions from the dictionary and record the score
for question in Bank:
    score += 1 if input(f"{question}: ") == Bank[question] else 0

# print the result
print(f"You got {score} questions right.\nThank you for your time.")
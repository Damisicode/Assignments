#!/usr/bin/bash python3

# Get number
num = int(input("Enter the table number: "))

# Display Table
for i in range(1, num+1):
    for j in range(1, num+1):
        print(i*j, end="\t")
    print("")
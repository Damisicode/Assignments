#!/usr/bin/bash python3

# Create a dictionary with user IDs and the other details subdictionary
record = {1: {"fname": "ali", "lname": "james", "balance": 0},
          1: {"fname": "fred", "lname": "peters", "balance": 0},
          1: {"fname": "dave", "lname": "joy", "balance": 0},
          1: {"fname": "daniel", "lname": "james", "balance": 0}
        }

# function to deposit
def deposit(user_id, amt):
    if amt:
        record[user_id]["balance"] += amt

    return record[user_id]["balance"]

# function to withdraw
def withdraw(user_id, amt):
    if amt:
        record[user_id]["balance"] -= amt

    return record[user_id]["balance"]

# function to check balance
def check(user_id):
    if user_id in record:
        return record[user_id]["balance"]
    

# Application flow

# Get user record
cur_user_id = int(input("Enter your ID: "))
cur_fname = record[cur_user_id]["fname"]
cur_lname = record[cur_user_id]["lname"]
print(f"Welcome {cur_lname} {cur_fname}")

# Perform Banking Operations
while True:
    action = input("What would you like to do: ").lower()
    if action == "withdraw":
        amount = int(input("How much would you like to withdraw: "))
        bal = withdraw(cur_user_id, amount)
        print(f"You have successfully deposited {amount}\nYour Account balance is {bal}.")
    elif action == "deposit":
        amount = int(input("How much would you like to deposit: "))
        bal = deposit(cur_user_id, amount)
        print(f"You have successfully deposited {amount}\nYour Account balance is {bal}.")
    elif action == "check balance":
        bal = check(cur_user_id)
        print(f"Your Account Balance is {bal}")
    else:
        print(f"Please enter a valid operation from the following: 'deposit', 'withdraw', 'check balance'.")
        continue
    
    status = input("Would you like to perform any other operation (Enter 'Y' for Yes and 'N' for No): ").lower()
    if status == 'y':
        continue
    else:
        break

print("Thank you for using our service.")
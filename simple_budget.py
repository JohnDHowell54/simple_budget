#!/bin/python
import sys
import json
import getopt
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",dest="calc", help="useage: simple_budget -c [BUDGET NAME]")
    parser.add_argument("-l",dest="load", help="useage: simple_budget -l [BUDGET NAME]")
    args = parser.parse_args()
  
    if args.calc:
        calcBudget(args.calc)
    elif args.load:
        loadBudget(args.load)

# Function to go through the budget prompt
def calcBudget(budget):
    print("Welcome to John's Simple Budget. Please note that in rent I have bundled "
          "water, trash, and sewage as that is how my personal situation is set up.\n")

    budget = budget
    income = int(input("Enter your total monthly income: "))

    rent = int(input("Enter your monthly rent: "))
    electric = int(input("Enter your monthly electricity bill: "))
    internet = int(input("Enter your monthly internet bill: "))
    debt = int(input("Enter your monthly debt repayment: "))
    groc = int(input("Enter your weekly grocery bill: "))
    charity = int(input("Enter your monthly charity donations: "))
    save = int(input("Enter your monthly savings: "))
    grocmonth = groc * 4
    
    # Calculate leftover money and provide leftover per month and per day
    leftover = income - (rent + electric + internet + debt + groc + charity)
    leftday = leftover / 30

    # Add all expenses and leftovers to a dict for easy json dumping
    expenses = {'rent': rent, 'electric': electric, 'internet': internet, 'debt': debt, 'charity': charity,
            'groceries': grocmonth, 'savings':save, 'Leftover': leftover, 'Leftover per day': leftday}

    # Check if you can afford your rent by the standard metric of it being 1/3rd of your income
    affrent = income * .33

    if affrent > rent:
        print(
            "Uh oh! Looks like rent is more than 1/3rd of your monthly income. That is generally considered unafforable")
    else:
        print("Congratulations, you can afford your rent!")

    print("Do you have any other expenses? Such as gym, Netflix, etc.: ")
    ans = input()

    if ans == 'y':
        while True:
            exp = input("Enter the name of the expense: ")
            amnt = int(input("Enter the amount: "))
            expenses.update({exp:amnt})

            more = input("Anymore? ")
            if more == 'n':
                break
        
    # Dump all the stuff we just acuired into a json file for ease of reading later
    with open('{0}.json'.format(budget), 'w') as fp:
        json.dump(expenses, fp, indent=4, sort_keys=True)

# Function to read from another budget json file
def loadBudget(budget):
    with open('{0}.json'.format(budget)) as f:
        data = json.load(f)
    print(data)

if __name__ == '__main__':
    main()

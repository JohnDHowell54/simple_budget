import math
import csv
import sys
import json

def calcBudget():
    print("Welcome to John's Simple Budget. Please note that in rent I have bundled "
          "water, trash, and sewage as that is how my personal situation is set up.\n")

    income = int(input("Enter your total monthly income: "))

    rent = int(input("Enter your monthly rent: "))
    electric = int(input("Enter your monthly electricity bill: "))
    internet = int(input("Enter your monthly internet bill: "))
    debt = int(input("Enter your monthly debt repayment: "))
    groc = int(input("Enter your weekly grocery bill: "))
    charity = int(input("Enter your monthly charity donations: "))
    save = int(input("Enter your monthly savings: "))
    grocmonth = groc * 4
    expenses = {'rent': rent, 'electric': electric, 'internet': internet, 'debt': debt, 'charity': charity,
                'groceries': grocmonth, 'savings':save}
    #
    # TODO: Daily/weekly allowance
    # Leftover money, to use as desired. Will factor into a daily allowance later
    #
    leftover = income - (rent + electric + internet + debt + groc + charity)
    leftday = leftover / 30

    leftovers = [leftover, leftday]

    affrent = income * .3


# Print our expenses
for key, val in expenses.items():
    print(key, ':', val)

# TODO Fix this calculation, doesn't properly work
if affrent > rent:
    print("Uh oh! Looks like rent is more than 1/3rd of your monthly income. That is generally considered unafforable")
else:
    print("Congratulations, you can afford your rent!")


# TODO have budgets be persistent
with open('budget.json', 'w') as fp:
    json.dump(expenses, fp, indent=4, sort_keys=True)

# TODO have options to load a budget, save a budget

# TODO have option to export to .tsv 

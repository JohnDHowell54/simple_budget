import math

print("Welcome to John's Simple Budget. Please note that in rent I have bundled "
      "water, trash, and sewage as that is how my personal situation is set up.\n")

income = int(input("Enter your total monthly income: "))

rent = int(input("Enter your monthly rent: "))
electric = int(input("Enter your monthly electricity bill: "))
internet = int(input("Enter your monthly internet bill: "))
debt = int(input("Enter your monthly debt repayment: "))
groc = int(input("Enter your weekly grocery bill: "))
charity = int(input("Enter your monthly charity donations: "))

expenses = [rent, electric, internet, debt, charity]

leftover = income - (rent + electric + internet + debt + groc + charity)
leftday = leftover / 30

leftovers = [leftover, leftday]

affrent = income * .3

for expense in expenses:
    print(expense)

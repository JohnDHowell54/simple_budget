import sys
import json
import getopt


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlc:v]", ["help"])
    except getopt.GetoptError as err:
        print(err)
        printHelp()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-l":
            loadBudget(a)
        elif o in "-c":
            calcBudget(a)
        elif o in ("-h", "--help"):
            printHelp()


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
    expenses = {'rent': rent, 'electric': electric, 'internet': internet, 'debt': debt, 'charity': charity,
                'groceries': grocmonth, 'savings':save}
    #
    # TODO: Daily/weekly allowance
    # Leftover money, to use as desired. Will factor into a daily allowance later
    #
    leftover = income - (rent + electric + internet + debt + groc + charity)
    leftday = leftover / 30

    leftovers = [leftover, leftday]

    affrent = income * .33

    if affrent > rent:
        print(
            "Uh oh! Looks like rent is more than 1/3rd of your monthly income. That is generally considered unafforable")
    else:
        print("Congratulations, you can afford your rent!")

    with open('{0}.json'.format(budget), 'w') as fp:
        json.dump(expenses, fp, indent=4, sort_keys=True)


# Prints a previously made budget for checking
def loadBudget(jsonbudget):
    with open(jsonbudget, 'r') as file:
        data= json.load(file)
    for l in data['budget']:
        print(l)


def printHelp():
    print("-l to load a budget \n-c to calculate a new budget \n -h to print help")
if __name__ == '__main__':
    main()
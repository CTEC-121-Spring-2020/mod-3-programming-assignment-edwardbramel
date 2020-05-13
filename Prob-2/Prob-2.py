# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Edward Lamanna

'''
take user input for name = employees name, wage = hour much they make an hour, and hours = how many hours they work in a week
'''


def main():
    name = input("what is your name?: ")
    wage = input("How much do you make an hour?: ")
    hours = input("in a week how many hours do you work?: ")
    # now the equation is for all hours
    if hours > 40:
        regularWage = 40 * wage
        overtime = (hours - 40) * 1.5 * wage
    else:
        regularWage = hours * wage
        overtime = 0

    total = regularWage + overtime
    # now were doing taxes
    tax = total * .2
    med = total * .1
    takehome = total - (tax + med)
    # now were printing data
    print("Employes Name:", name)
    print("Employes regualr hours:", hours)
    print("you regular wage is:", regularWage)
    print("your overtime wage is:", overtime)
    print("your total wage is:", total)
    print("the total tax withholding is:", tax)
    print("the total medical insurance withholding is:", med)
    print("this is what you take home:", takehome)


main()

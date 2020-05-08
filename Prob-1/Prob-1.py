# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Edward LaManna
"""
Input: ordersubtotal
process: Calculate shipping cost. Cost is $2.99 for totals less than
         $10.00 and zero otherwise
output: return shipping cost
"""


def shippingCost(orderSubTotal):
    shippingCost = 2.99
    x = input
    y = 10.00
    print(input("what is the total coast?: "))
    if x > y:
        print("the shipping cost is 0")
    else:
        print("the shipping cost is 2.99")

    return shippingCost


def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here


if __name__ == "__main__":
    unitTest()

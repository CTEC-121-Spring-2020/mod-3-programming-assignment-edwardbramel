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
    if orderSubTotal >= 10:
        shippingCost = 0

    return shippingCost


def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here
    print("shi[[ing cost if subtotal < 10.00:\t", shippingCost(14.02))


if __name__ == "__main__":
    unitTest()

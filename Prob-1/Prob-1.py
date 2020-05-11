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

    if orderSubTotal < 10:
        shippingCost = 2.99
    else:
        orderSubTotal > 10
        shippingCost = 0

    return shippingCost


def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here


if __name__ == "__main__":
    unitTest()

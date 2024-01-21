# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def calculate_present_value(future_value, discount_rate, compounding_periods, years):
    return future_value / (1 + discount_rate / compounding_periods) ** (compounding_periods * years)

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 650
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
present_value = calculate_present_value(future_value, discount_rate, compounding_periods, years)

# @TODO: Determine if the bond is worth it
if present_value > price:
    print("The bond is worth it.")
elif present_value < price:
    print("The bond is not worth it.")
else:  
    print("The bond is neutral.")

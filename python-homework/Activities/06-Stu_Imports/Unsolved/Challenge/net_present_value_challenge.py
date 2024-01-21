# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library
import numpy_financial as npf

# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {}

# @TODO: Calculate the NPV for each scenario
npv_dict["Conservative"] = npf.npv(discount_rate, cash_flows_conservative)
npv_dict["Neutral"] = npf.npv(discount_rate, cash_flows_neutral)
npv_dict["Aggressive"] = npf.npv(discount_rate, cash_flows_aggressive)


# @TODO: Initialize variables
max_key = ""
max_value = 0

# @TODO: Iterate over npv_dict to find the max key-value pair
for key, value in npv_dict.items():
    if value > max_value:
        max_key = key
        max_value = value



# @TODO: Print out the optimal project scenario with the highest NPV value
print(f"The project with the highest NPV value is the {max_key} project, with expected returns of ${max_value}.")

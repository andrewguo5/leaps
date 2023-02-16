import numpy as np
import datetime
# Homemade Options Pricing Utils

# Given the spot price of the underlier, the strike of the call option, and the current price, return the breakeven price
def c_breakeven(spot, strike, price):
    return(spot-strike+price)

def c_intrinsic_value(spot, strike):
    return(spot-strike)

def c_time_value(spot, strike, price):
    return(price-c_time_value(spot, strike))

# t -> time to maturity, expressed in years
def time_to_maturity(t1, maturity):
    days = np.busday_count(t1, maturity)
    print(days)
    # Assume 252 trading days per year
    return(days/252)

# quick test
t1 = datetime.date(2023, 2, 15)
maturity = datetime.date(2025, 3, 21)

print( time_to_maturity(t1, maturity))
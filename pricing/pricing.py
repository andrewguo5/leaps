from networkdays import networkdays
# Homemade Options Pricing Utils

# Given the spot price of the underlier, the strike of the call option, and the current price, return the breakeven price
def c_breakeven(spot, strike, price):
    return(spot-strike+price)

def c_intrinsic_value(spot, strike):
    return(spot-strike)

def c_time_value(spot, strike, price):
    return(price-c_time_value(spot, strike))

# t -> time to maturity, expressed in years
#def __t(t1, maturity):

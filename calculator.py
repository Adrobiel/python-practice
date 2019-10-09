"""
-----------------------------------------------------
Simple app to calculate equation provided as string
by Dan S
-----------------------------------------------------
"""

# import regular expression and operator modules

import re
import operator

# lookup table as dictionary for supported operators
ops = {
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
        "-": operator.sub
}

# funtion to perform calculation

def calculate(operator, val1, val2):
    if operator == "/" and val2 == 0:
        return "Cannot divide by zero"
    else:
        return ops[operator](val1, val2)

# query user for an equation until "q" is entered to quit

while True:

    eq_str = input("Input equation (q to quit): ")

    if eq_str == "q":
        break
    else:
        eq = re.split(r'(\D)', eq_str.replace(" ", ""))
        try:
            print("{} = {:,}".format(eq_str, calculate(eq[1], int(eq[0]), int(eq[2]))))
        except:
            print("Invalid data was entered: ", eq_str)



#print("End of application")
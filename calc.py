class Simplecalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

# create a function for -
# DOB
import datetime # imported module that gets the current year
def birth_year(age):
    current_year = datetime.date.today().year
    birth_year = current_year - age
    return birth_year
print(birth_year(24))

# %
def percentage(val1, val2):
    return val1 / val2
print(percentage(50,2))

# /
def division(val1, val2):
    return val1 / val2
print(division(10,2))

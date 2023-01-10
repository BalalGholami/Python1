# Exception cost

from timeit import timeit


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        # throwing an exception
        raise ValueError("Age cannot be 0 or Less")    
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass      #yani hich kari nakon
"""

print(timeit(code1, number=100000))


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        # throwing an exception
        return None
    return 10/age


xfactor =    calculate_xfactor(-1)
if xfactor == None:
    pass      #yani hich kari nakon
"""
print(timeit(code2, number=100000))

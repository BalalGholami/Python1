# Exception trhowing
# Own Exceptions

def calculate_xfactor(age):
    if age <= 0:
        # throwing an exception
        raise ValueError("Value Error. \nAge cannot be 0 or Less")
    else:
        print("We are not meet error")
    return 10/age


try:
    calculate_xfactor(-9)
except ValueError as ex:
    print(ex)

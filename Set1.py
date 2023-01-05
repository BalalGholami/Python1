# Set
# majmoue
# onsor tekrari nadarad
# Array1

from array import array
numbers = array("i", [1, 1, 2, 2, 3, 3, 4, 4, 4, 6, 5, 7, 7, 8])
print(type(numbers))
print(numbers)
uniqNumbers = set(numbers)
print(uniqNumbers)
print(len(uniqNumbers))
numbers2 = array("i", [1, 4, 6, 9, 13, 56])
uniqNumbers2 = set(numbers2)
ejtema = uniqNumbers | uniqNumbers2
eshterak = uniqNumbers & uniqNumbers2
dif = uniqNumbers-uniqNumbers2
BejozEshterak = uniqNumbers ^ uniqNumbers2
print(numbers)
print(numbers2)
print("-----------")
print(f"list1= {numbers}")
print(f"list2= {numbers2}")
print(f"Ejtema= {ejtema}")
print(f"Eshterak= {eshterak}")
print(f"Dif= {dif}")
print(f"Bejoz Eshterak= {BejozEshterak}")

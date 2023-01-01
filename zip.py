# zip

list1 = [1, 2, 3]
list2 = [10, 20, 30]
list4 = ("name", "name2", "name3")
# -> list3 = [(1,10),(2,20),(3,30)]

l3 = list(zip(list4, list1, list2))
print(l3)

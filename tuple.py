# Tuples are immutable. hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. then perform operation on that list and convert it back to tuple.

# tup = (1, 2, 76, 342, 32, "green", True)
# # tup[0] = 90
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# # print(tup[34])

# if  3421 in tup:
#   print("Yes 342 is present in this tuple")
# tup2 = tup[1:4]
# print(tup2)


###

# countries = ("Spain", "Italy", "India", "England")
# temp = list(countries)
# temp.append("Dubai")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)

###

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
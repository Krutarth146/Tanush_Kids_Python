# tup1 = (10,20,10,10,{10,20,10})
# # Ordered, Allow's Duplicates, Immutable (Unchangeble)
# print(tup1)   # (10, 20, 10, 10, {10, 20})

# print(tup1[1])  # 20  # int
# print(tup1[1:3])  # (20,10)  # tuple
# print(tup1[1:2])  # (20,)  # Tuple

# print(type(29))   # <class 'int'>
# print(type((29,)))   # <class 'tuple'>

# print(tup1.count(10))   # 3
# print(tup1.index(10))   # 0

# tup1 = list(tup1)

# tup1.append("Amana")

# tup1 = tuple(tup1)

# print(tup1)


# tup2 = (10,90,89)

# tup1 += tup2
# print(tup1)   # (10, 20, 10, 10, {10, 20}, 'Amana', 10, 90, 89)


# t9 = ((10,20), (40,50))
# l1 = []
# for subtup in t9:
#     # print(subtup)
#     for ele in subtup:
#         # print(ele)
#         l1.append(ele)

# print(tuple(l1))  # (10, 20, 40, 50)


# # ------------------------------------------------------

dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = set()
print(type(set1))   # <class 'set'>

# Dict : ---> Ordered (No Index), Don't Allow Duplicates (Unique Keys), Mutable (Changeble)
dict2 = {'Name' : 'Manav', 'Roll' : 903, 'School' : 'HBK'}

print(dict2)   # {'Name': 'Manav', 'Roll': 903, 'School': 'HBK'}

print(dict2['Name'])   # Manav
print(dict2.get('name'))   # None

dict2["address"] = 'AHm'
print(dict2)   # {'Name': 'Manav', 'Roll': 903, 'School': 'HBK', 'address': 'AHm'}

dict2["School"] = "Xaviers"
print(dict2)   # {'Name': 'Manav', 'Roll': 903, 'School': 'Xaviers', 'address': 'AHm'}

dict2.update({'SurName' : 'Agarwal'})
print(dict2)   # {'Name': 'Manav', 'Roll': 903, 'School': 'Xaviers', 'address': 'AHm', 'SurName': 'Agarwal'}


del dict2['Roll']

print(dict2)
dict1 = {}
print(type(dict1))   # Dict

set1 = {10}

print(type(set1))   # set

dict2 = {10:20}
print(dict2)   # {10 : 20}

set2 = set()  # using constructor   # Blank set

print(type(set2))   # set

set1 = {10,20,90,34,10,10,10}   # unordered (No Indexing), Unchangeble (We can add or remove Elements), Don't Allow Duplicates
print(set1)   #  {10,90,34,20}

# print(set1[0])   # Error


set1 = {10,220.90,'String', True, (10,20,301,10)}
print(set1)   # {True, (10, 20, 301, 10), 10, 220.9, 'String'}


set2 = {10,20}

# set1+=set2
# print(set1)  # Error

# **Unchangeble (can add or Remove Elements)
set1.add("20")
set1.add(30)
set1.add(('Aman', 'Manoj'))
print(set1)   # {True, '20', (10, 20, 301, 10), 10, 220.9, 30, 'String'}

set1.remove(True)
set1.discard(30)
print(set1)   # {('Aman', 'Manoj'), (10, 20, 301, 10), 'String', '20', 10, 220.9}


# -----------------------
# set1.discard('Z')   # It ignores if element is not Found
# print(set1,'---------------------')   # {'20', 'String', (10, 20, 301, 10), 10, ('Aman', 'Manoj'), 220.9} ---------------------
# set1.remove('Z')   # I will generate an Error if ele is Not Found


set1.update({10,202,90})

print(set1)   # {('Aman', 'Manoj'), 10, 202, 'String', (10, 20, 301, 10), 90, '20', 220.9}


# set1.clear()
# print(set1)  # set()


# del set1
# print(set1)

print(set1.pop())    # ('Aman', 'Manoj')
print(set1)  


set2 = set1.copy()  # Shallow Copy

set1.add(19)
print(set2)   # {90, 'String', (10, 20, 301, 10), '20', 202, 10, 220.9}
print(set1)   # {10, 'String', 202, 19, (10, 20, 301, 10), 90, ('Aman', 'Manoj'), 220.9}



# ---------------------------------------

set1 = {10,20,30}
set2 = {30,40,50}

print(sorted(set1.union(set2)))  # [10, 20, 30, 40, 50]

print(set1.intersection(set2))   # {30}

# set1.intersection_update(set2)

# print(set1)   # {30}

print(set1.difference(set2))   # {10,20}

print(set1.symmetric_difference(set2))   # {40, 10, 50, 20}


set1 = {10,12,13}
set2 = {90,56,78}
print(set1.isdisjoint(set2))   # True

set1 = {10,12,13}
set2 = {90,56,78,10,12,13}
print(set1.issubset(set2))   # True


print(set1.issuperset(set2))  # False
print(set2.issuperset(set1))  # True
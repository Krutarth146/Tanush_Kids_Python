# Typecasting -> One datatype to another Datatype

# 1. Implicit Typecasting
# 2. Explicit Typecasting


n = True
q = 89

print(n+q)  # 90   # Implicit Typecasting

_dhiraj_sir = '34.99'
g = '90'
# print(_dhiraj_sir + 'jk')
print(int(float(_dhiraj_sir)))   # 34  # Explicit typecasting

import math
d = float('34.999999999')
print(math.fabs(-56.90))
print(math.floor(d))   # 34
print(math.ceil(d))   # 35

# print(-18//4)    # -5

# x = input()
# y = input()
# print(x+y)


# # List    -> Allow Duplicates, 

array1 = [10,20,30,40,50]


list1 = [10,10,32.90, True, [(10,20,30), (40,50,60)], {10,20,10}, {"Name" : "Krutarth", 'address' : {'City' : "Ahm", 'pincode' : 380001}}]
print(list1)   # [10, 10, 32.9, True, [(10, 20, 30), (40, 50, 60)], {10, 20}, {'Name': 'Krutarth', 'address': {'City': 'Ahm', 'pincode': 380001}}]

list1=  tuple(list1) 
print(list1)   # (10, 10, 32.9, True, [(10, 20, 30), (40, 50, 60)], {10, 20}, {'Name': 'Krutarth', 'address': {'City': 'Ahm', 'pincode': 380001}})
print(type(list1))  # <class 'tuple'>

# Indexing
print(list1[4])  # [(10, 20, 30), (40, 50, 60)]
print(list1[-1])  # {"Name" : "Krutarth", 'address' : {'City' : "Ahm", 'pincode' : 380001}}

# Slicing

# print(list1[start : end(n-1)])

list2 = [10,20,30,40,50,60]

print(list2[0 : 4])  # [10,20,30,40]
print(type(list2[0 : 4]))  # <class 'list'>

print(type(list2[2:3]))   # <class 'list'>   # 30
print(list2[4:1:1])   # []
print(list2[-7:-2])   # [10, 20, 30, 40]
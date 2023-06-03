list1 = ['D', 'G']

ans = {'D' : {'D' : ['DD','DG'], 'G' : ['GG', 'GD']} , 'G' : {'G' : ['GG','GD'], 'D' : ['DD', 'DG']}}


list1 = [] 
print(type(list1))    # <class 'list'>

tup1 = ()
print(type(tup1))   # <class 'tuple'>

dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = {10}
print(type(set1))   # <class 'set'>


# list -> Ordered (Indexed), Mutable(Changeble), Allow Duplicates

list1 = [10,20,30,40,10]
print(list1[3])   # 40

list1.append(400)
print(list1)   # [10, 20, 30, 40, 10, 400]

# Tuple -> Ordered (Indexed), Allow Duplicates, Immutable (Not Changeble)
tup1 = (30,40,50,20, 20)
print(tup1[3])   # 20
print(tup1)  # (30, 40, 50, 20, 20)

# Dictionary -> Ordered, Don't Allow Duplicates, Mutable (Changeble)

dict1 = {"Name" : "Manoj", 'Roll' : [10,20,30,40,50], "Address" : True, "Name" : "jkl"}

print(dict1)   # {'Name': 'jkl', 'Roll': [10, 20, 30, 40, 50], 'Address': True}
# key is Name
# value is "Manoj"


# Set -> Unordered, Don't Allow Duplicates, Immutable (but We can add and remove Elelments)

set1 = {10,20,30,40,50,10,20,30,40,50,88}
print(set1)   # {50, 20, 40, 10, 88, 30}

set1.add(300)
print(set1)   # {50, 20, 40, 10, 88, 300, 30}


# print(set1[0])   # Gives Error


str1 = "MISSISSIPPI"

list1 = list(str1)

print(list1)   # ['C', 'o', 'm', 'p', 'u', 't', 'e', 'r']
dict1= {}
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

print(dict1)  # {'M': 1, 'I': 4, 'S': 4, 'P': 2}
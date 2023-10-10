# Dictionary ---> key - Value Pairs, Ordered (Not Indexed)

dict1 = {}
print(type(dict1))

dict1 = {10}
print(type(dict1))   # set

set1 = set()  # Constructor

print(type(set1))   # <class 'set'>

dict2 = {'Name' : 'Krutarth', 'roll' : 90, 'address' : [{'City' : ['Ahm', 'Gnr']}]}

print(dict2['Name'])   # Krutarth
print(dict2['address'][0]['City'][0])   # Ahm


dict2 = {'Name' : 'Krutarth', 'Roll' : 900}

print(dict2.keys())  # dict_keys(['Name', 'Roll'])


for k in dict2:
    print(k)


for k in dict2.keys():
    print(k)

for k in dict2.values():
    print(k)   # Krutarth  900

for n in dict2.items():
    print(n)

for key,val in dict2.items():
    print(key,'---->',val)   # Name ----> Krutarth  Roll ----> 900


dict2['Name'] = 'Manoj'
print(dict2)   # {'Name': 'Manoj', 'Roll': 900}

dict2['address'] = 'Gnr'
print(dict2)   # {'Name': 'Manoj', 'Roll': 900, 'address': 'Gnr'}

dict2.update({90 :89, 'Name111' : 'Aaman'})

print(dict2)   # {'Name': 'Manoj', 'Roll': 900, 'address': 'Gnr', 90: 89, 'Name111': 'Aaman'}

print(dict2['address'])   # Gnr
print(dict2.get('address'))   # Gnr
print(dict2.get('add'))   # None
# print(dict2['add'])   # Error
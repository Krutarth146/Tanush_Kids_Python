dict1 = {'Name' : 'Tanush', 'Roll' : 90, 'Address' : 'Shahpur'}

dict1['Money'] = 900
print(dict1)   # {'Name': 'Tanush', 'Roll': 90, 'Address': 'Shahpur', 'Money': 900}


dict1.update({'Bank' : 'SBI', 'Ac_no' : 90034})

print(dict1)   # {'Name': 'Tanush', 'Roll': 90, 'Address': 'Shahpur', 'Money': 900, 'Bank': 'SBI', 'Ac_no': 90034}


# del dict1

del dict1['Ac_no']
print(dict1)   # {'Name': 'Tanush', 'Roll': 90, 'Address': 'Shahpur', 'Money': 900, 'Bank': 'SBI'}

# dict1.clear()
# print(dict1)

x = dict1.pop('Roll')
print(f'Removed Element is {x}.')    # Removed Element is 90.
print('Removed Element is ',x,'.',sep='')   # Removed Element is 90.

print(dict1)


print(dict1.popitem())


print(dict1)   # {'Name': 'Tanush', 'Address': 'Shahpur', 'Money': 900}
print(dict1.get('Roll'))   # None
print(dict1.get('Name'))   # Tanush


# print(dict1['Roll'])   # Error
print(dict1['Name'])   # Tanush

print(dict1.values())   # dict_values(['Tanush', 'Shahpur', 900])

print(dict1.keys())   # dict_keys(['Name', 'Address', 'Money'])

print(dict1.items())   # dict_items([('Name', 'Tanush'), ('Address', 'Shahpur'), ('Money', 900)])



# {'Name': 'Tanush', 'Address': 'Shahpur', 'Money': 900}
dict1.setdefault('Tanush',90)
dict1.setdefault('Money',200)
print(dict1)   # {'Name': 'Tanush', 'Address': 'Shahpur', 'Money': 900, 'Tanush': 90}


# list1 = [10,20,30]
dict8 = dict.fromkeys(['Bank_Name', 'Bank_Ac', 'Bank_Cust_id'], None)
print(dict8)   # {'Bank_Name': None, 'Bank_Ac': None, 'Bank_Cust_id': None}


str1 = 'Mississippi'

ans = {'M' : 1, 'i' : 4, 's' : 4, 'p' : 2}

res = {}

for k in set(str1):   # {'M', 'i', 's', 'p'}
    res.update({k : str1.count(k)})

print(res)   # {'i': 4, 'M': 1, 's': 4, 'p': 2}
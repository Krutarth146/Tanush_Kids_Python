# array1 = [10,20,30,40,50]

list1 = []   # Mutable (Changeble), Ordered, Allow's Duplicates
print(type(list1))   # <class 'list'>


list2 = [90, 89.89, True, [10,20], (908,78), {89,89,90}, {"Name" : ['Tanush', 'Krutarth']}]
print(list2)   # [90, 89.89, True, [10, 20], (908, 78), {89, 90}, {'Name': ['Tanush', 'Krutarth']}]

print(len(list2))  # 7 # Length starts from 1, Index starts from 0

print(list2.__sizeof__())  # 96
print(id(list2))   # 2553216186112

list2 = [10, 90.90, 789, 54.32, True, 0.7]
print(max(list2))  # 789
print(min(list2))  # 0.7

print(sum(list2) // len(list2))  # 157.0

list1 = [10,90,89,78,67,56,10,90,89]


# Indexing
print(list1[0]) # 10

# Slicing
print(list1[2:5]) # [89,78,67]
print(list1[-2:-6]) # []
print(list1[-6:-2]) # [78, 67, 56, 10]
print(list1[4:1:2]) # []
print(list1[4:1:-2]) # [67, 89]
print(list1[::1]) # [10, 90, 89, 78, 67, 56, 10, 90, 89]
print(list1[::-1]) # [89, 90, 10, 56, 67, 78, 89, 90, 10]
print(list1[::-3]) # [89, 56, 89]
print(list1[-3:2:2]) # []


# List Methods

list1.append("Tanush")
print(list1)  # [10, 90, 89, 78, 67, 56, 10, 90, 89, 'Tanush']

list1.extend("Tanush")
list1.extend([500,900,89])
print(list1)  # [10, 90, 89, 78, 67, 56, 10, 90, 89, 'Tanush', 'T', 'a', 'n', 'u', 's', 'h']

list1.insert(2,9000)
print(list1)  # [10, 90, 9000, 89, 78, 67, 56, 10, 90, 89, 'Tanush', 'T', 'a', 'n', 'u', 's', 'h', 500, 900, 89]

list1[-3] = 7800

print(list1)  # [10, 90, 9000, 89, 78, 67, 56, 10, 90, 89, 'Tanush', 'T', 'a', 'n', 'u', 's', 'h', 7800, 900, 89]


# --------------------------------------
list1.pop()
list1.pop()
print(list1.pop())  # 7800
print(list1)  # [10, 90, 9000, 89, 78, 67, 56, 10, 90, 89, 'Tanush', 'T', 'a', 'n', 'u', 's', 'h']


list1.pop(4)
print(list1)   # [10, 90, 9000, 89, 67, 56, 10, 90, 89, 'Tanush', 'T', 'a', 'n', 'u', 's', 'h']


list1.remove('Tanush')
print(list1)  # [10, 90, 9000, 89, 67, 56, 10, 90, 89, 'T', 'a', 'n', 'u', 's', 'h']

del list1[2:]
print(list1)   # [10, 90]


# list1.clear()
# print(list1)  #[]

list2 = list1.copy()  # Shallow Copy
list3 = list1   # Deep Copy


list3.append(600)
print(list1)  # [10, 90, 600]
print(list2)   # [10, 90]
list1.append(10)
print(list1.count(10))  # 2
print(list1.index(10))  # 0
list1.sort()
print(list1)  # [10, 10, 90, 600]


list1.sort(reverse=True)
print(list1)   # [600, 90, 10, 10]
  

# list1.reverse()
# print(list1)



list1 = [10,90,78,566,32]
user_need = int(input())

for i in list1:
    # print(i)
    if user_need == i:
        print("Element is FOund")
        break
else:
    print("Elemnet is Not Found")
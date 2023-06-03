list1 = [30,40,20,190,203,405,50]

# print(list1[start : end : step])
print(list1[:5:])  # [30, 40, 20, 190, 203]

print(list1[3:8:2])  # [190,405]

print(list1[2:3])  # [20]
print(type(list1[2:3]))  # <class 'list'>  # Slicing

print(type(list1[2]))  # <class 'int'>  # Indexing

list1 = [30,40,20,190,203,405,50]
print(list1[5:1])  # []

print(list1[-4:-1])  # [190, 203, 405]

print(list1[::-1])  # [50, 405, 203, 190, 20, 40, 30]
print(list1[::-2])  # [50, 203, 20, 30]
print(list1[:-5:])  # [30, 40]
print(list1[:-5:-1])  # [50, 405, 203, 190]
print(list1[-3:3:2])  # []


# List Methods

list1 = [10,20,30,40,50,60,12,23,4455]

list1.append(9000)
print(list1)  # [10, 20, 30, 40, 50, 60, 12, 23, 4455, 9000]

list1.append("Tanush")
print(list1)

# list1.extend(900)   Gives Error

list1.extend("Tan")
print(list1)  # [10, 20, 30, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n']


list2 = [10,20,22,33,11]

# list1.append(list2)
# print(list1)  # [10, 20, 30, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', [10, 20, 22, 33, 11]]

# print(len(list1)) # 15

list1.extend(list2)
print(list1)  # [10, 20, 30, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 11]

print(len(list1))  # 19


list1.insert(3,4000)
print(list1)  # [10, 20, 30, 4000, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 11]

list1.insert(-1,3000)
print(list1)  # [10, 20, 30, 4000, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 3000, 11]

list1[-1] = 6000

print(list1)   # [10, 20, 30, 4000, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 3000, 6000]

# Remove Element


list1.pop()
print(list1)  # [10, 20, 30, 4000, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 3000]

ele = list1.pop(2)
print(list1)  # [10, 20, 4000, 40, 50, 60, 12, 23, 4455, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 3000]

print(ele)  # 30

list1.remove(4455)
print(list1)  # [10, 20, 4000, 40, 50, 60, 12, 23, 9000, 'Tanush', 'T', 'a', 'n', 10, 20, 22, 33, 3000]
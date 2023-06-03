list1 = [1,3,4,5,6]

list2 = [int(x) for x in range(1,11) if x % 2 == 0]    # List Comprehension
print(list2)   # [2, 4, 6, 8, 10]


# even = []
# for i in list1:
#     if i % 2 == 0:
#         even.append(i)

# print(even)


list1 = [1,3,4,5,6]

square = [x*x for x in list1]
print(square)    # [1, 9, 16, 25, 36]

cube = [x*x*x for x in list1]
print(cube)    # [1, 27, 64, 125, 216]

cub1 = [(x,x*x) for x in list1]
print(cub1) # [(1, 1), (3, 9), (4, 16), (5, 25), (6, 36)]


# Map
 
# Convert Str elements into Int elements using Map

# lst3 = ["2", "4", "7", "1", "90"]

# lst3 = list(map(int, lst3))

# print(lst3)    # [2, 4, 7, 1, 90]

def square(x):
    return(x*x)


# # 1. Without return type and without Args.

# def play():
#     print("Hello Tanush!")

# play()    # Hello Tanush!

# # 2. Without return type and with Args.


# def add(a,b,c):
#     print(a+b+c)

# add(10,20,30)    # 60


# # 3. With return type and without Args.

# def div():
#     a = 60
#     b = 2
#     return a//b

# print(div())   # 30

# # 4. With return type and with Args.

# def mul(a,b):
#     return a*b

# e = mul(20,10)

# print(e)    # 200


# def square(x):
#     return(x*x)

# list3 = list(map(float, list1))
# print(list3)   # [1.0, 3.0, 4.0, 5.0, 6.0]



# list3 = list(map(square, list1))
# print(list3)   # [1, 9, 16, 25, 36]



# list1 = []
# a = int(input("Enter the Number: "))
# list1.append(a)
  
# print(list1)    # [34]

#  lst1 = []
# num = int(input("Enter frequency: "))

# for i in range(num):
#     a = int(input("Enter One Number: "))
#     lst1.append(a)

# print(lst1)    # [45, 67, 12]#

# lst2 = [int(i) for i in input().split()]
# print(lst2)    # [34, 2, 31, 56, 78, 90000, 2000]

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f1(num):
    if num > 5:
        return num

list3 = list(filter(f1, list3))
print(list3)

# print(f1(10))


import functools

list1 = [1, 2, 3, 4, 5]

list1 = functools.reduce(lambda a, b : a+b, list1)

print(list1)
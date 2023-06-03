# Datatypes, Typecasting, Variables, print, input

print('Hello Tanush!')
print('''
    Tanush
    Ahmedabad
    380001
    ....
    ''')

print("Hello Krutarth",end=' Tanush ')
print("Good Evening!")  # Hello Krutarth Tanush Good Evening!


# Python Interpreted (Line By Line), Dynamic Language

# int x
# float y
# char c

x = 90
print(x)   # 90
print(type(x))  # <class 'int'>

y = 89.78
print(type(y))   # <class 'float'>

s = "w"
print(type(s))   # <class 'str'>

j = True
print(type(j))   # <class 'bool'>

w = 23 + 90j
print(type(w))   # <class 'complex'> -> 23 is Real Part, 90j is Imaginary Part

print(23 + w)   # (46+90j)
print(23j + w)   # (23+90j)

list1 = [10,20,30,40,50,89.90, True, [10,203,40] , (20,30,40,50), {10,203,40}, {"Name" : "Krutarth", "Roll" : 34}]
print(list1)  # [10, 20, 30, 40, 50, 89.9, True, [10, 203, 40], (20, 30, 40, 50), {40, 10, 203}, {'Name': 'Krutarth', 'Roll': 34}]
print(type(list1))   # <class 'list'>

tup1 = (10,20,30,40,50,89.90, True, [10,203,40] , (20,30,40,50), {10,203,40,40,40}, {"Name" : "Krutarth", "Roll" : 34})
print(tup1)   # (10, 20, 30, 40, 50, 89.9, True, [10, 203, 40], (20, 30, 40, 50), {40, 10, 203}, {'Name': 'Krutarth', 'Roll': 34})
print(type(tup1))   # <class 'tuple'>

set1 = {10,203,40,40,40}

print(set1)  # {40, 10, 203}
print(type(set1))   # <class 'set'>

dict1 =  {"Name" : "Krutarth", "Roll" : 34}
print(dict1)
print(type(dict1))   # <class 'dict'>

x = "Royal"
y = "Techno"

print(x,y,sep="\n")   # Royal 
                    #   Techno


x = 78
# print(type(x))   # <class 'int'>

# y = int(input("Enter Any Number: "))
# print(y)   # 23
# print(type(y))   # <class 'str'>

# print(x+y)

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

print(num1,"+",num2,"=",num1+num2)   # 20 + 10 = 30
print(f"{num1} - {num2} = {num1-num2}")   # 20 + 10 = 30
print(f"{num1} * {num2} = {num1*num2}")   # 20 + 10 = 30
print(f"{num1} / {num2} = {num1/num2}")   # 25 / 2 = 12.5
print(f"{num1} // {num2} = {num1//num2}")   # 25 // 2 = 12  (Floor Division)
print(f"{num1} ** {num2} = {num1**num2}")   # 25 ** 2 = 625 (Exponencial) # 25 * 25
print(f"{num1} % {num2} = {num1%num2}")   # 25 % 2 = 1
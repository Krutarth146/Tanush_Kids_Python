# Function ----> Code Usability

def Play():   # Func. Defination
    print("Sachin is Good Cricketer")



# Play()   # func. Calling
# Play()
# Play()
# # Play()
# Play()
# Play()
# Play()

# Inbuilt Function -----> len(), max(), min(), id(), print(), input()
# User-defined FUnctions ----> Play()

# -------------------------------------------------

# UDF
# 1. without Return Type and without Arguments


def Tanush():
    a,b = 90,89
    a = a + 10
    print(a,b,a*b)

Tanush()  # 100 89 8900


# 2. without Return Type and with Argument

def kru(num1 = 89, data = 1):   # Default Function
    print(num1 * data)

kru('Aman ', 2) # Aman Aman
kru('Aman ')  # Aman
kru()  # 89


# --------------------------------------

def tanush1(a1,a2,*args,a3 = 10):
    print(args)
    print(type(args))  # <class 'tuple'>

    print(args[-1])   # [10, 20]

tanush1(10,90.89, True,[10,20],'str1',90,20)  # (10, 90.89, True, [10, 20])



def Agarwal(*args, **kwargs):
    print(kwargs)   # {'name': 'Tanush', 'Roll': 90, 'address': 'Ahm'}

    print(kwargs['address'])  # Ahm

    for i in kwargs.items():
        print(i)

Agarwal(10,20,30,name = "Tanush", Roll = 90, address = 'Ahm')


def Ayush():
    return 90

print(Ayush())   # 90
x = Ayush()
print(x)

def Royal():
    return [10,20,30], "Aamana" , 90


print(Royal()[1])  # Aamana



# def Tan():
#     def Aam():
#         print("Inside Aam Function")
#     print("Inside Tan Function")
#     return Aam()

# Tan()
# def Dev(aman):
#     def Tanush(rama):
#         print("Inside Tanush FUnction")
#         return rama()
#     print("Inside Dev FUnction")
#     return Tanush(aman)

# def Agni():
#     print("This is Agni Function")


# Dev(Agni)


def Royal(student):
    def Aman(x):
        print("This is Aman FUnction")
    print('This is Royal Function')
    return Aman(student)

@Royal   # Custom Decorator ----> Django (Web-Application) & Oops (Object Oriented Concepts)
def Student():
    print("This is Diwali gettoGather")

# Royal(Student)


# @classmethod, @staticmethod ---> Inbuilt Decorator


# Type - 4

def power(x,y):
    return x ** y


print(power(4,3))   # 4**3 ---> 4*4*4  ->  64


#- ----------------------------------------------
def Series(num):
    list1 = []
    for j in range(1,num+1):
        # print(j,end=' ')   # 1 2 3 4 5 6 7 8 9 10
        list1.append(j)
    return list1


print(Series(10))   # 1


#- ----------------------------------------------

# Generators (yield Keyword)

def Series(num):
    list1 = []
    for j in range(1,num+1):
        yield j


x = Series(10)

print(x)
print(x.__next__())   # 1
print(x.__next__())   # 2
print(x.__next__())   # 3


for k in Series(10):
    print(k)   # 1 2 3 4 5 6
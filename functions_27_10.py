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
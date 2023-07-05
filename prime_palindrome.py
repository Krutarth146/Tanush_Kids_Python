# 23 ----> 1,23
# 24 ----> 1,2,3,4,6,8,12,24
# 29 ----> 1,29
# 31 ----> 1,31
# 44 ----> 1,2,4,11,22,44

num = 31

factors = 0

k = 1
while k<=num:
    if num % k == 0:
        print(k,end=' ')  # 1 2 3 4 6 8 12 24 
        factors+=1
    k+=1

print(factors)

if factors == 2:
    print("Prime Number")


# ------------------------------------


num = 982 # ----> 289

# while num != 0:
while num > 0:
    print(num % 10,end='')  # 289
    num = num // 10   # 0

# ---------------------------------
print()
print()
# Sum of Digits

num = 902631
sum = 0


while num > 0:
    rem = num % 10   # rem = 9
    if rem % 2 == 1:
        sum = sum + rem  # sum =  13
    num = num // 10  # num = 0


print(sum)  # 13

# ----------------------------------
print()
print()
# 

num = 902631
sum = 0


while num > 0:
    rem = num % 10   # rem = 
    sum = sum*10 + rem  # sum =  
    num = num // 10  # num = 


print(sum) 
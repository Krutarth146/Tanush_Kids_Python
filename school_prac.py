# 1] Different statements 
# 2] palindrome no
# 3] factorial
# 4] HELLO@123
# replace HELLO with hello
# @ with #
# 123 with %


# 1] Different statements

# break, continue, pass


# break

# j = 5

# while j<=15:   # 10 <= 15

#     print(j,end=' ')  # 5 6 7 8 9

#     if j==10:  # 10 == 10
#         break

#     j+=1


# # ---------------------
# # pass
# name = 'Manoj'

# if name == "Manoj":
#     pass
# else:
#     print("Tanush")


# # ---------------------------
# # continue

# for i in range(25,33):
#     if i == 28:
#         continue
#     print(i)


# k = 1
# while k<=10:
#     if k==5:
#         continue
#     print(k)
#     k+=1


# --------------------------------------

# 2] palindrome no


# SUm of Digits
# num = 732   # ---> 237
# sum = 0


# while num != 0:
#     rem = num % 10    # rem = 7
#     sum = sum + rem   # sum = 12
#     num = num // 10   # num = 0


# print(sum)


num = 373
sum = 0
replika = num

while num != 0:
    rem = num % 10    # rem = 3
    sum = sum * 10 + rem   # sum = 173
    num = num // 10   # num = 0


print(sum)

if replika == sum:   # 0 == 373
    print("Palindrome Number")


# 3] factorial
# 5! = 5*4*3*2*1

num = 5
mul = 1

for i in range(1,num+1):   # 1 to 5
    mul = mul * i   # 6 = 6 * 3

print(mul)  # 120


# 4] HELLO@123
# replace HELLO with hello
# @ with #
# 123 with %

str1 = "HELLO@123"

str1 = str1.lower().replace('@', '#')   # hello#123

for i in range(len(str1)):
    if str1[i].isnumeric():
        str1 = str1.replace(str1[i], '%')

print(str1)   # hello#%%%
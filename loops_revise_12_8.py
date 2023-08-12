# Loop ---> 1. start  2. End(Condition)  3. Flow (Incre / Decre)

# 35 to 45

tanush = 65
while tanush >= 55:
    print(tanush,end=' ')   # 65 64 63 62 61 60 59 58 57 56 55 
    tanush-=1

print()
for kru in range(35,46):
    print(kru,end=' ')   # 35 36 37 38 39 40 41 42 43 44 45

print()
for h in range(65,54,-1):
    print(h,end=' ')   # 65 64 63 62 61 60 59 58 57 56 55

# 43 * 1 = 43

# 15. Write a Python program to check the validity of passwords input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = "man2222@sssssW"
upper = 0
lower = 0
num = 0
sp = 0
print()

if len(password) >= 6 and len(password) <= 16:
    for i in password:
        if i >= 'A' and i<='Z':
            upper += 1
        elif i >= 'a' and i<= 'z':
            lower+=1
        elif i >= '0' and i<= '9':
            num+=1
        else:
            sp+=1

    if upper>=1 and lower >=1 and num >= 1 and sp>=1:
        print("Valid Password")
    else:
        print("Try Again")
else:
    print("Try Again")

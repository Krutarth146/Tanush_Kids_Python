l1= [10,20,309,40]

for i in l1:
    print(i,end=' ')  # 10 20 309 40

print()

l2 = [i for i in l1]
print(l2)  # [10, 20, 309, 40]

print()

d2 = [[10,20,30], [30,40,50], [90,11,12]]

# 2d to 1d

# str1 = [i for i in input()]

# print(str1)   # ['T', 'a', 'n', 'u', 's', 'h']

str2 = [int(i) for i in input().split()]
print(str2)  # [10, 90, 89, 78]
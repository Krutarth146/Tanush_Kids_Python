l1= [[10,20,30],
     [90,89,78],
     [32,78,45]]

print(l1)   # [[10, 20, 30], [90, 89, 78], [32, 78, 45]]


for i in l1:
    print(i) 
# [10, 20, 30]
# [90, 89, 78]
# [32, 78, 45]

for j in l1:  # j = [10, 20, 30]
    for k in j:
        if k % 2 != 0:
            print(k,end=' ')   # 89 45


    

l1= [[10,20,30],
     [90,89,78],
     [32,78,45]]

print()
for i in range(len(l1)):  # 3  ---> 0 to 2
    if i % 2 == 0:
        for j in range(len(l1[i])):
            print(l1[i][j],end=' ')
    else:
        for j in range(len(l1[i])-1, -1, -1):
            print(l1[i][j],end=' ')

    print()

# 10 20 30
# 78 89 90
# 32 78 45

l1= [[10,20,30],
     [90,89,78],
     [32,78,45]]


sum = 0
cross = 0
for row in range(len(l1)):  # 0 to 2
    for col in range(len(l1[row])):  # 0 to 2
        if row == col:
            sum += l1[row][col]


for row in range(len(l1)):  # 0 to 2  # i = 0
    cross += l1[row][len(l1)-1-row]

print(cross)  # 151  # 30 + 89 + 32


print(sum)  # 135   # 10 + 89 + 45
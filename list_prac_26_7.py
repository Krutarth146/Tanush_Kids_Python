list1 = [[10,20,30],
         [40,66,22],
         [90,78,67]]


for i in list1:  
    print(i)  # [10,20,30]  [40,66,22]


for x in range(len(list1)):
# for x in range(3):  # 0,1,2
    print(list1[x])

print('--------------')
for y in range(len(list1)):
    for v in range(len(list1[y])):   # list1[0]  # 3 ---> 0,1,2
        print(list1[y][v])   # list1[0][2]
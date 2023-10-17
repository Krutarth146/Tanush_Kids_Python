list1 = [10,20,31,24,22]
main = []
dict1 = {}


for num in list1:
    # print(num)

    # num = 10  ---> 1,2,5,10
    temp = []
    for i in range(1,num+1):  # 1 to 10
        if num % i == 0:  # 10 % 1 == 0
            temp.append(i)

    # print(temp)
    dict1[num] = temp
    main.append(temp)

print(main)   # [[1, 2, 5, 10], [1, 2, 4, 5, 10, 20], [1, 31], [1, 2, 3, 4, 6, 8, 12, 24], [1, 2, 11, 22]]
print(dict1)   # {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 31: [1, 31], 24: [1, 2, 3, 4, 6, 8, 12, 24], 22: [1, 2, 11, 22]}



# Dict Comprehension

ans = {num : [i for i in range(1,num+1) if num % i == 0] for num in list1 }
print(ans)  # {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 31: [1, 31], 24: [1, 2, 3, 4, 6, 8, 12, 24], 22: [1, 2, 11, 22]}
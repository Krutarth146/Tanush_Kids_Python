tup1 = ()
print(type(tup1))   # <class 'tuple'>

tup2 = (90, 90, 90, 89.78, "Tanush", 'N', True, 89+9j, [10,20], ((10,20),(30,20)), {20,90}, {"Name" : "Rishita"})

print(tup2)   # (90, 89.78, 'Tanush', 'N', True, (89+9j), [10, 20], ((10, 20), (30, 20)), {90, 20}, {'Name': 'Rishita'})

print(type(tup2))  # <class 'tuple'>

print(tup2.__sizeof__())  # 104
print(len(tup2))  # 10 (Length starts from 1, Index starts from 0)

# Tuple -> Ordered (Indexed), Imutable (Not Changeble) , Allow's Duplicates

# print(type(tup2[2]))  # Tanush   # <class 'str'>
# print(tup2[2:7])  # ('Tanush', 'N', True, (89+9j), [10, 20])
# print(type(tup2[2:3])) # ('Tanush')  # <class 'tuple'>

print(tup2[3:-2:3])  # ('N', [10, 20])
print(tup2[-3:5:2])  # ()

print(tup2.index(((10,20),(30,20))))   # 9

print(tup2.count(90))  # 3

tup2 = list(tup2)
tup2.append(3000)
print(tup2)  # [90, 90, 90, 89.78, 'Tanush', 'N', True, (89+9j), [10, 20], ((10, 20), (30, 20)), {90, 20}, {'Name': 'Rishita'}, 3000]

tup2 = tuple(tup2)
print(tup2)   # (90, 90, 90, 89.78, 'Tanush', 'N', True, (89+9j), [10, 20], ((10, 20), (30, 20)), {90, 20}, {'Name': 'Rishita'}, 3000)
print(type(tup2))  # <class 'tuple'>


tup1 = (10,20,30,40,50,80,90)

print(tup1[-5:-1])  # (30, 40, 50, 80)
print(tup1[-1:-5])  # ()
print(tup1[-1:-5:-2])  # (90, 50)
print(tup1[-1:-5:-3])  # (90, 40)
print(tup1[-7:2:-3])  # ()
print(tup1[-3:5:2])  # (50,)
print(tup1[-3:3:2])  # ()

# STep -> 1. Skip points  2. Flow



tup1= (10,20,30)

print(id(tup1))   # 2796023493760
tup2 = (45, "Mansi")

tup1 += tup2
print(id(tup1))   # 2796022101104

print(tup1)
tup1= (10,20,30,7,2,1,90)
print(max(tup1))
print(min(tup1))

print(sorted(tup1))   # [1, 2, 7, 10, 20, 30, 90]

del tup1

# print(tup1)

'''
Tasks in tuple -: 

1. Python program to find the size of a tuple
-> tuple = ("python", "includehelp", 43, 54.23)

2. Python program for adding a Tuple to List and Vice-Versa
-> tuple = ("python", "includehelp", 43, 54.23)

3. Python program to find the maximum and minimum K elements in a tuple
-> 
Input: 
myTuple = (4, 2, 5,7, 1, 8, 9), k = 2

Output: 
(9, 8) , (1, 2)

4. Python program to create a list of tuples from given list having number and its cube in each tuple
->
Input: 
list = [4, 1, 6, 2]

Output: 
[(4, 64), (1, 1), (6, 216), (2, 8)]

5. Python program to remove all tuples of length K
-> 
Input:
[(1, 4), (2), (4,5,6,8), (26), (3, 0, 1), (4)] k = 1

Output:
[(1, 4), (4, 5, 6, 8), (3, 0, 1)]

6. Python program to extract digits from tuple list
->
Input: 
list = [(4, 62), (2, 65), (5, 9), (0,1)]

Output:
[4, 6, 2, 5, 9, 0, 1]

7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

8. Python program to join tuples if similar initial element
->
Input:
list = [(1, 4), (3, 1), (1, 2), (4, 2), (3, 5)]

Output:
list = [(1, 4, 2), (3, 1, 5), (4, 2)]

9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

11. Python program to sort tuples by frequency of their absolute difference
-> 
Input:
[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

Output:
[(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

Output:
[(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

14. Python program to concatenate maximum tuples
->
Input:
tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]

Output:
"python programming"

15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)
'''


n1,n2 = 0,1

print(n1,n2,end=' ')  # 0 1


for i in range(6):
    n3 = n1 + n2
    print(n3,end=' ')  # 0 1 1 2 3 5 8 13
    n1 = n2
    n2 = n3

print()
list1 = [10,290,32,65,32,2,1,78]

list1.sort()
print(list1[-2])

# -------------------------------------------------

tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3), ('Tanush', 7)]

list1 = []
for subtup in tupList:
    print(subtup)
    list1.append(subtup[1])

print(list1)
max1 = max(list1)

print(max1)   # 7

res = []
for i in tupList:
    if max1 in i:
        res.append(i[0])

str1 = '_'.join(res)
print(str1)   # python_programming_Tanush

# 13. Python program to order tuples by list
# ->
# Input:
# tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

# Output:
# [('l', 5), ('a', 1), ('k', 2), ('e', 6)]


tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
sortList = ['l', 'a', 'k', 'e']

ans = []

for i in sortList:    #  i = 'l'
    for j in range(len(tupList)):   # 0,1,2,3   # j = 0
        if i == tupList[j][0]:   # 'l' == 'l'
            ans.append(tupList[j])
            break

print(ans)   # [('l', 5), ('a', 1), ('k', 2), ('e', 6)]
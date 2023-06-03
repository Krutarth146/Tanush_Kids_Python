list1 = [23,90,89,78,67,56]

# [(23,23), (23,90), (23,89)......]

for i in list1:   # i = 23
    for j in list1:  # j = 90
        print((i,j),end=' ')   # (23,23), (23,90)


l1 = [10,20,30,40,50]

max1= max(l1)
print(max1)   # 50

l2 = []
for i in l1:
    if i != max1:
        l2.append(i)
l2.sort()
print(l2[-1])  # 40


# l3 = [90,2,765,21,68,45,34,10,20,10,2]

# # Maximum, minimum = (?)
# k = int(input())


# l3.sort()

# res = []

# for i in l3:
#     if i not in res:
#         res.append(i)
# print(res)
# for i in range(k):
#     print("Minimum Num: ",res[i])

# for j in range(len(res) - k, len(res)):
#     print('Maximum Numbers:',res[j])

# for j in range(len(res)-1, (len(res) - k)-1, -1):
#     print('Maximum Numbers:',res[j])

list1 = [10,20,30,40,50]


# ans = [(10,10), (10,20), (10,30) .....]
combinations= []
for c in list1:
    for h in list1:
        combinations.append((c,h))

print(combinations)   # [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50)]


list1 =  [[10, 20, 30], 
          [44,  2, 77], 
          [55, 13, 21], 
        ]

print(list1[2][2])   # 21
print(list1[-2][-2])   # 21
sum = 0
for x in list1:   # x = [10, 20, 30]
    for d in x:
        print(d,end=' ')
        sum += d
    print()

print(sum)   # 272


# Task: 
# Diagonal Sum


'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''


list1 = [10,20,30,80,{"Address" : {"State" : "Gujarat", 'country' : "India", "Area" : {"Main" : "Gnr", "sub" : "Sarghasan", 'Pincode' : [380001, 90000, 80000]}}}]

# 90000

print(len(list1))  # 5

print(list1[-1]["Address"]["Area"]['Pincode'][1])  # 90000



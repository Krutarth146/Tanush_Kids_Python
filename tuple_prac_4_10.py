tup1 = (10,20,30,40,10,10,20)

# set ------> Don't Allow Duplicates, Unordered


# tup1 = tuple(set(tup1))
# print(tup1)   # (40, 10, 20, 30)


tup1 = list(tup1)

new = []

# for i in tup1:
#     if i not in new:
#         new.append(i)
# print(tuple(new))


# for i in tup1:
#     if tup1.count(i) == 1:
#         new.append(i)
# print(tuple(new))


# print(tup1)  # [10, 20, 30, 40, 10, 10, 20]

list1 = [10,20,30,40,50,10,10,10,10]

for k in list1:
    count1 = list1.count(k)
    if count1 > 1:
        for d in range(count1-1):
            list1.remove(k)

print(list1)   # [20, 30, 40, 50]


tup1 = (20,90,34,1,5)

# [(1,2,4,5,10,20),(),(1,5) ....]

# ------------------------------------------------------------------------
# Date - 6/10/23

tup1 = ((10,20), (333,9), (34,), (34,90,233), (45,90), (22,900))
k = 2

ans = ((10,20) , (34,) , (45,90))

list1 = []
for subtup in tup1:
    if len([k for k in subtup if len(str(k)) == 2]) == len(subtup):
        list1.append(subtup)

print(tuple(list1))   # ((10, 20), (34,), (45, 90))


# Sort by last Element of Subtuples

# print(sorted(tup1))   # [(10, 20), (22, 900), (34,), (34, 90, 233), (45, 90), (333, 9)]
tup1 = ((10,20), (333,9), (34,3), (34,90,233), (45,90), (22,900))
# ans =  [(34,3), (333,9), (10,20), (45,90), (34,90,233), (22,900)]
tup1 = list(tup1)

for j in range(len(tup1)):
    for k in range(j+1,len(tup1)):
        if tup1[j][-1] > tup1[k][-1]:
            tup1[j],tup1[k] = tup1[k],tup1[j]

print(tup1)   # [(34, 3), (333, 9), (10, 20), (45, 90), (34, 90, 233), (22, 900)]
tup1 = ()
print(type(tup1))   # Tuple

tup2 = (10)
print(type(tup2))   # int

tup3 = (20,)  
print(type(tup3))   # tuple


# Tuple ----> Immutable, Ordered (Indexed), Allow's Duplicates

tup1 = (10,10,101,10,[(10,20,30), ((), (199, [23,885, {'Name' : [11, ]}]))])


print(tup1[-1])   # [(10, 20, 30), ((), (199, [23, 885, {'Name': [11]}]))]
print(tup1[-1][1])   # ((), (199, [23, 885, {'Name': [11]}]))
print(tup1[-1][-1])   # ((), (199, [23, 885, {'Name': [11]}]))
print(tup1[-1][-1])   # ((), (199, [23, 885, {'Name': [11]}]))
print(tup1[-1][-1][1])   # (199, [23, 885, {'Name': [11]}])
print(tup1[-1][-1][1][-1])   # (199, [23, 885, {'Name': [11]}])
print(tup1[-1][-1][1][-1][-1])   # (199, [23, 885, {'Name': [11]}])
print(tup1[-1][-1][1][-1][-1]['Name'])   # [11]  # List
print(tup1[-1][-1][1][-1][-1]['Name'][0])   # 11   # int

tup1 = [(), (10,20,10), (90,34,22,21)]

print(tup1 * 3)   # [50, 50, 50]


# [10,20,10,90,34....]


new1=  []
for subtup in tup1:
    for k in subtup:
        new1.append(k)

print(new1)   # [10, 20, 10, 90, 34, 22, 21]



new1 = tuple(new1)
print(new1)

print(new1[2:5])   # (10, 90, 34)
print(new1[-1:3])   # ()
print(new1[-1:3:-2])   # (21, 34)
print(type(new1[3:-3:1]))   # Tuple

print(new1[::-1])  # (21, 22, 34, 90, 10, 20, 10)
   
print(new1[3:-3:1])   # (90,)  # tuple

for j in range(3,-3,-1):
    print(j)   # blank
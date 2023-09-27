str1 = "Tanush is good Boy123."

# String -----> Immutable, Ordered (Indexed)

# Indexing

print(str1[2])   # n
print(str1[-2])   # 3

# Slicing

print(str1[-1:-5])   # blank
print(str1[-5:-1])   # y123
print(str1[4:8])     # sh i

str1 = "Tanush is good Boy123."
print(str1[5:-5])   # h is good Bo
print(str1[-1:-5])   # 
print(str1[3:-5])   # ush is good Bo
print(str1[3:-5:2])   # uhi odB
print(str1[3:-5:-1])   # 
print(str1[::-1])   # .321yoB doog si hsunaT

str2 = "Tanush"
print(str2[2:-3:-1])   # blank


str1 = 'Tanush_is Good'

print(str1.capitalize())   # Tanush_is good
print(str1.title())   # Tanush_Is Good
print(str1.lower())   # tanush_is good
print(str1.upper())   # TANUSH_IS GOOD
print(str1.swapcase())   # tANUSH_IS gOOD
print(str1.casefold())   # tanush_is good


ans = 'a lion is the king of a Jungle'

str1 = 'the lion_is_the king of the Jungle'
list1 = str1.split('_')
print(list1)   # ['the lion', 'is', 'the king of the Jungle']
list1 = str1.split(' ',2)
print(list1)   # ['the', 'lion_is_the', 'king of the Jungle']


print(str1.split('t'))   # ['', 'he lion_is_', 'he king of ', 'he Jungle']

print(str1.partition(' '))   # ('the', ' ', 'lion_is_the king of the Jungle')
print(str1.partition('t'))   # ('', 't', 'he lion_is_the king of the Jungle')
print(str1.rpartition('t'))   # ('the lion_is_the king of ', 't', 'he Jungle')

print(str1.replace('the','a'))   # a lion_is_a king of a Jungle
print(str1.replace('the','a',1))   # a lion_is_a king of a Jungle


str3 = 'Hello Sam'
table = str3.maketrans('S', 'R')
print(table)   # {83: 82}

print(str3.translate(table))   # Hello Ram


str3 = 'Hello Tanush'
print(len(str3))   # 12
print(str3.ljust(15,'*'))   # Hello Tanush***
print(str3.rjust(15,'*'))   # ***Hello Tanush
str3 = '           Hello Tanush             '
print(str3.strip())   # Hello Tanush
print(str3.lstrip())   # Hello Tanush
print(str3.rstrip())   #            Hello Tanush


str1 = 'the lion_is_the king of the Jungle'

list1 = str1.replace('the','a',1).split(' ')
print(list1)   # ['a', 'lion_is_the', 'king', 'of', 'the', 'Jungle']

# for i in reversed(list1):
for i in range(len(list1)-1,-1,-1):
    if list1[i]=='the':
        list1[i] = 'a'
        break

print(list1)   # ['a', 'lion_is_the', 'king', 'of', 'a', 'Jungle']

print(' '.join(list1))   # a lion_is_the king of a Jungle


str2 = '901'

print(str2.zfill(5))   # 00901


# print(str2.is)
   
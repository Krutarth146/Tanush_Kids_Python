# while Loop

# start, End(Condition), Step

tanush = 25

while tanush <= 30:
    print(tanush,end=' ')
    tanush+=1  # tanush = tanush + 1

print(tanush)   # 31


# --------------------------

jk = 89

while jk>=80:
    print(jk,end=' ')
    jk-=2

# 

# 3 
# 33
print()
num = 3

xerox = num
sum = 0
step = 1
while step <= 10:
    print(num)
    sum += num
    num = num * 10 + xerox   # 33 = 3 * 10 + 3
    step+=1
print("Sum = ",sum)  
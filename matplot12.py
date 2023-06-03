from matplotlib import pyplot as plt

# x = [10, 20 ,30 ,40, 50]
# y = [1, 9 , 3 , 5, 4]

# plt.plot(x,y)
# plt.show()

# x = range(1,11)
# y = range(5,15)

# plt.plot(x,y)
# plt.show()

# plt.axis([-20, 50, 0, 50])
# plt.plot(x,y)
# plt.show()

# plt.bar(x,y)
# plt.show()


# x = [10, 90, 20, 60, 40 , 33]
# y = [1,2,3,4,5,6]

# plt.hist(x)
# plt.show()

# plt.scatter(x,y)
# plt.show()


# --------------------------------------------------------

# import numpy as np

cars = ['Audi', 'BMW', 'Ford', 'Tesla', 'Jaguar', 'Mercedes']
data = [23, 17, 35, 29 ,12, 41]

# fig = plt.figure(figsize=(10,7))
# plt.pie(data, labels=cars)
# plt.show()

# ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# plt.show()


# '.' -> pointer Marker
# 'o' -> Circle Marker
# '+' -> Plus Marker
# 's' -> square Marker
# 'D'-> Diamond Marker
# 'H' -> Hexagon Marker


x = [-2 , -1.5, -1, -0.5,  0, 0.5, 1, 1.5, 2]
y = [-4,-3,-2,-1,0,1,2,3,4]
s = [-4,-3,-2,-1,0,1,2,3,4]

ax1 = plt.plot(x, s, 'bD:')   # b - blue, D - diamond, - Dashhed Line
# 
plt.legend(labels=("Population Line"), loc="upper left")
plt.suptitle("Decoration Graph")
plt.show()
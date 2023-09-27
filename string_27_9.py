str1 = "Tanush is Good Boy123."

print(len(str1))   # 22
print(str1.center(30,'*'))

print(str1.count('o'))   # 3
print(str1.count('o',13,15))   # 0
print(str1.count('o',13))   # 1

print(str1.endswith('3.'))   # True
print(str1.startswith('t'))  # False


str2 = "Ståle"
print(str2.encode())   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors="backslashreplace"))   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors="replace"))   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors="namereplace"))   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors="ignore"))   # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors="xmlcharrefreplace"))   # b'St\xc3\xa5le'


# Hello
# waggr


str1 = 'Aman has\t3 Ruppes' 
print(str1.expandtabs(24))  # Aman has                3 Ruppes

print(str1.find('f'))  # -1
# print(str1.index('f'))  # Error

name = 'Tanush'
rupees = 900

print('{} has {} Ruppes only.'.format(name, rupees))   # Tanush has 900 Ruppes only.
print('{1} has {0} Ruppes only.'.format(name, rupees))   # 900 has Tanush Ruppes only.
print('{name} has {rupees} Ruppes only.'.format(name = 'Aman', rupees = 897))   # Aman has 897 Ruppes only.

dict1 = {'name' : "Tanush", 'Roll' : 900}

print('{name} has {Roll} Ruppes only.'.format_map(dict1))   # Tanush has 900 Ruppes only.

str1 = 'aman_90'
print(str1.isidentifier())


print(str1.removeprefix('am'))   # an_90

str1 = 'Tanush\nAgarwal\nAman\nPatel'
print(str1)
print(str1.splitlines())   # ['Tanush', 'Agarwal', 'Aman', 'Patel']


# ---------- String Methods Finished ----------------
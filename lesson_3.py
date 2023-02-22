#start : Data type
''' Numeric Data Type'''
# integer variable.
a=99
print("the type",a, " is ", type(a))
# float variable.
b=20.45
print("the type", b, " is ", type(b))
# complex variable.
c=2+3j
print("the type", c, " is ", type(c))

print(1 + 2.0)
print(1 - 2.0)
print(1 * 2.0)
print(1 / 2.0)


def datetype ():
    a = int(2.3)
    b = int(-2.8)
    c = float(5)
    d = complex('3+5j')
    print(a)
    print(b)
    print(c)
    print(d)
datetype()
'''String Data Type'''
str ="Hom nay la thu bay"
print(str)  # in full chuoi
print(str[0]) # in ky tu dau tien
print(str[str.__len__() -1]) # in ky tu cuoi cung
print(str[2:5]*3) #ky tu tu 2 den 5 in ra 3 lan

list = ['monday', 3, "thu tu", "thurday"]
tinylist = [6, 'thu bay']
print(tinylist[1])


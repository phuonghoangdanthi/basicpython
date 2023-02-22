# 1. Boolean
'''x= True
y= True
print (x==y)
print(3<5 or 10>20)
print(3<5 and 10>20)'''
# 2. If
'''dtb = float (input("Nhap diem trung binh:"))
if dtb >= 5:
    print("Ban dau roi")
    print("Chuc mung ban")'''
 
# 3 If... else
'''dtb = float(input("Nhap diem trung binh:"))
if dtb>=5:
    print("Ban dau roi")
    print("Chuc mung ban")
else:
    print("Ban rot goi")
    print('thi lai roi')'''
#4 If...elif long nhau
'''dtb = float(input("Nhap diem trung binh:"))
if dtb >=9:
    print("Ban xep loai gioi")
elif dtb >=7:
    print("Ban xep loai kha")
elif dtb >=5:
    print("Ban xep loai trung binh")
else: 
    print("ban xep loai yeu")'''

#5 Pass
'''a= int(input("Nhap he so a:"))
b= int(input("Nhap he so b:"))
if a==0:
    pass # giữ khoảng code cho lần sau
else:
    x=-b/a
    print("No x=", -b/a)
'''
#6 So sanh so thuc
'''d1=1.11-1.10
d2 =2.11-2.10
print("d1",d1)
print("d2",d2)
diff =d1-d2
if diff<0:
    diff=-diff
if diff <0.000001:
    print("d1=d2")
else:
    print("d1 khac d2")'''

#7 Su dung if else nhu phep gan
'''a=5
b=7
if a!=b:
    c=113
else:
    c=115
print("c =",c)
c=113 if a!=b else 115
print(c)'''
    # check chan le
x = int(input("Nhap so x:"))
print("chan" if x%2 ==0 else "le")

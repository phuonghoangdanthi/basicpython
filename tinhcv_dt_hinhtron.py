# Cho ban kinh r. tinh chu vi, dien tich hinh tron
# cv=2pi*r S= pi*r^2
import math
try:
    r= float(input("Moi ban nhap ban kinh:"))
    cv=2*math.pi*r
    S= r**2*math.pi
    print("Chu vi:", cv)
    print("Dien tich", S)
except:
    print("Loi roi")


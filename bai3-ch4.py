# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:22:36 2024

@author: NguyenTruongDuy
"""

print("giải phương trình bậc nhất ax + b")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a==0 and b!=0:
    print("Phương trình vô nghiệm.")
elif a==0 and b==0:
    print("phương trình có vô số nghiệm.")
else:
    print("nghiệm của phương trình: ", -b/a)
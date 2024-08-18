# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:26:02 2024

@author: NguyenTruongDuy
"""

print("Nhập 3 kích thước xem có phải tam giác không?")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Đây là tam giác đều.")
    elif a==b or a==c or b==c:
        print("Đây là tam giác cân.")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        print("Đây là tam giác vuông.")
        if a==b or a==c or b==c:
            print("Đây là tam giác vuông cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("a,b,c không là 3 cạnh của một tam giác.")
    
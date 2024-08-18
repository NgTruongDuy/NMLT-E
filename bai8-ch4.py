# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:37:22 2024

@author: NguyenTruongDuy
"""

import random 

kbb = ["kéo", "búa", "bao"]
p = input("Người chơi chọn: ")
if p not in ["kéo", "búa", "bao"]:
    print("Không hợp lệ, xin vui lòng nhập lại.")
b = random.choice(kbb)
print("Máy chọn: ",b)

if p==b:
    print("Hòa ròi.")
elif  (p=="kéo" and b=="bao") and (p=="bao" and b=="búa") and (p=="búa" and b=="kéo"):
         print("Bạn thắng ròi!")
else:
    print("Bạn thua ròi.")
    
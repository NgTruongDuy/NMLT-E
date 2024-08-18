# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:09:40 2024

@author: NguyenTruongDuy
"""

gpa = float(input("nhập điểm trung bình (GPA): "))

if gpa < 3.5:
    print("Học lực kém.")
elif gpa >= 3.5 and gpa < 5.0:
    print("Học lực yếu.")
elif gpa >= 5.0 and gpa < 7.0:
    print("Học lực trung bình.")
elif gpa >= 7.0 and gpa < 8.0:
    print("Học lực khá.")
elif gpa >= 8.0 and gpa < 9.0:
    print("Học lực giỏi.")
elif gpa >= 9.0 and gpa <= 10.0:
    print("Học lực xuất sắc.")
else:
    print("Vui lòng nhập lại!")

    
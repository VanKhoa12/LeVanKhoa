# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:01:11 2024

@author: Dell
"""

from math import sqrt

a = float(input("Nhap gia tri cua a: "))
b = float(input("Nhap gia tri cua b: "))
c = float(input("Nhap gia tri cua c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        if c == 0:
            print("Phuong trinh co 1 nghiem x = 0")
        else:
            print("Phuong trinh co 1 nghiem x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phuong trinh vo nghiem.")
    elif delta == 0:
        print("Phuong trinh co 1 nghiem x = ", -b / (2 * a))
    else:
        print("Phuong trinh co 2 nghiem phan biet.")
        print("x1 = ", float((-b + sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b - sqrt(delta)) / (2 * a)))
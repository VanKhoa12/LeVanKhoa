# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:31:39 2024

@author: Dell
"""

a = float(input("So km quang duong di duoc: "))
if a == 1:
    print("Tien taxi theo so km quang duong di duoc: ",20,"k")
elif a <= 3:
    print("Tien taxi theo so km quang duong di duoc: ", a*13,"k")
elif a <= 8:
    print("Tien taxi theo so km quang duong di duoc: ", 3*13+(a-3)*12,"k")
else:
    b = 3*13+5*12+(a-8)*10
    if b <= 100: 
        print("Tien taxi theo so km quang duong di duoc: ", b,"k")
    else:
        print("Tin taxi theo so km quang duong di duoc: ", b*0.92,"k")
        
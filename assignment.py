import numpy as np

L1 = float(54)
L2 = float(61)

teta1 = np.deg2rad(float(input("masukan sudut derajat rotasi lengan pertama")))
teta2 = np.deg2rad(float(input("masukan sudut derajatrotasi lengan kedua")))
teta3 = np.deg2rad(float(input("masukan sudut derajat lengan ketiga")))

x1= np.cos(teta1) * L1 * np.cos(teta2)
y1= np.sin(teta2) * L1 * np.sin(teta2)
z1 = L1 * np.sin(teta2)

x2 = x1 + L2 * np.cos(teta1 + teta3)
y2 = y1 + L2 * np.sin(teta1 + teta3)
z2 = z1 + L2 * np.sin(teta1 + teta2)

print(f"x = {x2:.2f}")
print(f"y = {y2:.2f}")
print(f"z = {z2:.2f}")







import matplotlib.pyplot as plt
import statistics
import os
import numpy as np

nilai = ()
x =[]
y =[]
na1_sa9 = []
for i in range(9):
    os.system('cls')
    print('data ke -'+str(i+1))
    nilai = int(input("Masukkan nilai absen 1 - 9 : "))
    na1_sa9.append(nilai)  
na10_sa19 = []
for i in range(9):
    os.system('cls')
    print('data ke -'+str(i+1))
    nilai = int(input("Masukkan nilai absen 10 - 19 : "))
    na10_sa19.append(nilai)
na20_sa29 = []
for i in range(9):
    os.system('cls')
    print('data ke -'+str(i+1))
    nilai = int(input("Masukkan nilai absen 20 - 29 : "))
    na20_sa29.append(nilai)
na30_sa39 = []
for i in range(9):
    os.system('cls')
    print('data ke -'+str(i+1))
    nilai = int(input("Masukkan nilai absen 30 - 39 : "))
    na30_sa39.append(nilai)
nilaiA = np.array([[na1_sa9],[na10_sa19],[na20_sa29],[na30_sa39]])
resnilaiA = nilaiA.reshape(4,9)
mean_ = sum(nilaiA[0:3])/len(nilaiA[0:3])
x = [na1_sa9,na10_sa19]
y = [na20_sa29,na30_sa39]
plt.plot(x,y)
plt.show()
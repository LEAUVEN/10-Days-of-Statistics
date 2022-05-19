import math
import os
import random
import re
import sys

size=int(input())
numbers_1 = list(map(int, input().split())) # sayilarimizi liste haline getirdi.
numbers_2 = list(map(int, input().split())) # sayilarimizi liste haline getirdi.
carpim=[numbers_1[i]*numbers_2[i] for i in range(len(numbers_2))] # listelerimizi çarpıp yeni bir listeye eleman olarak ekledik
carpim_toplam=sum(carpim) # Pay kısmını toplayarak bulduk
toplam=sum(numbers_2) # Payda kısmını hesapladık
son_hali=carpim_toplam/toplam # İşlemimizi yaptık
son_hali_1=round(son_hali,1) # Yuvarladık.
print(son_hali_1) # Yazdırdık
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:00:08 2024

@author: serkan
"""

#16.10.2024 vücut kitle endeksi alıştırması

kilo = float(input("Kilonuzu Giriniz(kg)"))
boy = float(input("boyunuzu Girin(cm)"))
boy_metre = boy / 100
boyunkaresi = boy_metre * boy_metre
print("Kilonuz",kilo)
print("boyunuzun karesi ",boyunkaresi,)
bmi= kilo / boyunkaresi
print(" Kitle Endeksiniz",bmi,)
if bmi < 18.5:
    print("Durum: Zayıf")
elif 18.5 <= bmi < 24.9:  # Bu satırda düzeltme yapıldı
    print("Durum: Normalsiniz")
elif 25 <= bmi < 29.9:
    print("Durum: Kilolu")
else:
    print("Durum: Obez") 

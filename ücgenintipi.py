# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:55:48 2024

@author: serkan
"""

#16.10.2024 üçgenin tipini belirleme alıştırması 

kenar1 = int(input("Birinci Kenarı Girin"))
kenar2 = int(input("İkinci Kenarı Girin:"))
kenar3 = int(input("Üçüncü Kenarı Girin:"))

if kenar1 == kenar2 == kenar3:
    print("Bu Üçgen Eşkenar Üçgendir")
elif kenar1 == kenar2 or kenar1 == kenar2 == kenar3: 
    print("Bu Üçgen İkizkenar Üçgen")
else: 
    print("Bu Üçgen Çeşitkenar Üçgen")
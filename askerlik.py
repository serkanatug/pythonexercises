# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:46:41 2024

@author: serkan
"""
 
cinsiyet= input("cinsiyetinii girin [e/k]")
yas= int(input("kaç yaşndasınız"))
if (cinsiyet == "k"):
    print("Kadınlar Askere Gitmeybilir")
elif(cinsiyet== "e" and yas>=20):
    print("Asker Olabilir")
elif(cinsiyet == "e" and yas<20):
    print("Askerlik Yaşında Değilsin")


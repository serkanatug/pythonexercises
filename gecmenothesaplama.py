# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:57:32 2024

@author: serkan
"""


    
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:57:32 2024

@author: serkan
"""
#15.10.24 4. hafta geçme notu hesaplama
vizenot = float(input("Vize notunuzu girin: "))
finalnot = float(input("Final notunuzu girin: "))

gecmenotu = (vizenot * 0.40) + (finalnot * 0.60)

print("Geçme Notu:", gecmenotu)

if gecmenotu > 90:
    print("AA / Mükemmel")
elif gecmenotu >= 85:
    print("BA / Pekiyi")
elif gecmenotu >= 75:
    print("BB / İyi")
elif gecmenotu >= 70:
    print("CB / Orta")
elif gecmenotu >= 60:
    print("CC / Geçer")
elif gecmenotu >= 50:
    print("DC / Şartlı Geçer")
elif gecmenotu >= 40:
    print("DD / Başarısız")
elif gecmenotu >= 30:
    print("FD / Başarısız")
else:
    print("FF / Başarısız")
    
if gecmenotu>60:
    print("Geçtiniz")
else:
    print("Kaldınız")






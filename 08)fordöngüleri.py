******* FOR *******


# listedeki elemanları yazdırma:
liste = [1,2,3,4,5]
 
for eleman in liste:
    print("Eleman",eleman)
 
"""
Çıktı
Eleman 1
Eleman 2
Eleman 3
Eleman 4
Eleman 5
"""
    
    
# Liste elemanlarını toplama
liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)
 
"""
Çıktı
Toplam 28
"""
    
    
# Çift elemanları bastırma
liste = [1,2,3,4,5,6,7,8,9]
 
for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)
 
"""
Çıktı
2
4
6
8
"""


# Her bir karakteri 3 ile çarpma
s = "Python"
 
for karakter in s:
    print(karakter * 3)
 
"""
Çıktı
PPP
yyy
ttt
hhh
ooo
nnn
"""


# Listelerin için 2 boyutlu demetler
liste = [(1,2),(3,4),(5,6),(7,8)]
 
for eleman in liste:
    print(eleman) # Her bir elemanın demet olduğu görebiliyoruz.
 
"""
Çıktı
(1, 2)
(3, 4)
(5, 6)
(7, 8)
"""


# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]
 
for (i,j) in liste:
    print(i,j)
 
"""
Çıktı
1 2
3 4
5 6
7 8
"""


# Demet içindeki elemanları çarpalım.
liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print(i * j * k)
 
"""
Çıktı
6
120
504
1320 
"""


# Sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
 
for eleman in sözlük:
    print(eleman)
 
"""
Çıktı
bir
iki
üç
dört
"""


# keys() - Aynı şey
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
 
for eleman in sözlük.keys():
    print(eleman)
 
"""
Çıktı 
bir
iki
üç
dört 
"""


# values() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
 
for eleman in sözlük.values():
    print(eleman)
 
"""
Çıktı
1
2
3
4
"""

# items() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
 
for (i,j) in sözlük.items():
    print("Anahtar:",i,"Değer:",j)
 
"""
Çıktı
Anahtar: bir Değer: 1
Anahtar: iki Değer: 2
Anahtar: üç Değer: 3
Anahtar: dört Değer: 4
"""


# yıldızlarla üçgen oluşturma
for b in range(10):
    print("*"*b)
    
"""
çıktı
*
**
***
****
*****
******
*******
********
*********
"""

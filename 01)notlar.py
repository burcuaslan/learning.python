
"""
#   --> not satırı, bu satırı okumaz
\   --> sonrakini görmez
\n  --> alt satıra geçer
\t  --> 4 tane boşluk bırakır
//  --> tamsayı bölmesi
%   --> kalan bulma
**  --> üs bulma
-   --> işaret değiştirme
"""



# SEP PARAMETRESİ
#print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar.
#Eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan olarak boşluk yerleştirilir.

print(3,4,5,6,7,8,9,sep = ".")
print("06","04","2015",sep = "/")

"""
çıktı
3.4.5.6.7.8.9
06/04/2015
"""


#YILDIZLI PARAMETRELER
#Eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek
#bu string karakterlerine ayrılacak ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır.

# Varsayılan olarak karakterlerin arasına boşluk konuluyor.
print(*"Python")
print(*"Python",sep = "\n")
print(*"TBMM",sep =".")
 
"""
Çıktı
P y t h o n
P
y
t
h
o
n
T.B.M.M 
"""

#SÖZLÜKLER

a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
 
print(a)
print(a["iki"])
print(a["iki"][1][1])
print(a["üç"])
a["üç"] += 5
print(a["üç"])
print(a)
 
"""
Çıktı
[[1, 2], [3, 4], [5, 6]]
4
15
20
{'bir': [1, 2, 3, 4], 'iki': [[1, 2], [3, 4], [5, 6]], 'üç': 20}
"""


yeni_sözlük = {"bir":1,"iki":2,"üç":3}
 
# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sözlük.values())
 
# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sözlük.keys())
 
# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
print(yeni_sözlük.items())
 
"""
Çıktı
dict_values([1, 2, 3])
dict_keys(['bir', 'iki', 'üç'])
dict_items([('bir', 1), ('iki', 2), ('üç', 3)])
"""

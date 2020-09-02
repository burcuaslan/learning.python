# Liste değişkeni. Değişik veri tiplerinden değerleri saklayabiliyoruz.
liste =  [3,4,5,6,"Elma",3.14,5.324]
print(liste)

"""
Çıktı
[3, 4, 5, 6, 'Elma', 3.14, 5.324]
"""


# Boş liste
boş_liste = []
print(boş_liste)
 
"""
Çıktı
[]
"""


# Boş liste, list() fonksiyonuyla da oluşturulabilir.
boş_liste = list()
print(boş_liste)

"""
Çıktı
[]
"""


# len fonksiyonu listeler üzerinde de kullanılabilir.
liste3 = [3,4,5,6,6,7,8,9,0,0,0]
print(len(liste3))

"""
Çıktı
11
"""


# Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.
s =  "Merhaba"
lst =  list(s)
print(lst)
 
"""
Çıktı
['M', 'e', 'r', 'h', 'a', 'b', 'a']
"""


# Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.

liste = [3,4,5,6,7,8,9,10]
print(liste)
 
# 0. eleman 
print(liste[0])
 
# 4. eleman 
print(liste[4])
 
# Sonuncu Eleman
print(liste[len(liste)-1])
 
# Baştan 4. indekse kadar (dahil değil)
print(liste[:4])

# 1.indeksten 5.indekse kadar
print(liste[1:5])
 
print(liste[5:])
 
print(liste[::2])
 
print(liste[::-1])
 
"""
Çıktı
[3, 4, 5, 6, 7, 8, 9, 10]
3
7
10
[3, 4, 5, 6]
[4, 5, 6, 7]
[8, 9, 10]
[3, 5, 7, 9]
[10, 9, 8, 7, 6, 5, 4, 3]
"""

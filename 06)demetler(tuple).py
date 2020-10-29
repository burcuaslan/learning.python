# Demetler veya İngilizce ismiyle tuplelar listelere oldukça benzer ancak farkları demetlerin değiştirilemez oluşudur.
# Bu yüzden programlarımızda değiştirilmesini istemediğimiz değerleri bir demet içinde depolayabiliriz.


# Demet elemanları parantez içine alınarak demet oluşturulabilir.
demet = (1,2,3,4,5,6,7,8,9)
print(demet)
print(type(demet))
 
"""
Çıktı 
(1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple
"""


demet = (1,2,3,4,5,6,7)

# 0. indekse  ulaşma
print(demet[0])
# 4. indekse ulaşma
print(demet[4])
print(demet[-1])
print(demet[2:])

""" 
Çıktı
1
5
7
(3, 4, 5, 6, 7)
"""


# index metoduyla içine verdiğimiz elemanın hangi indekste olduğunu bulabiliriz.
demet = (1,2,3,"Mustafa","Murat","Coşkun")
# "Mustafa" elemanının indeksini buluyoruz.
print(demet.index("Mustafa"))
 
"""
Çıktı
3
"""


# count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.
demet = (1,23,34,34,2,1,4,5,1,1,34)
print(demet.count(1))
 
"""
Çıktı
4
"""


"""
Demetleri Ne Zaman Kullanalım ?
Aslında Python programcıları demetlerden ziyade listeleri daha çok kullanır.
Ancak eğer programınızda değiştirilmesini istemediğiniz bilgiler varsa 
(Android uygulama sabitleri gibi) bunları demet içinde depolayabilirsiniz. 
Aynı zamanda, Read Only(Sadece Okuma) bir veritipi olduğu için listelere göre biraz daha hızlı çalışırlar.
"""

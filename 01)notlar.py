
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

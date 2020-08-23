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



****  String Oluşturma  ****
# Tek tırnak ile 
In [1]: 'Mustafa Murat Coşkun'
Out[1]: 'Mustafa Murat Coşkun'

# Çift Tırnak ile 
In [2]: "Mustafa Murat Coşkun"
Out[2]: 'Mustafa Murat Coşkun'

# 3 tırnak ile
In [3]: """Mustafa Murat Coşkun"""
Out[3]: 'Mustafa Murat Coşkun'




****  Veri tipi Dönüşümleri  ****
# Çevireceğimiz sayıyı parantez içine alıyoruz

a = 43
float(a)
43.0

int(4.7)
4

a = 32324324
b = str(a)
b
'32324324'

len(b)

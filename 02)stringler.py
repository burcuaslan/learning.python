****  STRİNGLER  ****

# Tek tırnak ile 
In [1]: 'Mustafa Murat Coşkun'
Out[1]: 'Mustafa Murat Coşkun'

# Çift Tırnak ile 
In [2]: "Mustafa Murat Coşkun"
Out[2]: 'Mustafa Murat Coşkun'

# 3 tırnak ile
In [3]: """Mustafa Murat Coşkun"""
Out[3]: 'Mustafa Murat Coşkun'
  
  
# Stringin 0. elemana  ulaşalım. Bunun için [] operatörünü kullanacağız.
a = "ali"
a[0]  --> a

# 1.eleman
a[1]  -->l

# 2.eleman
a[2]  -->i

# Sondaki eleman "-1" eleman
a[-1] -->i

#stringin uzunluğunu hesaplama
len(a) -->3


Peki uzun bir string'in sadece belirli bir kısmını elde etmek için ne yapacağız ? Bunun için indeksleri, : ve [] işaretini kullanacağız. Formülümüz şu şekilde ;
[başlama indeksi : bitiş indeksi : atlama değeri]

a = "Python Programlama Dili"

# 4. indeksten başla 10.indekse kadar(dahil değil) al.
In [25]:  a[4:10]
Out[25]: 'on Pro'
  
# Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
In [26]:  a[:10]
Out[26]: 'Python Pro'
  
# Bitiş değeri belirtilmemişse en sonuna kadar alır.
In [28]:  a[4:]
Out[28]: 'on Programlama Dili'
  
# İki değer de belirtilmemişse tüm stringi al.
In [29]:  a[:]
Out[29]: 'Python Programlama Dili'
  
#Son karaktere kadar al.
In [30]:  a[:-1]
Out[30]: 'Python Programlama Dil'
  
# Baştan sona 2 değer atlaya atlaya stringi al.
In [32]:  a[::2]
Out[32]: 'Pto rgalm ii'

# 4.indeksten 12'nci indekse 3'er atlayarak stringi al.
In [33]: a[4:12:3]
Out[33]: 'oPg'
  
# Baştan sona -1 atlayarak stringi al. (String'i ters çevirme)
In [34]: a[::-1]
Out[34]: 'iliD amalmargorP nohtyP'

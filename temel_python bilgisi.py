##### Veri Tiplerine Örnekler ####
5 ### integer veri tipi - tam sa
5.3 ### float veri tipi
"fatih" ### string veri tipi


######değişken örnekler#######
a=5
b=10
c="fatih"
d="2"
e=2.5

print(a+b) ## sonuc 15 olarak dönecektir
print(a*b) ## sonuc 50 olarak dönecektir
print(a*2+3) ## burada önce a'nın değeri ile 2 çarpılıp 3 ile toplanır. Sonuç 13 olarak dönecektir
print(c) ## sonuç fatih olarak dönecektir
print(d*2) ## sonuç 22 olarak dönecektir. Çünkü d değişkeninin değeri stringdir
print(e*2) ##sonuç 5.0 olarak dönecektir.
print(8/3) ## sonuç 2.6666666 float değer dönecektir
print(8//3) ## sonuç 2 integer dönecektir. Buradaki "//" işareti taban bölme işlemi yapar
##############################################
# Yazdığımızı Değişkenin Hangi veri tipinde olduğunu öğrenmek için type() fonksiyonunu kullanabiliriz
print(type(a)) ## sonuç <class 'int'> olarak dönecektir. Yukarıda a değişkenine integer değer vermiştik
print(type(c)) ## sonuç <class 'str'> olarak dönecektir. Yukarıda c değişkenine string değer vermiştik
print(type(e)) ## sonuç <class 'float'> olarak dönecektir. Yukarıda e değişkenine float değer vermiştik
##############################################
## string değerleri çift tırnaklar veya tek tırnaklar içinde gösterebilirsiniz
strings="fatih"
strings='fatih'  
print(strings) ## sonuç fatih dönecektir.
## fakat aşağıdaki gibi kullanımda
strings="mustafa"
print(strings) ## sonuç mustafa dönecektir. Çünkü yukarıda fatih verdiğimiz değeri mustafa olarak değiştirmiş olduk
## string ifadelerinde çoklu satır kullanımı için
strings="""
Burada 
çoklu satır
kullanımı
gösterilmiştir
"""
print(strings) 
## sonuç alt alta yazılmış şekilde dönecektir
##############################################
## Veri Tipi Dönüşümleri ##
a=5
b=3.5
metin="10"

## şimdiye kadar öğrendiklerimize göre
print(a*metin) ## sonuç olarak 50 beklemekteyiz. Fakat burada metin değişkeninin değeri string olduğu için sonuç 1010101010 olarak dönecektir
print(a*int(metin)) ## kodumuzu bu şekilde yazdığımızda sonuç olarak 50 dönecektir. Çünkü metin değerini int veri tipine dönüştürmüş olduk


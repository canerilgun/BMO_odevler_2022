#kisiler isimli bos bir liste olusturalim
kisiler=[]
#kisiler isimli bos listeye kullanicidan 3 isim girelim
a=input("isim giriniz:")
kisiler.append(a)
b=input("isim giriniz:")
kisiler.append(b)
c=input("isim giriniz:")
kisiler.append(c)
#listeyi ekrana yazdiralim
print(kisiler)
#listenin uzunlugunu ekrana yazdiralim
uzunluk=len(kisiler)
print("listenin uzunlugu:",uzunluk)
#listenin ikinci elemanini ekrana yazdiralim
print(kisiler[1])
#listenin son elemanini silelim
kisiler.pop(2)
print(kisiler)
#listeyi ekrana tekrar yazdiralim
print(kisiler)
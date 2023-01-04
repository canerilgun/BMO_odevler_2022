#Tabloyu sinav_sonuc adlı bir sözlüğe aktaralım
sinav_sonuc = {
    'isim': ['Ayşe K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
    'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'],
    'vize': [80, 60, 77, 25, 36, 75],
    'final': [90, 50, 53, 100, 98, 66]
}
#Öğrencilerin geçme notunu hesaplayacak formülü yazalım
def gecme_notu(vize, final):
  return (vize*30/100)+(final*70/100)

#Öğrencilerin geçme notlarını hesaplayıp sözlükteki verilere ekleyelim
sinav_sonuc['gecme_notu'] = [gecme_notu(vize, final) for vize, final in zip(sinav_sonuc['vize'], sinav_sonuc['final'])]

#Öğrencilere ait bilgilerin kayıtlı olduğu bir fonksiyon yapalım
def kayit(isim, cinsiyet, vize, final):
  sinav_sonuc['isim'].append(isim)
  sinav_sonuc['cinsiyet'].append(cinsiyet)
  sinav_sonuc['vize'].append(vize)
  sinav_sonuc['final'].append(final)
  sinav_sonuc['gecme_notu'].append(gecme_notu(vize, final))

#Kullanıcıdan 2 yeni öğrenci -notları ile birlikte- girelim
for i in range(2):
  isim = input("Öğrenci adi: ")
  cinsiyet = input("Öğrencinin cinsiyeti (K/E): ")
  vize = int(input("Öğrencinin vize notu: "))
  final = int(input("Öğrencinin final notu: "))
  kayit(isim, cinsiyet, vize, final)

#Yeni öğrencilerin eklenmiş olduğu listeyi ekrana yazdıralım
print(sinav_sonuc)
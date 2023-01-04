#listeyi sınav_sonuc isimli bir sözlüğe aktaralım
sinav_sonuc = {'isimler':['Ayse K.' ,'Ahmet M.','Nuri C.','Nawar T. ','Suzan T. ','Ala B.'],
'cinsiyet' : ['K', 'E', 'E', 'E', 'K', 'K'], 
'Turkce' : [90,50,53,100,98,66],
'Matematik' : [80,60,77,25,36,75]
}
#kadınlar ve erkekler için boş birer liste oluşturalım
erkek = []
kadin = []
#arttırmalar sıfırdan başlanır
count_ka = 0
count_er = 0
ka_matematik = 0
ka_turkce = 0
er_matematik = 0
er_turkce = 0
#cinsiyete göre matematik ve türkçe notları arttırılarak yapalım
for i in range(len(sinav_sonuc['cinsiyet'])):
    if (sinav_sonuc['cinsiyet'][i] == 'K'):
        count_ka +=1 
        ka_matematik =ka_matematik + sinav_sonuc['Matematik'][i]
        ka_turkce =ka_turkce + sinav_sonuc['Turkce'][i]
        kadin.append(sinav_sonuc['Turkce'][i])
    else: 
        count_er +=1 
        er_matematik =er_matematik + sinav_sonuc['Matematik'][i]
        er_turkce =er_turkce + sinav_sonuc['Turkce'][i]
        erkek.append(sinav_sonuc['Turkce'][i])
#istenilen durumları ekrana yazalım
print(f"Erkeklerin matematik ortalamasi:" ,{er_matematik/count_er})
print(f"Kadinlarin matematik ortalamasi:" ,{ka_matematik/count_ka})
print(f" Kursun toplam Turkce ortalamasi:" ,{((ka_turkce + er_turkce)/(count_er + count_ka))})
print("Turkce icin erkek en yuksek Elemani: ",max(erkek))     
print("Turkce icin kadin en yuksek Elemani: ",max(kadin))


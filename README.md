# Opencv-Selective-Search
# python selective_search.py --image dog.jpg --method fast
Daha hızlı sürede bölge önerileri alıyoruz ancak isabetlik oranı çok fazla olmayabilir.
[BILGI] hızlı seçici arama kullanılıyor
[BILGI] seçici arama 2.7339 saniye sürdü
[BILGI] Toplam 1219 bölge teklifi vardır.

![SS-fast](https://user-images.githubusercontent.com/64548477/93670289-0cd32980-faa3-11ea-948c-9eb5d1727bd9.gif)

# python selective_search.py --image dog.jpg --method quality  
[BILGI] yavaş seçici arama kullanılıyor
[BILGI] seçici arama 8.9593 saniye sürdü
[BILGI] Toplam 4709 bölge teklifi vardır.

Uzun sürer ancak isabet oranı yüksek bölge önerileri alabiliriz.

![Ss-slow](https://user-images.githubusercontent.com/64548477/93670354-8539ea80-faa3-11ea-988b-bbb05a7314af.gif)

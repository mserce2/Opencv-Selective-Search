#kütüphanelerimizi ekliyoruz

import argparse
import random
import cv2
import time

#Bağımsız değşkenlerimi yapılandırıyoruz
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,
                help="path to the input image") #Giriş resmimiz için path gireceğiz
ap.add_argument("-m", "--method", type=str, default="fast",
                choices=["fast","quality"],  #Daha sonra resim üzerinde hangi seçmeli algoritmayı kullacağımızı belirteceğiz
                help="selective search method")
args=vars(ap.parse_args())


#İnput olarak girdi resmimizi yüklüyoruz
image=cv2.imread(args["image"])

#opencv'in seçici arama uygulamasını başlatacağız
ss=cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image) #Başlattığımız seçmeli aramaya girdii olarak image'mizi veriyoruz

#Seçmeli aramanın "hızlı" ancak "daha az doğru" versiyonunu kullanıp kullanmadığımızı kontrol ediyoruz:
if args["method"] =="fast":
    print("[BILGI] hızlı seçici arama kullanılıyor ")
    ss.switchToSelectiveSearchFast() #Hızlı seçici aramayı etkinleştirdik

#aksi halde  daha yavaş  ama  daha doğru sürümü kullanıyoruz
else:
    print("[BILGI] yavaş seçici arama kullanılıyor")
    ss.switchToSelectiveSearchQuality() #Yavaş ama doğruluk oranı yüksek seçmeli arama

#İnput resmimiz üzerinde seçici aramayı çalıştırıyoruz
start=time.time()
rects=ss.process()
end=time.time()
#seçici aramanın, döndürülen toplam bölge teklifi sayısıyla birlikte ne kadar sürdüğünü gösteriyoruz
print("[BILGI] seçici arama {:.4f} saniye sürdü".format(end-start))
print("[BILGI] Toplam {} bölge teklifi vardır.".format(len(rects)))


#bölge önerileri üzerinde parçalar halinde döngü yapıyoruz (böylece onları daha iyi görselleştirebiliriz)
for i in range(0,len(rects),100):
    #orijinal resmi klonlıyoruz, böylece üzerine çizim yapabiliriz
    output=image.copy()
    #mevcut bölge tekliflerinin alt kümesi üzerinde döngü yapıyoruz
    for(x,y,w,h) in rects[i:i+100]:
        #resim üzerine bölge önerisi sınırlayıcı kutusunu çiziyoruz
        color=[random.randint(0,255) for j in  range(0,3)] #bölgeler için rastgele renk kodu oluşturuyoruz
        cv2.rectangle(output,(x,y),(x+w,y+h),color,2) #Dikdörtgen çiziyoruz bölge önerisi için

    #Tüm bu yaptıklarımızı görselleştiriyoruz
    cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
    cv2.imshow("Output",output)
    cv2.imshow("Orijinal resim",image)
    key=cv2.waitKey(0) and 0xFF

    if key==ord("q"):#çalışma esnasında q basarsanız program kapanacaktır
        break

"""
45.Satır ve 49.Satırda oluşturulan iç içe döngüler aracılığıyla bölge tekliflerini 100'lük parçalar halinde döngüleyin 
(Seçmeli Arama birkaç yüz ila birkaç bin teklif oluşturacaktır; onları daha iyi görselleştirebilmemiz için onları 
"parçalara ayırıyoruz")Seçici Arama tarafından oluşturulan bölge önerilerimizin her birini çevreleyen sınırlayıcı kutu
koordinatlarını çıkarın ve her biri için renkli bir dikdörtgen çizin (51-56 Satırlar)Sonucu ekranımızda göster 
(Satır 59)Tüm sonuçlar tükenene veya q (çık) tuşuna basılıncaya kadar kullanıcının sonuçlar arasında
(herhangi bir tuşa basarak) dolaşmasına izin verin

"""


"""
Bu programı çalıştırmak için terminali açın ve;
=>python selective_search.py --image dog.jpg 

=>Burada, OpenCV’nin Seçmeli Arama "hızlı modunun" çalıştırılmasının yaklaşık 1 saniye sürdüğünü ve 1.219 sınırlayıcı
kutu ürettiğini görebilirsiniz - Şekilteki görselleştirme, Seçici Arama tarafından oluşturulan bölgelerin her biri
üzerinde döngü oluşturduğumuzu ve bunları ekranımızda görselleştirdiğimizi gösteriyor.Bu görselleştirme kafanız
karıştıysa, Seçici Aramanın son hedefini düşünün: kayan pencereler ve görüntü piramitleri gibi geleneksel bilgisayar
görüşü nesnesi algılama tekniklerini daha verimli bir bölge önerisi oluşturma yöntemiyle değiştirmek.Bu nedenle,
Seçici Arama size ROI'de ne olduğunu söylemeyecek, ancak ROI'nin son sınıflandırma için bir aşağı akış sınıflandırıcıya
(örn. SVM, CNN, vb.) Aktarılacak kadar "yeterince ilginç" olduğunu söyleyecektir.

=> python selective_search.py --image dog.jpg --method quality
=> python selective_search.py --image dog.jpg --method fast

"""

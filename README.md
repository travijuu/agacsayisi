# Ağaç sayısı hesaplama

Karbon dioksit miktarı girilerek, tükettiğiniz kaynağın yerini doldurmak için kaç ağaca ihtiyaç olduğunu hesaplar.

### Gereklilikler

* Python 2.7 ve üzeri


## Açıklamalar
### Ağaç sayısının hesaplanması:

- Ağaçlar çok çeşitli ve farklı ortalama ömürlere sahip olduklarından kısa ömürlü ağaçların
yaş ortalaması 40-50 arası olarak belirlendi ve 45 yaş ortalama yaş olarak alındı.	
(http://www.agacnet.com/node/65)

- Ortalama bir ağaç senede 21.77(22) kg karbon dioksit özümsemektedir.
(https://www.americanforests.org/explore-forests/forest-facts/)

- Kar edilen karbondioksit miktarını senede özümsenen karbondioksit miktarı ve ağaç yaş
ortalamasının çarpımına böldüğümüz zaman(980=~1000) ağaç sayısını buluyoruz. 

#### Katsayı ile enerjinin çarpılması:

- Üretilen elektrik enerjisiyle önceden elle belirlenmis olan katsayının çarpımı veriliyor. 

#### Katsayının hesaplanması:
- Türkiyede elektrik üretebilmek için doğalgaz, ithal kömür, linyit, taş kömürü, fuel oil, rüzgar
enerjisi, jeotermal enerji ve güneş enerjisi kullanılıyor. 2018’in Nisan ayı verilerine göre, doğalgaz, 
elektrik üretiminin %28’inde, ithal kömür %16’sında, linyit %15’inde, taş kömürü %1’inde, rüzgar enerjisi 
%5’inde, jeotermal enerji %3’ünde, fuel oil %0’ında ve son olarak güneş enerjisi %3’ünde kullanıldı. 
Toplamda ise 23,844,12 kWh üretildi. 
[(AYLIK ENERJİ İSTATİSTİKLERİ RAPORU - 4)](http://www.eigm.gov.tr/File/?path=ROOT%2f4%2fDocuments%2f%c4%b0statistik%20Raporu%2f2018%20Nisan%20Ay%c4%b1%20Enerji%20Raporu.pdf)
	
- EMO’ya göre, bu elemanların sera gazı emisyonları(ton- karbon dioksit/GWh) şu şekildedir:
(http://www.emo.org.tr/ekler/15ed8b43a250de0_ek.pdf)
```
Doğalgaz:		499
İthal kömür:		888
Linyit:			1054
Taş kömürü:		888
Fuel oil:		733
Rüzgar enerjisi: 	10
Jeotermal enerji:	38
Güneş enerjisi:		23
```
	
- Her elemana ait elektrik üretimini bulmak için toplam enerji miktarıyla yüzdeler çarpıldı.
Çıkan sonuçla da elemanların sera gazı emisyon değerleri çarpılıp gerekli birim hesaplamaları 
yapıldı.(kg/kWh) Her elemanın sebep  olduğu salınmalar teker teker bulundu ve toplandı. 
Böylece toplam karbondioksit miktarı bulundu. Bu değer de toplam elektrik enerjisine bölündü 
ve katsayı bulundu. 


## Katkı
Daha doğru olduğunu düşündüğünüz hesaplamalar varsa katkıda bulunabilirsiniz. 

## Lisans
[MIT](https://choosealicense.com/licenses/mit/)

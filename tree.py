
def tree():     #ağaç sayısını bulan fonksiyon
	h = input('Karbon dioksit miktarını ton olarak giriniz: ')
	co2miktar = float(h)										
	tree = (co2miktar/1000)*5     #verilen karbondioksit miktarına göre ağaç sayısının bulunması. Ekilen her ağaç doğal seçilim nedeniyle büyüyemediğinden 5 ile çarpılıyor. 
	a = str(tree)                 #Ortalama ağaç yaşı 45, bir senede emdiği karbondioksit 22 ton. Yuvarlama yapınca bu sayı 1000 oluyor. 

	print("Ağaç: " + a )
	return a


def coeff():     #katsayıyla verilen enerjiyi çarpan fonksiyon
	x = input('Enerjiyi giriniz(kWh): ')				
	a = float(x)
	katsayi = 0.45110999999999996     #bu katsayıyı 2018 nisan ayı verilerine göre manuel olarak buldum
	sonuc = katsayi*a                 #katsayıyla girilen verinin çarpılması
	print(sonuc)


def other():     #katsayıyı hesaplayan fonksiyon.
	
	#Katsayıyı hesaplamak için gerekli olan iki veri var biri elemanlara göre üretim yüzdeleri, diğeri ise toplam enerji miktarı.

	#2018 Nisan ayı verileri
	#6 ayda bir aşağıdaki veriler güncellenecek.
	dogalgaz = 28
	ithal = 16
	linyit = 15
	tas = 1
	ruzgar = 5
	jeo = 3
	gunes = 3

	enerji = 23844012

	ton1 = (enerji*dogalgaz/100)*499/1000     #Kaynakta her elemanın oluşturduğu emisyon değerleri var. Doğalgaz için 499 ton/GWh, ithal kömür için 888 ton/GWh vs vs. 
	ton2 = (enerji*ithal/100)*888/1000        #Bu değerleri kg/kWh a çevirip ve basit oran orantıyla formülize ediyoruz.
	ton3 = (enerji*linyit/100)*1054/1000      #Linyitin değeri: 1054 ton/GWh
	ton4 = (enerji*tas/100)*888/1000          #Taş kömürünün değeri: 888 ton/GWh
	ton5 = (enerji*ruzgar/100)*10/1000        #rüzgar enerjisinin değeri: 10 ton/GWh
	ton6 = (enerji*jeo/100)*38/1000	          #jeotermal enerji için : 38 ton/GWh
	ton7 = (enerji*gunes/100)*23/1000         #güneş enerjisi içinse : 23 ton/GWh
	
	print("2018 Nisan ayı verilerine göre, sırasıyla doğalgaz, ithal kömür, linyit, taş kömürü, rüzgar enerjisi, jeotermal enerji, ve güneş enerjisinin karbon dioksit salınım miktarları(kg):")
	print(ton1, ton2, ton3, ton4, ton5, ton6, ton7)

	toplam = ton1+ton2+ton3+ton4+ton5+ton6+ton7     #katsayıyı bulmak için toplam karbon dioksit miktarı gerektiğinden topluyoruz. 
	katsayi = toplam/enerji                         #toplam karbon dioksit miktarını girilen enerjiye böldüğümüz zaman katsayıyı bulmuş oluyoruz.
	print("Katsayı :")
	print(katsayi)
other()

krediler=["Hızlı Krediler","Maaş müşterileri","Mutlu emekliler"]

#diziler aynı birimleri bir arada tutmamızı sağlar.0 dan başlayarak artmaya devam eder.
# köşeli parantez için->option+yukarı ok+8 kullanılır.


krediler[0]="Şimdi değişim zamanı"
#bu tanımladan sonra 0.dizinimiz "şimdi kredi zamanı" olarak değişecektir.
print(krediler[0])# ekrana 0. dizini hızlı kredileri yazar.



for x in range(len(krediler)):#i sadece aliasdır(takma ad).Range for döngüsünün tekrarlanma sayısıdır.Burada krediler değişkeninin sayısı kadar çalıştırılmaktadır.
 print(krediler[x])
   #i=0 olduğunda 0.dizini hızlı kredileri ekrana yazar.For döngüsüyle bu işlem tekrarlanır.
 
for i in range(10):#for döngüsü 10 defa çalışır.
  print(i)

for sayi in range(0,10,2):
    print(sayi)
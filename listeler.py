
krediler=["Hızlı Krediler","Maaş müşterilerine özel krediler","Mutlu emekliler"]
print(krediler[0])
krediler[2]="Değişimin ayak sesleri"
print(len(krediler))#lenght--->Dizide bulunan değişken sayısını verir.
print(krediler)




listeler=["Burak Erol","Zevcesi Merve Erol","Pıtırcıkları Özüm Erol"]
print(listeler[0])
print(listeler[1])
print(listeler[2])


print(8,4,5,7,7,sep="/")
print("MERVE","EROL",sep="\n")

print(*"Merve Erol",sep=" . ")
a=10
b=12

print("{} + {} 'nin değeri {}'dir.".format(a,b,a+b))
liste=[2,3,4,56]
liste1=[10,20,30,40]
liste.append("zazaza" )
print(liste)
liste.pop(3)
print(liste)

yeni_liste=[[1,2],[3,4],[5,6]]
yeni_liste[1]
print(yeni_liste[1][0])

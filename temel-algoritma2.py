

oyuncu=["Zlatan","ibrahimoviç",29,1.77]
oyuncu[2]="31"

oyuncu.append("Barselona")


oyuncu=oyuncu+["Atletico Madrid"]


oyuncu[:2 ]=["Dani","Alves"]
print(oyuncu)


a=int(input("lütfen birinci sayıyı girin:"))
b=int(input("lütfen ikinci sayıyı girin:"))
c=int(input("lütfen üçüncü sayıyı girin:"))
print("Sayıların toplamı:",a+b+c)



print("Oyuncu Kaydetme Programı")
ad=input("Oyuncunun adı:")
soyad=input("Oyuncunun soyadı:")
takim=input("Oyuncunun takımı:")


print("Database e kaydedildi.....\n")

print("Oyuncunun adı:",ad,"\nOyuncunun soyadi:",soyad,"\nOyuncunun takımı",takim)
print("Kaydedildi.....")
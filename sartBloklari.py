dolarDun = 7.99
dolarBugun = 7.85 #float

if dolarDun>dolarBugun:
  print("Azalma var.")
  
elif dolarDun<dolarBugun:
    print("Artma var.")   

else:#yukarıdaki iki şartta geçerli değilse else çalışır.
      print("Eşitlik var.")




num1=4
num2=7
num3=11
enKucukSayi="En küçük sayı:"
enBuyukSayi="En büyük sayı:"

if num1<num2 and num1<num3:
  print(enKucukSayi+""+str(num1))#Sayı stringe çevrilip,işlem yapılır.

elif num2<num3 and num2<num1:
  print(enKucukSayi+""+str(num2))
 
else:
  print(enKucukSayi+""+str(num3))

if num1>num2 and num1>num3:
  print(enBuyukSayi+""+str(num1))
elif num2>num1 and num2>num3:
  print(enBuyukSayi+""+str(num2))  
else:
  print(enBuyukSayi+""+str(num3))


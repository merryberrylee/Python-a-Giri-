merveMesaj="Merhaba arkadaşlar"
print(merveMesaj)
x=12
y=24
print(x+y)
print("x="+str(x)+" "+"y="+str(y))
print(merveMesaj.upper())
print(merveMesaj.lower())
yeni=merveMesaj[2:5]
print(yeni)
x=32
y=44
if x>y:
  print("x y den büyüktür")
else:
  print("y x ten büyüktür")
 


for i in range(20):
  print(i*"*")


günler="Hello World!"



sehirler=list(("Ankara","Adana","Urfalıyam ezelden"))
print(sehirler)
print(sehirler.count("Ankara"))
print(sehirler.index("Ankara"))

sehirler.pop(1) #1. Index'i sıfır yapar.
print(sehirler)
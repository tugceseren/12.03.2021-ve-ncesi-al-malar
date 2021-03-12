vize= 90
final= 30


ort=vize *0.4 + final *0.6

if final<=49:
  print("FF")
  print("kaldı","ortalama:",ort)
elif ort<=55:
  print("DC")
  print("sorumlu geçti","ortalama",ort)
elif ort<=65:
  print("CC")
  print("geçti", "ortalama:", ort)
elif ort<=75:
  print("CB")
  print("geçti", "ortalama:", ort)
elif ort<=85:
  print("BB")
  print("geçti", "ortalama:", ort)
elif ort<=90:
  print("BA")
  print("geçti", "ortalama:", ort)
elif ort<=100:
  print("AA")
  print("geçti", "ortalama:", ort)
else:
  print("hatalı not girdiniz. ortalama:", ort)

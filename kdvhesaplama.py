a = int(input("Fiyat:  "))
b = float(input("KDV Oranı: "))

print("Fiyat: ",a,"₺")
print("KDV Oranı: ","%",b)
print("KDV Fiyatı: ",a*b/100,"₺")
print("KDV Dahil Toplam Fiyat:", a + a*b/100, "₺")

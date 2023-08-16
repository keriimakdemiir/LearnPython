sayac = 0

print("while loop started")
while sayac <= 10:
    print(sayac)
    sayac += 1
print("while loop ended")

# Example

p = 0
while p <= 20:
    print(f"value of p: {p}")
    p += 1

# Continue, Break, Pass

# Example
# continue
# # 1-100 arasındaki çift sayıların toplamını ekrana yazdırın ama continue kullanarak problemi çözün.

sayac = 0
cift_toplam = 0

while sayac < 100:
    sayac +=1
    if sayac % 2 !=0:
        continue
    cift_toplam += sayac
print(f"Çift sayıların toplamı: {cift_toplam}")

# Example
# break
# 1-10 arasındaki sayıları yazdır. 5'i bulunca döngüden çıkın ve yes yazdırın.

sayac = 0
while sayac <= 10:
    print(sayac)
    if sayac == 5:
        print("yes")
        break
    sayac += 1

# Example
# pass

sayac = 0
while sayac <= 10:
    pass


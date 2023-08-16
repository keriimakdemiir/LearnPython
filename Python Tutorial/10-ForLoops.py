my_list = [10,20,30,40,50,60]

for num in my_list:
    print(num / 5 * 2)


print("for loop started")
for x in my_list:
    new_number = x / 5 * 2
    print(new_number)
print("for loop ended")

for number in my_list:
    if number % 6 == 0:
        print(number)

# Example

my_string = "Kerim Akdemir"

for c in my_string:
    print(c)

# Range

for x in range(2, 30, 3):
  print(x)

# Example
# 0 ile 100 arasında kaç tane çift sayı ve kaç tane tek sayı var yazdıralım

tek_sayi = 0
cift_sayi = 0

for num in range(0,101):
  if num % 2 == 0:
    cift_sayi += 1
  else:
    tek_sayi += 1

print(f"Tek sayıların adedi= {tek_sayi}\nÇift sayıların adedi= {cift_sayi}")

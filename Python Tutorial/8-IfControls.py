x = 3
y = 5

if x > y:
    print("x")
else:
    print("y")

# Example

my_superhero = input("Superhero: ")

my_superhero_list = ["Spider Man","Iron Man","Thor","Black Widow"]

if my_superhero in my_superhero_list:
    print(":)")
else:
    print(":(")

# Example

my_superhero = input("enter superhero: ").lower()

if my_superhero == "superman":
    print("superman")
elif my_superhero == "batman":
    print("batman")
elif my_superhero == "aquaman":
    print("aquaman")
elif my_superhero == "ironman":
    print("ironman")
else:
    print(":(")

# Nested if-else
# araç ve Hız

arac = input("Araç: ")
hiz = int(input("Hız: "))

if hiz > 0:
    if arac == "otomobil" or arac == "motorsiklet":
        if hiz > 90:
            print(f"{arac} 90 hız sınırını açtığı için cezalıdır")
        else:
            print("Cezalı değildir")
    if arac == "kamyon":
        if hiz > 60:
            print(f"{arac} 60 hız sınırını açtığı için cezalıdır")
        else:
            print("Cezalı değildir")
    else:
        print("Lütfen araç bilgisini kontrol ediniz")
else:
    print("Lütfen pozitif tam sayı hız değeri giriniz")
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

# Example

# Kullanıcıdan user_name ve password ve role bilgilerini alalım
# user_name = beast password = 123 ise role = admin ise ekrana welcome the major yazdırın
# user_name = beast password = 123 ise role = super admin ise ekrana welcome the beast yazdırın
# user_name= bear , password = 321 ise role = manager ise ekrana welcome the manager
# user_name= savage , password = 987 ise role manager ise ekrana welcome savage raider

user_name = input("User Name: ")
password = input("Password: ")
role = input("Role: ")

if user_name == "beast" and password == "123":
    if role == "admin":
        print("welcome the major")
    elif role == "super admin":
        print("welcome the beast")
    else:
        print("yetkiniz bulunmamaktadır")
elif user_name == "bear" and password == "321":
    if role == "manager":
        print("welcome the manager")
    else:
        print("yetkiniz bulunmamaktadır")
elif user_name == "savage" and password == "987":
    if role == "manager":
        print("welcome savage raider")
    else:
        print("yetkiniz bulunmaktadır")
else:
    print("Lütfen bilgilerinizi kontrol ediniz")

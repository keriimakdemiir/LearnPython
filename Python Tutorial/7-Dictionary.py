# Key-Value pairing

my_dictionary = {"key1":"value1","key2":"value2","key3":"value3"}

print(my_dictionary["key2"])

# Example

actor_dict = dict(name = "Robert De Niro", age = 79, nationality = "American")

print(actor_dict.keys())
print(actor_dict.values())

# Nested Dictionary

last_dictionary = {"k1":10,"k2":[10,20,30,40,50],"k3":"string","k4":{"a":100,"b":200}}

print(last_dictionary["k2"][3])
print(last_dictionary["k4"]["b"])
print(last_dictionary.get("k3"))
print(len(last_dictionary))

last_dictionary.update({"k3": "integer"})
print(last_dictionary)
last_dictionary["k5"] = True
print(last_dictionary)
last_dictionary.pop("k5")
print(last_dictionary)


# Aşağıdaki "a"'yı tek satırda alınız.

new_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}

print(new_dictionary["kk2"][1]["k21"])

# Example

my_dictionary = {"k1": 10, "k2k": "a", "k32": 30, "k4": "c"}

if "a" in my_dictionary.values():
    print("yes")


# Example

products = [
	{'name': 'Everlast Pro Boxing Gloves', 'price': 245},
	{'name': 'Everlast Training Gloves', 'price': 145},
	{'name': 'Everlast Heavy Bag', 'price': 345},
	{'name': 'Everlast Hand-Wrap', 'price': 45},
	{'name': 'Iphone 14 Pro Max', 'price': 52000},
	{'name': 'Samsung S23 Ultra', 'price': 53000},
	{'name': 'Lenovo X1 Carbon', 'price': 49000}
    ]

# products listesindeki bütün ürünlerin fiyatını toplayın

for product in products:
    total = 0
    total += product["price"]
print(f"Total Price: {total}")

# products listesindeki fiyatı 30000'den büyük olan ürünlerin isimlerini yazdırın

for product in products:
    if product["price"] > 3000:
        print(f"Name: {product.get('name')} - Price: {product['price']}")

# ürün adı içerisinde Everlast geçen ve fiyat aralığı 150 ile 400 arasında olan ürünleri listeleyin

for product in products:
    if "Everlast" in product["name"] and 150 < product["price"] < 400:
        print(f"Name: {product.get('name')} - Price: {product['price']}")
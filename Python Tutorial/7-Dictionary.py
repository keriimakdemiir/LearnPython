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
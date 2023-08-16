print("hello python")

# Example

name = "kerim"

print(type(name))
print(len(name))
print(name.capitalize())
print(name.upper())

# Example
restaurant = "ARDA'S RESTAURANT"

print(restaurant.lower())
print(restaurant.count("A"))
print(restaurant.split())

# Index

myString = "Gordon Ramsay"   # camel case
best_chef = "Anthony Bourdain" # snake case

print(best_chef[0])
print(best_chef[-1])
print(best_chef.index("B"))

# Slicing[starting index:stopping index:stepping size]

barcode = "KA190794"

print(barcode[0:7:2])
print(barcode[0]+barcode[1]+barcode[2])
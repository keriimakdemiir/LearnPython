myTuple = (10,"a","b",3.14)

print(type(myTuple))
print(myTuple[3])

# A tuple with strings, integers and boolean values

tuple1 = ("Victoria", "Azarenka")
tuple2 = (1, 9, 8, 9)
tuple3 = (True, False, False)
tuple4 = ("Azarenka", 1989, True)

# Example

this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.append("orange")
this_tuple = tuple(y)

print(this_tuple)

# Example

thisTuple = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple += y

print(thisTuple)

# Example

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
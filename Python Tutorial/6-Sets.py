# Duplicate values will be ignored:

fruit_set = {"apple", "banana", "cherry", "apple"}

print(fruit_set)

countrySet = {"de","fr","tr","fr","tr","tr","de","nl","de","tr"}

print(countrySet)
print(len(countrySet))
print(type(countrySet))


# True and 1 is considered the same value:

this_set = {"apple", "banana", "cherry", True, 1, 2}

print(this_set)

# Example

thisSet = {"apple", "banana", "cherry"}
tropical_set = {"pineapple", "mango", "papaya"}

thisSet.update(tropical_set)
print(thisSet)

thisSet.remove("banana")
print(thisSet)

thisSet.add("banana")
print(thisSet)

# A set with strings, integers and boolean values

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
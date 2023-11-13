# A list with strings, integers and boolean values

list1 = ["Rafael", "Nadal"]
list2 = [1,9,8,6]
list3 = [True, False, False]
list4 = ["Male", 37, True]

# Example

x = 10
y = 20
z = 30

my_new_list = [x,y,z]

print(my_new_list)
print(my_new_list[0])
print(type(my_new_list))
print(type(my_new_list[0]))

my_new_list.append(40)
print(my_new_list)

my_new_list.insert(4,50)
print(my_new_list)

my_new_list.pop()
print(my_new_list)

my_new_list.remove(40)
print(my_new_list)

my_new_list[2] = 40
print(my_new_list)

del my_new_list[2]
print(my_new_list)

# Nested List

lastList = [0,1,[2,3],4,[5,6]]

print(lastList[4][1])

smallList = lastList[-1]

print(smallList)


from random import randint, shuffle

print(randint(0, 100))

my_list = [10, 20, 30, 40, 50, 60]
shuffle(my_list)
print(my_list)

# Zip

food_list = ["apple", "banana", "melon"]
calories_list = [100, 150, 200]
day_list = ["monday", "tuesday", "wednesday"]

zipped_list = list(zip(food_list, calories_list, day_list))
print(zipped_list)

# list comprehension

number_list = [10,20,30,40,50,60]
new_number_list = [num/2 for num in number_list]
print(new_number_list)

new_number_list = []
for num in number_list:
    new_number_list.append(num/2)
print(new_number_list)
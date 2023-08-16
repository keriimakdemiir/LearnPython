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
def hello_python():
    print("hello")
    print("python")

hello_python()

#input

def hello_name(name):
    print("hello")
    print(name)

hello_name("java")

# Example

def sum_example(num1, num2):
    num3 = num1 + num2
    print(num3)

sum_example(20, 12)

# Example

def hello_surname(surname="akdemir"):
    print("hello")
    print(surname)

hello_surname()

# Return

def return_summation(num1, num2, num3):
    result = num1+num2+num3
    print(result)
    return result

x = return_summation(10, 2, 8)


# args, kwargs (arguments, key word arguments)

def args_sum(*args):
    print(sum(args))

args_sum(10, 20, 30, 40, 50, 60)


def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(apple=100, banana=150, melon=200)

# Example

def divideNumber(number):
    return number / 2

myList = [3, 5, 7, 10, 20, 30]
myResultList = []

for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)

# Map

print(list(map(divideNumber, myList)))

# Filter

def controlString(string):
    return "Kerim" in string

myStringList = ["Kerim", "Kerim Akdemir", "Akdemir", "Kadayıf"]

print(list(filter(controlString, myStringList)))

# Lambda

numList = [10, 20, 30, 40]

print(list(map(lambda num: num/4, numList)))

# Scope

# LEGB  L->Local, E-> Enclosing, G->Global, B->Built-In

#Global
my_string = "Kerim"

def myFunction():
    #Enclosing
    my_string = "Kerim 2"
    print(my_string)

    def myFunction2():
        #Local
        my_string = "Kerim 3"
        print(my_string)

    myFunction2()

# Example

y = 10

def changeY():
    global y
    y = 5
    print(y)

changeY()
print(y)
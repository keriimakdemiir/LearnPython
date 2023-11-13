# try - except

while True:
    try:
        myAge = int(input("enter age: "))
        print(myAge * 2)
        break
    except ValueError:
        print("enter your age!")
    finally:
        print("finally")
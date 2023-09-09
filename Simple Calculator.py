import math

while True:
    print("list of operations: a x b, a/b, a-b, a+b, a^b, math.sqrt(a)")
    response = (input("What operation would you like to do:  "))
    if (response == "Multiplication" or response == "multiplication"):
                a = input("what is the first factor: " )
                b = input ("what is the second factor: " )
                c = int(a) * int(b)
                print ( a, "x", b, "is equal to", c)
    elif (response == "Addition" or response == "addition"):
        a = input("what is the first factor: " )
        b = input ("what is the second factor: " )
        c = int(a) + int(b)
        print ( a, "+", b, "is equal to", c)
    elif (response == "division" or response == "Division"):
        a = input("what is the first factor: " )
        b = input ("what is the second factor: " )
        c = int(a) / int(b)
        print ( a, "/", b, "is equal to", c)
    elif (response == "subtraction" or response == "Subtraction"):
        a = input("what is the first factor: " )
        b = input ("what is the second factor: " )
        c = int(a) - int(b)
        print ( a, "-", b, "is equal to", c)
    elif (response == "exponent" or response == "exponent"):
        a = input("what is the first factor:  ")
        b = input ("what is the second factor: " )
        c = int(a) ** int(b)
        print( a, "to the power of", b, "is equal to", c)
    elif (response == "square root" or response == "Square root"):
        a = input("what is being square rooted: " )
        c = math.sqrt(int(a))
        print ("The square root of", a, "is equal to", c)
    
    choice = input("Would you like to use it again: " )
    if choice == ("no" or "No"):
        break




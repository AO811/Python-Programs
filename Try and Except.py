try:
    number=int(input("Enter a number "))
    print(number)                           #Simple try and except
except:
    print("Invalid input")

print()

try:
    a=10/0
    number=int(input("Enter a number "))
    print(number)
except ZeroDivisionError:
    print("Number divided by zero")         #Program recognizes 10/0 as ZeroDivisionError
except ValueError:                          #Hence chooses the req. except block
    print("Invalid input")

print()

try:
    number=int(input("Enter a number "))
    print(number)
except ZeroDivisionError:               #Program can recognize the input error
    print("Number divided by zero")     #Hence chooses the req. except block 
except ValueError:
    print("Invalid input")

print()

try:
    a=10/0
    number=int(input("Enter a number "))      
    print(number)                          #Program recognizes 10/0 as ZeroDivisionError
except ZeroDivisionError as err:           #Program will now choose the req. except block and will give a statement on its own 
    print(err)
except ValueError as errr:
    print(errr)

print()

try:
    number=int(input("Enter a number "))  #Program can recognize the input error
    print(number)                         #Program will now choose the req. except block and will give a statement on its own
except ZeroDivisionError as err:
    print(err)
except ValueError as errr:
    print(errr)





















    

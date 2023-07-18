def func(num):
    print("This is the first function")
    print("Yay!")
    return(num*num)

print("Hello")
result=func(4)
print("Nice to meet y'all")
print(result)

def hi(name,age):
    print("Hello "+name+", you are "+str(age))
name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
hi(name,age)
    

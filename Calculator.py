
print("                       ****Welcome to calculator****")
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

def calc(a,b):
 c=str(input("Choose from addition,subtraction,division and multiplication:"))
 c=c.lower()
 if(c=="addition"or c=="add" or c=="sum" or c=="plus" or c=="+"):
    return(str(a+b))
 elif(c=="subtraction"or c=="subtract" or c=="minus" or c=="-"):
    return(str(a-b))
 elif(c=="division"or c=="divide" or c=="slash" or c=="/"):
    return(str(a/b)) 
 elif(c=="multiplication"or c=="multiply" or c=="product" or c=="*" or c=="x"):
   return(str(a*b))

result=calc(a, b)
print(result)
      
      
        

#My name is Abhik Das
#I created this code
def Translator(phrase):
    Translation=""                     
    for letter in phrase:                 
        if letter in "AEIOUaeiou":
            if letter.isupper():
                Translation=Translation + "G"
            else:
                Translation=Translation + "g"
        else:
             Translation=Translation + letter
    return Translation

print("Welcome to G Translator device.")
print("All vowels get converted to letter 'g' or 'G'")
print(Translator(input("ENTER PHRASE: ")))

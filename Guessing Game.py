print("Welcome to the guessing game")
print("If you guess the correct number you win")
print("You have five tries")
print("Hint: The number is between 0 to 50")
print("Note: Enter only an integer number")
n=6
a=0
count=0
while count<5:
    a=int(input("Enter your guess in digits:"))
    if a==n:
        print("Hooray! You win")
        break
    elif a!=n and count<4:
        print("Nope! Try again :)")
    elif a!=n and count==4:
        print("Nope! You lose")
    count=count+1
    

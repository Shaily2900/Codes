import random
color=['red','orange','pink','purple','green','grey','brown','blue','black','white']

while True:
 colors=color[random.randint(0,len(color)-1)]
 guess = input("Enter your guess:")
 while True:
   if (guess.lower()==colors):
    break
   else:
    guess = input("Nope,your guess is wrong, try again:")

 print("You guessed the right color",colors)
    
 try_again=input("Press enter to continue else type no to exit.")
 
 if try_again.lower()== 'no':
   break

print("Thank you for playing.")

         
  
  

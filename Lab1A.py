print("Practical 1A")

#To add two numbers
def addition(x,y):
 return x+y
#To sub two numbers
def subtract(x,y):
 return x-y
#To mul two numbers
def multiply(x,y):
 return x*y
#To div two numbers
def divide(x,y):
 return x/y


print("Select the operator:")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

while True:
 choice=input("The selected operator is:")
 if choice in('1','2','3','4'):
  x=float(input("x:"))
  y=float(input("y:"))

 if choice=='1':
  print("The addition of two numbers is:",addition(x,y))
        
 elif choice=='2':
  print("The subtraction of two numbers is:",subtract(x,y))

 elif choice=='3':
  print("The multiplication of two numbers is:",multiply(x,y))

 elif choice=='4':
  print("The division of two numbers is:",divide(x,y))

 elif choice=='5':
     
  break

 else:
  print("Invalid input")


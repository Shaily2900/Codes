import random
x=0
people=[]
while x<8:
 name=(input("Enter the name:"))
 people.append(name)
 x+=1
print(people)
ran_name= random.choice(people)
print("Random choice:",ran_name)

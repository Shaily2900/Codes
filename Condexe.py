weight= float(input("Enter your weight in kg:"))
height= float(input("Enter your height in meters:"))
BMI= (weight)/(height*height)
print("Your BMI is:",round(BMI,2))
if(BMI<=18.5):
 classification="Underweight"
elif(BMI>18.5 or BMI<=24.9):
 classification="normal weight"
elif(BMI>24.5 or BMI<=29.9):
 classification= "overweight"
else:
 classification= "obesity"

print("The BMI classification is:", classification)
 
 

#Area of triangle
import math


a= float(input("Enter the length of side 1:"))
b= float(input("Enter the length of side 2:"))
c= float(input("Enter the length of side 3:"))
if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):
 print('Not a valid triangle')
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5
print("The semiperimeter of the triangle is:",s)
print("The area of the triangle is:",area)

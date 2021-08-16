from fractions import gcd

a= int(input("a:"))
b= int(input("b:"))

if gcd(a, b) == 1:
 print("True")
else:
 print("False")

Dict={'name':'abc','age':'40','profession':'doctor','address':'guj','phone':'326'}
x=input("Enter the details you want about person:").lower()
result=Dict.get(x,"Detail not present")
print(result)

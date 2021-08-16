months=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec")
bd=input("Enter birthdate in DD-MM-YYYY:")
index=int(bd[3:5])-1
bdmonth= months[index]
print("You were born in the month:",bdmonth)

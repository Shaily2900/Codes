def prac(num,coun):
 if (coun<=0):
    return
 else:
    print(num,end="")
    num+=1
    coun-=1
    prac(num,coun)

num=int(input("Enter the num:"))
prac(num,num)


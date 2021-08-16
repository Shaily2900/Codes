import matplotlib.pyplot as plt
import time as t

times=[]
mistakes=0

input("Press enter to continue.")
while len(times)<5:
 start_t= t.time()
 word=input("Enter the word:")
 end_t=t.time()
 time_elapsed= end_t - start_t

 times.append(time_elapsed)
 if (word.lower()!="python"):
  mistakes+=1

print("You made"+str(mistakes)+"mistake(s).")
print(time_elapsed)
print("Let's see the evolution")
t.sleep(3)

x=[1,2,3,4,5]
y=times
plt.plot(x,y)
legend=['1','2','3','4','5']
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.show()

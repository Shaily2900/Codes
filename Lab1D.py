word = input("Enter the word:")
print(word)
freq={}
output=''
for x in word:
 if x in freq:
  freq[x]=freq[x]+1
  output=output+ '*'
 else:
  freq[x]=1
  output=output+ x
     
print(output)

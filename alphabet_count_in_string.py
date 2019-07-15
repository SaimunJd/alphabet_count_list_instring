s=input("word=")
k=0
for i in range(0,len(s)):
	m=s[i]
	for j in range(len(s)):
	    if(s[j]==m):
	    	k+=1
	print(m,"=",k)
	k=0

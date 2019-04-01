#Modify the previous program
#such that only multiples of three or five are considered in the sum

num = eval(input("Please type in a number: "))
res=0
for x in range(num+1):
	if x%3==0 or x%5==0:
		res+=x
print (res)

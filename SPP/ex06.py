# Write a program that asks the user for a number n and gives them the possibility to choose
# between computing the sum and computing the product of 1,…,n.

num=eval(input("Insert a number"))
opt=eval(input("Type 1 if you want to multiply, 2 if you want to sum"))
if opt==1:
	res=1
	for x in range(1, num+1):
		res*=x
elif opt==2:
	res=0
	for x in range(num+1):
		res+=x
else:
	print("cry me a river")
print(res)

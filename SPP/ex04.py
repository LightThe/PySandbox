#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

num = eval(input("Please type in a number"))
res=0
for x in range(num+1):
	res+=x
print ("adding from 1 to "+str(num)+" you have: "+str(res))

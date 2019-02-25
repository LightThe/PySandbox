print("This is my first Python file\n")

#this is a comment
"""this is a docstring
it can have multiple lines"""

#input recieves keyboard text
#eval processes (evaluates) this input
print("insert some X number")
x = eval(input())
print("now insert another Y one")
y = eval(input())
res = x + y

#conversion from int to string (casting)
print("This software can sum the nubers, it's "+str(res))
print("I can even say how these numbers compare to each other")

#if and else
if x > y:
	print("X is greater than Y")
elif y > x:
	print("Y is greater than X")
else:
	print("I guess the numbers are equal")

print ("talk about some serious computation power right there")

# Write a program that prints a multiplication table for numbers up to 12.

print("Multiplication tables up to 12")

for x in range(1, 13):
    print("\nTable of "+str(x))
    for y in range(1, 11):
        res = x*y
        print(str(x)+" * "+str(y)+" = "+str(res))
print("It's done")

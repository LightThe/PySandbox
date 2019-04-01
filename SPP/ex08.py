# Write a program that prints all prime numbers (in a range).

def isPrime(n):
    if n<=3:
        return n > 1
    elif (x%2)==0 or (x%3)==0:
        return False
    y=5
    while(y**2) <= n:
        if (n%y)==0 or (n%(y+2))==0:
            return False
        y = y+6
    return True

for x in range(2, 100):
    if isPrime(x):
        print(x)
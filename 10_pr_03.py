
n=int(input("Enter a number\n"))

def sum(n):
    if n==1 or n==0:
        return 1
    return n + sum(n-1)

print(sum(n))    



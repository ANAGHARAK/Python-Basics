num=int(input("Enter the number "))
for i in range (2,num):
    if num%i==0:
        print('The number is not a prime number')
        break
    else:
        print("The number is a prime number ")
        
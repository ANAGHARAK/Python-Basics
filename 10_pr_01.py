num1=int(input("Enter number 1\n"))
num2=int(input("Enter number 2\n"))
num3=int(input("Enter number 3\n"))
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
print("The greater number is "+ str(maximum(num1,num2,num3)))
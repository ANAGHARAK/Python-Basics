a=int(input("Enter a number "))
b=int(input("Enter another number "))
print("What function you want to perform?")
list=['add', 'subtract', 'multiply', 'divide']
print("Options are: " + str(list))
c= input("What function you want to perform? ")
add=a+b
sub=a-b
mul=a*b
div=a/b
if c=="add":
    print(add)
elif c=="subtract":
    print(sub)
elif c=="multiply":
    print(mul)
elif c=="divide":
    print(div)
else:
    print("Invalid Input!")
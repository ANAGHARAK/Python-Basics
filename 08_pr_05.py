marks=int(input("Enter your marks\n"))
if(marks<=100 and marks>90):
    print("Your Grade is Ex! Keep it Up!")
elif(marks<=90 and marks>80):
    print("Your Grade is A!")
elif(marks<=80 and marks>70):
    print("Your Grade is B!")
elif(marks<=70 and marks>60):
    print("Your Grade is C! ")  
elif(marks<=60 and marks>50):
    print("Your Grade is D!")  
else:
    print("Your grade is F")

sub1=float(input("Enter marks of first subject\n"))
sub2=float(input("Enter marks of second subject\n"))
sub3=float(input("Enter marks of third subject\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed because you have less than 33% in any one subject")
elif(sub1+sub2+sub3/3 < 40):
    print("You are failed because of percentage less than 40%")
else:
    print("You are passed, Congratulations!")     

    



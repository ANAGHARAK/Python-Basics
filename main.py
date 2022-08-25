import random


def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True


           

print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randomNo=random.randint(1,3)
if randomNo==1:
    comp="s"
elif randomNo==2:
    comp ="w" 
elif randomNo==3:
    comp="g"

    
you=input("Your turn: Snake(s) Water(w) or Gun(g)?")
print(f"Comp chose {comp}")
print(f"You chose {you}")
a=gamewin(comp,you)
if a==None:
    print("There is a tie")
elif a==False:
    print("You lose")

elif a==True:
    print("You win!")
text=input("Enter the text\n")
spam=False
if("make a lot of money" in text ):
    spam=True
    print("WARNING! This is a spam message")
elif("buy now" in text):
    spam=True
    print("WARNING! This is a spam message")
elif("watch this" in text):
    spam=True   
    print("WARNING! This is a spam message")
elif("click this" in text):
    spam=True   
    print("WARNING! This is a spam message")  
elif("subscribe this" in text):
    spam=True 
    print("WARNING! This is a spam message")   
else:
    print("This is not a spam message") 

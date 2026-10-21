fullname = input("Enter full name:")
staffnumber = input("Enter staff number")
level = input("Enter level")

if fullname.strip() =="":
    print("Error: full name cannot be empty.")
    
elif not staffnumber.isdigit():

    print ("Error: staff number must contain numeric values only.")

else:
    print("Full name:",fullname)
    print("staff number:",staffnumber)
    print("Level:",level)
    

    
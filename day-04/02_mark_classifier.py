mark = (input("Enter a mark "))



while mark == "" or not mark.isdigit():
    print("Please enter a mark")
    mark = input("Enter a mark ")
mark = int(mark)
if mark >= 0 and mark <= 100:
    if mark >= 80:
        print("Outstanding")
    elif mark >= 70:
         print("Highly competent")
    elif mark >= 50:
         print("Competent")
    elif mark >= 40:
         print("Not yet competent")
    else:
         print("Not achieved")
else:
        print("Invalid mark")
   
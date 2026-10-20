#Highest common factor (Problem 4)
first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

if first < second:
    factor = first
else:
    factor = second
        
while first % factor != 0 or second % factor != 0:
    factor = factor - 1
            
print("The highest common factor is", factor)
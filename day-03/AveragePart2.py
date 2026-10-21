# This program inputs four quiz marks and calculates the average
mark1 = float(input("Enter quiz mark1:"))
mark2 = float(input("Enter quiz mark2:"))
mark3 = float(input("Enter quiz mark3:"))
mark4 = float(input("Enter quiz mark4:"))

average = (mark1 + mark2 + mark3 + mark4) / 4

print("The Average is:", f"{average : .2f}")
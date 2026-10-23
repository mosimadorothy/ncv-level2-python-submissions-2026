marks = []
mark = int(input("Please enter a mark(or -1 to stop) "))
i = 0
while mark != -1:
    #add values in the list
    marks.append(mark) 

    mark = int(input("Please enter a mark(or -1 to stop) "))
print(f'Our list has {len(marks)} elements')

for x in range(len(marks)):
    print("Student" , x + 1,":", marks[x])
    
    ##get the sum of all marks
    sum = 0
for x in range(len(marks)):
    mark = marks[x]
    sum = sum + mark
print(f'The sum of all marks = {sum}')
 
 
 ##Get the average of all marks
total = 0
for x in range(len(marks)):
     mark = marks[x]
     total = total + mark
     avg = total / len(marks)
print(f'The average of all marks = {avg}')
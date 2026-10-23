#LISTS AND FUNCTIONS
def getMarks():
    marks = []
    mark = int(input("Please enter a mark(or -1 to stop) "))

    while mark != -1:
    #add values in the list
        marks.append(mark)
        mark = int(input("Please enter a mark(or -1 to stop) "))
    return marks
    
def print_list_size(marks):
    print(f'Our list has {len(marks)} elements')
    
def print_marks():
    for x in range(len(marks)):
        print("Student" , x + 1,":", marks[x])
    
def get_sum_of_marks(marks):
    sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    return sum

def determine_highesst(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if (current_mark > highest):
            highest = current_mark
    print(f'The highest mark is {highest}')
    
menu = 'Press 1: Capturing marks\n'
menu += 'Press 2: Check number of marks\n'
menu += 'Press 3: To calculate sum of marks\n'
menu += 'Press 4: To find highest marks\n'
menu += 'Press -1: To exit\n'
print(menu)
choice = int(input(' : Make your choice'))

entered_marks = []
while choice != -1:
    if choice == 1:
        entered_marks = getMarks()
        print(entered_marks)
    elif choice == 2:
        print_list_size(entered_marks)
    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print('Sum of all marks = ', calc_sum)
    elif choice == 4:
        determine_highesst(entered_marks)
    else: print('not on the menu')
    print(menu)
    choice = int(input(': Make your choice (-1 to exit)'))

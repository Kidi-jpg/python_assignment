def calculate_grade():
    name = input("Enter student name: ")
    marks = []
    
    
    for i in range(1, 6):
        mark = float(input(f"Enter mark for Subject {i}: "))
        marks.append(mark)
    
  
    average = sum(marks) / 5
    

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
 
    print(f"\nStudent: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


calculate_grade()
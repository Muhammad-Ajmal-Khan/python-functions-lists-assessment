# Get number of students
def get_num_students():
    while True:
        try:
            num = int(input("How many students are in the class? "))
            if num > 0:
                return num
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# marks between 0 and 100
def get_valid_mark():
    while True:
        try:
            mark = int(input("Enter marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# lists as per assignment instructions
student_names = []
student_marks = []

numStudents = get_num_students()

# Loop to collect data
for i in range(numStudents):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    student_names.append(name)
    
    mark = get_valid_mark()
    student_marks.append(mark)

# Calculations using built in list functions
totalMarks = sum(student_marks)
classAvg = totalMarks / len(student_marks)
highestMark = max(student_marks)
lowestMark = min(student_marks)

# Count pass and fail students
passCount = 0
failCount = 0
for mark in student_marks:
    if mark >= 50:
        passCount += 1
    else:
        failCount += 1

# Display Report
print("\nClass Analysis Report")
print(f"Class Average: {classAvg:.2f}")

print(f"\nHighest Marks: {highestMark}")
print("Achieved by:")
# who get the highest marks
for i in range(len(student_marks)):
    if student_marks[i] == highestMark:
        print(student_names[i])

print(f"\nLowest Marks: {lowestMark}")
print("Achieved by:")
# who get the lowest marks
for i in range(len(student_marks)):
    if student_marks[i] == lowestMark:
        print(student_names[i])

print("\nPerformance Summary")
print(f"Passing Students: {passCount}")
print(f"Failing Students: {failCount}")

print("\nStudents above class average:")
for i in range(len(student_marks)):
    if student_marks[i] > classAvg:
        print(f"{student_names[i]} ({student_marks[i]} marks)")

print("\nMarks sorted from highest to lowest:")
# sorted with reverse=True to sort descending
sortedMarks = sorted(student_marks, reverse=True)
for mark in sortedMarks:
    print(mark)
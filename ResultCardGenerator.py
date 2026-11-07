def format_name(name):
    return name.strip().title()

def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Error: Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_percentage(total, max_total):
    return (total / max_total) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

# Get name.
rawName = input("Enter student's name: ")
studentName = format_name(rawName)

# Get roll number
rollNumber = ""
while not rollNumber.isdigit():
    rollNumber = input("Enter roll number (please add digits only): ")
    if not rollNumber.isdigit():
        print("Error: Roll number must contain only digits.")

# Get marks for 5 subjects
mathMarks = get_valid_marks("Math")
scienceMarks = get_valid_marks("Science")
englishMarks = get_valid_marks("English")
urduMarks = get_valid_marks("Urdu")
computerMarks = get_valid_marks("Computer")

# total
obtainedMarks = mathMarks + scienceMarks + englishMarks + urduMarks + computerMarks
totalMarks = 500
finalPercentage = calculate_percentage(obtainedMarks, totalMarks)

# grade give to persontage
if mathMarks < 40 or scienceMarks < 40 or englishMarks < 40 or urduMarks < 40 or computerMarks < 40:
    finalStatus = "Fail"
    grade = "no grade because of fail"
else:
    if finalPercentage < 50:
        finalStatus = "Fail"
        grade = "Fail"
    else:
        finalStatus = "Pass"
        grade = get_grade(finalPercentage)

print("\nResult Card")
print(f"Name: {studentName}")
print(f"Roll Number: {rollNumber}")
print(f"Math: {mathMarks}")
print(f"Science: {scienceMarks}")
print(f"English: {englishMarks}")
print(f"Urdu: {urduMarks}")
print(f"Computer: {computerMarks}")
print(f"Total Marks: {obtainedMarks} / {totalMarks}")
print(f"Percentage: {finalPercentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {finalStatus}")
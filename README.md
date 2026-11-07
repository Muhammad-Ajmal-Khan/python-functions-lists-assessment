# Python Functions, Strings and Lists Assessment

This repository contains two Python console applications developed for the assessment on Functions, String manipulation, and Lists. 

## Repository Name
`python-functions-lists-assessment`

## Project Overview & Descriptions

This project is divided into two main tasks. Both programs are designed to evaluate student performance but at different scales (individual vs. class level).

### 1. Task 1: Student Result Card Generator (`result_card_generator.py`)
This program generates a highly detailed, formatted result card for a single student. 
**How it works:**
- It takes the student's name, roll number, and marks for 5 subjects.
- It cleans up the user input (e.g., removing accidental spaces from the name and making the first letters capital).
- It calculates the total marks and overall percentage.
- **Strict Grading Rule:** It checks a special condition where if a student scores less than 40 in *any* single subject, their final result automatically becomes "Fail", even if their overall percentage is high.
- Finally, it prints a clean and aligned result card.

### 2. Task 2: Class Marks Analyzer (`class_marks_analyzer.py`)
This program acts as a data analysis tool for teachers to evaluate an entire class.
**How it works:**
- It asks the teacher how many students are in the class.
- It uses a loop to collect the names and marks of all students and stores them safely inside two separate Python Lists (`student_names` and `student_marks`).
- Once data is collected, it calculates the class average and counts exactly how many students passed (50 or above) and failed (below 50).
- It identifies the top scorers (highest marks) and lowest scorers.
- Finally, it displays a sorted list of all marks in descending order (from highest to lowest) so the teacher can see the ranking.

## Python Concepts & Techniques Used

To build these applications, the following Python concepts were used:

* **Functions:** Used `def` to create reusable blocks of code for calculating percentages, assigning grades, and validating inputs. Also used parameters and `return` statements.
* **String Manipulation:** Used `.strip()` to remove extra spaces, `.title()` to capitalize names, and `.isdigit()` to ensure the roll number only contains numbers.
* **F-Strings:** Used for clean and aligned text formatting in the final output.
* **Lists:** Created empty lists (`[]`) and used `.append()` to add data dynamically inside a loop.
* **List Methods:** Used built-in functions like `len()` for counting, `sum()` for total, `max()` for highest, `min()` for lowest, and `sorted(reverse=True)` for ranking.
* **Loops & Conditionals:** Used `for` loops to iterate through the lists and `if/else` statements for validation and logic building.

## Instructions to Run the Programs

1. Make sure Python 3 is installed on your computer.
2. Clone or download this repository to your local machine.
3. Open a terminal or command prompt inside the project folder.
4. To run the Result Card Generator, execute this command:
   ```bash
   python result_card_generator.py
   ```
5. To run the Class Marks Analyzer, execute this command:
   ```bash
   python class_marks_analyzer.py
   ```

## Sample Input and Output

### Sample Run: Task 1 (Result Card)
```text
Enter student's name:   ali raza  
Enter roll number (digits only): 1025
Enter marks for Math (0-100): 85
Enter marks for Science (0-100): 35
Enter marks for English (0-100): 70
Enter marks for Urdu (0-100): 65
Enter marks for Computer (0-100): 90

Result Card
Name: Ali Raza
Roll Number: 1025
Math: 85
Science: 35
English: 70
Urdu: 65
Computer: 90
Total Marks: 345 / 500
Percentage: 69.00%
Grade: Fail
Status: Fail 
(Note: Failed because Science marks are below 40)
```

### Sample Run: Task 2 (Class Analyzer)
```text
How many students are in the class? 2

Student 1
Enter student name: Ali
Enter marks (0-100): 85

Student 2
Enter student name: Sara
Enter marks (0-100): 45

Class Analysis Report
Class Average: 65.00

Highest Marks: 85
Achieved by:
Ali

Lowest Marks: 45
Achieved by:
Sara

Performance Summary
Passing Students: 1
Failing Students: 1

Students above class average:
Ali (85 marks)

Marks sorted from highest to lowest:
85
45
```
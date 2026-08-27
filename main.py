import csv
import os

name = input("Enter student name:")
subjects = ["Python", "Database", "Math", "English", "CS"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)
total_marks = sum(marks)  
average = total_marks / len(subjects)
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
result = "PASS" if average >= 40 else "FAIL"
print(f"Student Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")
file_name = "student_results.csv"
file_exists = os.path.exists(file_name)
with open(file_name,"a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            "Name",
            "Total Marks",
            "Average Marks", 
            "Grade", 
            "Result"
      ])
    writer.writerow([
        name,
        total_marks,
        average, 
        grade, 
        result
    ])
print("\nResult has been saved to student_results.csv") 
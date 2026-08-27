name = input("Enter student name:")
num_subject = int(input("Enter number of subjects: "))
toatl_marks = 0
for i in range(num_subject):
    grade_point = float(input(f"Enter grade point for subject {i+1}:v "))
    toatl_marks += grade_point
cgpa = toatl_marks / num_subject
print("\n--- Student Result ---")
print("Student Name:", name)
print("CGPA:", round(cgpa, 2))
# Step 1: Create a dictionary of student names and marks
students_marks = {
    "SK AZAD ALI": 85,
    "ROHAN MISHRA": 78,
    "AMIRUL RAHEMAN": 92,
    "GUIDO VAN RUSSOM": 88,
    "GAMES GOSLING": 76
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks or show a message if not found
if student_name in students_marks:
    print(f"{student_name}'s marks: {students_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
#####TASK 2###########################
#  Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

#  Extract the first five elements
first_five = numbers[:5]

#  Reverse the extracted elements
reversed_first_five = first_five[::-1]

#  Print both lists
print("Original List:",numbers)
print("First five elements:", first_five)
print("Reversed list:", reversed_first_five)

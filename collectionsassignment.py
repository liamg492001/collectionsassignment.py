# Function that determines letter grade based on numeric average
def calculate_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Input: Obtain student name
student_name = input("Enter student name: ")

# Input: Obtain 5 grades without using loops
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

# Store grades in a list
grades_list = [grade1, grade2, grade3, grade4, grade5]

# Calculate average without using loops
average_score = sum(grades_list) / len(grades_list)

# Determine the letter grade using the custom function
letter_grade = calculate_letter_grade(average_score)

# Output results
print()
print(student_name)
print(f"Average: {average_score:.1f}")
print(f"Letter Grade: {letter_grade}")

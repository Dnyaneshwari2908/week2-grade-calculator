# Name: Dnyaneshwari Shinde
# Project: Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures

# Function to calculate grade and comment
def calculate_grade(average):

    if average >= 90:
        return "A", "Excellent Performance!"
    
    elif average >= 80:
        return "B", "Very Good Work!"
    
    elif average >= 70:
        return "C", "Good Job. Improve More."
    
    elif average >= 60:
        return "D", "Needs Improvement."
    
    else:
        return "F", "Failed. Study Hard."


# Function to get valid marks
def get_valid_marks(subject):

    while True:

        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            else:
                print("Marks must be between 0 and 100!")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Main Program
print("=" * 60)
print("              STUDENT GRADE CALCULATOR")
print("=" * 60)

# Get number of students
while True:

    try:
        num_students = int(input("Enter number of students: "))

        if num_students > 0:
            break

        else:
            print("Please enter a positive number!")

    except ValueError:
        print("Invalid input! Enter whole numbers only.")


# Lists to store student data
student_names = []
student_results = []

# Collect student information
for i in range(num_students):

    print()
    print("-" * 40)
    print(f"Entering Details for Student {i + 1}")
    print("-" * 40)

    # Get valid student name
    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty!")
        name = input("Enter student name: ").strip()

    # Get marks
    math_marks = get_valid_marks("Math")
    science_marks = get_valid_marks("Science")
    english_marks = get_valid_marks("English")

    # Calculate average
    average = (math_marks + science_marks + english_marks) / 3

    # Calculate grade and comment
    grade, comment = calculate_grade(average)

    # Store data
    student_names.append(name)

    student_results.append({
        "math": math_marks,
        "science": science_marks,
        "english": english_marks,
        "average": average,
        "grade": grade,
        "comment": comment
    })


# Display Results
print()
print("=" * 60)
print("                    RESULTS SUMMARY")
print("=" * 60)

print(f"{'Name':<15} {'Average':<10} {'Grade':<10} Comment")
print("-" * 60)

for i in range(num_students):

    name = student_names[i]
    avg = student_results[i]["average"]
    grade = student_results[i]["grade"]
    comment = student_results[i]["comment"]

    print(f"{name:<15} {avg:<10.1f} {grade:<10} {comment}")


# Calculate class statistics
averages = []

for result in student_results:
    averages.append(result["average"])

class_average = sum(averages) / len(averages)

highest_average = max(averages)
lowest_average = min(averages)

highest_index = averages.index(highest_average)
lowest_index = averages.index(lowest_average)

# Display statistics
print()
print("=" * 60)
print("                  CLASS STATISTICS")
print("=" * 60)

print(f"Total Students   : {num_students}")
print(f"Class Average    : {class_average:.1f}")
print(f"Highest Average  : {highest_average:.1f} ({student_names[highest_index]})")
print(f"Lowest Average   : {lowest_average:.1f} ({student_names[lowest_index]})")


# Search feature
print()
search_name = input("Enter student name to search: ").strip()

found = False

for i in range(num_students):

    if student_names[i].lower() == search_name.lower():

        print()
        print("Student Found!")
        print("-" * 30)

        print(f"Name     : {student_names[i]}")
        print(f"Average  : {student_results[i]['average']:.1f}")
        print(f"Grade    : {student_results[i]['grade']}")
        print(f"Comment  : {student_results[i]['comment']}")

        found = True
        break

if not found:
    print("Student not found!")


# Save results to file
file = open("results_sample.txt", "w")

file.write("STUDENT RESULTS\n")
file.write("=" * 40 + "\n")

for i in range(num_students):

    file.write(f"Name: {student_names[i]}\n")
    file.write(f"Average: {student_results[i]['average']:.1f}\n")
    file.write(f"Grade: {student_results[i]['grade']}\n")
    file.write(f"Comment: {student_results[i]['comment']}\n")
    file.write("-" * 40 + "\n")

file.close()

print()
print("=" * 60)
print("Results saved successfully in results_sample.txt")
print("Thank you for using the Grade Calculator!")
print("=" * 60)
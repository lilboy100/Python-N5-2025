total_scores = 0
number_of_students = int(input("Enter the number of students in the class: "))

for i in range(number_of_students):
    score = int(input(f"Enter the test score for student {i + 1}: "))
    total_scores += score

average = total_scores / number_of_students
print("The average test mark is:", round(average, 1))

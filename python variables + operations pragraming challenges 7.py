# Task 7: Library Fine Calculator
# Write a program that:

# Stores the number of days a book is overdue
# The fine is £0.50 per day
# If the fine exceeds £5, add an additional £2 processing fee
# Calculate and display the total fine

days_overdue = 7.00
fine_per_day = 0.50 
proccesing_fee = 2.00

total_fine = (days_overdue * fine_per_day)
if total_fine > 5:
    total_fine = total_fine + 2
print(total_fine)
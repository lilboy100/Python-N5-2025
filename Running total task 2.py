#task 2 
 #create a program that asks the user to input 5 test scores and calculates the running total after each input.


total = 0

for index in range(5):

savings = float(input("Enter monthly savings amount(£): "))

total = total + savings 

print(total)

print("your final savings amount after one year is", total)
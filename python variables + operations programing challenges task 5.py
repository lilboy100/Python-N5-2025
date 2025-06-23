#Task 5: Pizza Party Calculator
#Write a program that:

#Stores the number of students in the class
#Stores that each pizza serves 8 people
#Calculate how many pizzas are needed (you may need to round up)
#If each pizza costs £12, calculate the total cost
#Display the number of pizzas needed and the total cost

students = int(input("Enter number of students"))

pizza = 8

pizzas_needed = (students / pizza)

totalcost = (pizzas_needed*12)
print(pizzas_needed)
print("Your total cost is £"+str(totalcost))
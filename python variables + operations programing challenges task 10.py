#Task 10: Energy Bill Calculator
#Create a program that calculates an electricity bill:

#Store that each unit costs £0.15
#Store the meter reading at the start and end of the month
#Calculate units used (i.e end reading - start reading)
#Calculate the cost of the units used
#Add a standing charge of £12 to the total cost
#Calculate and display the total bill

each_unit = 0.15

start_reading = 100
end_reading = 250 

units_used = (end_reading - start_reading)
cost_of_units = (each_unit * units_used)

standing_charge = 12

total_bill = (cost_of_units + standing_charge)

print("total bill",total_bill)



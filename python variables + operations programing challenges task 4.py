#Task 4: Classroom Supplies
#Create a program that manages classroom supplies:

#Start with 50 pencils in stock
#15 pencils are given out to students
#25 new pencils arrive as a delivery
#Calculate and display the final stock level

pencils = 50 
pencils_out = 15
pencils_in = 25

final_stock = pencils - pencils_out + pencils_in
print (final_stock)
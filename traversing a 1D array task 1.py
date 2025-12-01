#Task 1 - Create a program that contains an array of 7 daily temperatures. 
#Traverse the 1D array to calculate and display the average temperature.

temperatures = [12, 23, 30, 16, 15, 19]

total_temp = 0
for temp in daily_temp:
 total_temp += temp

average_temp = total_temp / len(daily_temp)

print("average temp for the week:", round(average_temp, 2), "o2")
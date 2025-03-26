temps = []

for index in range(5):
    temp = float(input("Enter temprature between -20 and 50c: "))
    while temp < -20 or temp > 50:
        temp = float(input("invalid input, enter a temprature between -20 and 50c: "))
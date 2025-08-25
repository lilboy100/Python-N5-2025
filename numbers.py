while True:
  number = int(input("Please enter a number between 25 and 75: "))
  if number < 25 or number > 75:
    print("That is an invalid number")
  else:
    print("That is a valid number")
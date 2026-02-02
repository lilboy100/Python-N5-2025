import random

# set up all variables
mysteryFruit = ["apple" "bannana" "blueberry" "kiwi" "mango" "oragne" "peach" "paineaple" "rasberry" "strawberry"]
userFruits = []
counter = 0
decision = "yes"

# loop until all fruit added
while decision == "yes" and counter <6:
    userInput = input("please enter the fruit name")
    fruitLength = len(userInput)
    while fruitLength <4:
        print("incorect fruit name length")
        userInput = input("please enter the fruit name")
        fruitLength = len(userInput)
    # must be valid
    userFruits.append(userInput) # adds userInput to userFruits array
    counter = counter +1
    decision = str(input("do you wnat to enter another fruit"))

# generate mystery fruit and show all other fruits added
number = random.randint(0,9)
for i in range(counter):
    print("the fruits you entered where",userfruits[i])
print("the mistery fruit is", mysteryFruit[number])

# add 1 to counter because mystery fruit
counter = counter + 1

# show what type of drink it should be
if counter <3:
    print("milkshake")
elif counter ==3 or counter == 4:
    print("smoothie")
else:
    print("fruit juice")
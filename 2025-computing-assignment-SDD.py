mysteryFruit = ["apple" "bannana" "blueberry" "kiwi" "mango" "oragne" "peach" "paineaple" "rasberry" "strawberry"]
userFruits = [""]
counter = 0
decision = ("yes")
while decision = yes and counter <6:
    userFruits = int(input("please enter the fruit name"))
    fruitLength = len(userFruits)
    while fruitLength <4:
        print("incorect fruit name length")
        userFruits = int(input("please enter the fruit name"))
        fruitLength = len(userFruits)
    counter = counter +1
    decision = str(input("do you wnat to enter another fruit"))
number = random.randit(0,9)
for i in range(counter):
    print("the fruits you entered where",userfruits[i+1])
print("the mistery fruit is", mysteryFruit[number])
if counter <3
    print("milkshake")
    if counter =3 or 4
        print("smoothie")
        else print("fruit juice")
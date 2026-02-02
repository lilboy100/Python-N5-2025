import random
endings = ["ing", "end", "axe", "gex", "goh"]
num_students = int(input("enter number of students: "))
for i in range(num_students):
    ok = False
    while ok != True:
        name = input("Enter the first three letters of the student's name: ")

        if len(name) != 3: 
            print("Enter! you must exactly 3 charactors.")
        else: 
            ok = True
    random_number = random.randint(1, 5)
    username = name + endings[random_number - 1]
    print("Generated username:", username)
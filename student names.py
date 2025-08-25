names = []

for i in range(10):
    name = input(f"Enter the first name of student {i + 1}: ")
    names.append(name)

print("\nThe names of the students are:")
for name in names:
    print(name)
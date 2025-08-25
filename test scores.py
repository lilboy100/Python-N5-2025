testScores = [0] * 20  

for i in range(20):
    score = int(input("Enter test score for student " + str(i+1) + ": "))
    
    if score >= 0 and score <= 100:
        testScores[i] = score
    else:
        print("Error: Score must be between 0 and 100.")


print("Test Scores:")
for i in range(20):
    print("Student", i+1, "Score:", testScores[i])
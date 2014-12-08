# Assigning Grades
# Su Min Kim
# 11-4

# getting input
grades = input ("Enter the scores on one line: ")
grades = grades.split()
best = int(max(grades))

# assigning i for student number
i = 0

# for loop to loop through grades
for g in grades:
    g = int(g)

    # assigning the letter grade
    if g >= (best - 10):
        letter = "A"
    elif g >= (best - 20):
        letter = "B"
    elif g >= (best - 30):
        letter = "C"
    elif g >= (best - 40):
        letter = "D"

    # print result, increase student number
    print("Student ",i , "score is ", g, "and grade is ", letter)
    i += 1

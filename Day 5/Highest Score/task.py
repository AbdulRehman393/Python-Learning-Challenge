# Highest Score programs , Python sum and max built-in function and  finding sum and max through for loops.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)
print(total_score)

Sum = 0
for scores in student_scores:
    Sum += scores
print(Sum)

max_number = max(student_scores)
print(max_number)
maximum_number = student_scores[0]
for Max in student_scores:
    if Max > maximum_number:
        maximum_number = Max

print(f"The Maximum Number is: {maximum_number} ")
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max=0
for score in student_scores:
  if score > max:
    max= score #max will store a new value to compare with the next score in the score list
print(f"The highest score in the class is: {max}")

name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Display table
print("\n--- Result ---")
print(f"Name     : {name}")
print(f"Total    : {total}")
print(f"Average  : {average:.2f}")
print(f"Grade    : {grade}")

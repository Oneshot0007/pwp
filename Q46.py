print("Enter marks for 5 subjects:")
marks = []

# Input marks
for i in range(1, 6):
    mark = float(input(f"Subject {i}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 5

# Determine grade based on average
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
    grade = "F (Fail)"

# Display result
print("\n--- Result ---")
print(f"Total Marks  : {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade        : {grade}")

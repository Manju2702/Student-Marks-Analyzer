import matplotlib.pyplot as plt

students = {}

def safe_int(prompt, default=None):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

def safe_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number (e.g. 78 or 78.5).")

num_students = safe_int("How many students? ")

for s in range(num_students):
    name = input(f"\nEnter name of student {s+1}: ").strip() or f"Student_{s+1}"
    num_subs = safe_int(f"How many subjects for {name}? ")
    
    marks_dict = {}
    if num_subs == 0:
        print("Warning: zero subjects — student will have empty marks.")
    for i in range(num_subs):
        subj = input(f"  Enter subject {i+1}: ").strip() or f"Subject_{i+1}"
        mark = safe_float(f"  Enter marks in {subj}: ")
        marks_dict[subj] = mark
    
    students[name] = marks_dict

print("\nStudents Data:")
print(students)

def analyze_marks(marks):
    if not marks:
        return 0, 0.0, (None, None), (None, None)
    total = sum(marks.values())
    avg = total / len(marks)
    high_sub = max(marks, key=marks.get)
    low_sub = min(marks, key=marks.get)
    return total, avg, (high_sub, marks[high_sub]), (low_sub, marks[low_sub])

print("\n--- Student Marks Report ---")
for name, marks in students.items():
    total, avg, high, low = analyze_marks(marks)
    print(f"\nStudent: {name}")
    print(f"Subjects & Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
    if high[0] is not None:
        print(f"Highest: {high[1]} in {high[0]}")
        print(f"Lowest : {low[1]} in {low[0]}")
    else:
        print("No subject marks available.")

if students:
    name = input("\nEnter student name to plot marks (or press Enter to skip): ").strip()
    if name:
        if name in students and students[name]:
            marks = students[name]
            plt.bar(marks.keys(), marks.values())
            plt.title(f"{name} - Marks Chart")
            plt.xlabel("Subjects")
            plt.ylabel("Marks")
            plt.ylim(0, max(marks.values()) + 10)
            plt.show()
        elif name in students:
            print("Student has no marks to plot.")
        else:
            print("Student not found!")
else:
    print("No students available to plot.")

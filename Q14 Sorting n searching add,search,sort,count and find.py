students = []

# Add students
n = int(input("How many students: "))
for i in range(n):
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students.append([sid, name, marks])

# Search by ID
key = input("Enter ID to search: ")
found = False
for s in students:
    if s[0] == key:
        print("Found:", s)
        found = True
        break
if not found:
    print("Not found")

# Sort by marks
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][2] < students[j][2]:     # compare marks
            temp = students[i]
            students[i] = students[j]
            students[j] = temp

print("Sorted by marks:", students)

# Count fails (marks < 40)
fail = 0
for s in students:
    if s[2] < 40:
        fail = fail + 1

print("Fail count:", fail)

# Top 5
print("Top 5:")
for i in range(min(5, len(students))):
    print(students[i])
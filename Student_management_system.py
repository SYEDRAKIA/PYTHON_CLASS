students = []   # list of dictionaries


def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    student = {
        "id": sid,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def search_by_id():
    sid = int(input("Enter Student ID to search: "))

    for s in students:
        if s["id"] == sid:
            print("Student Found:")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            return

    print("Student not found.")


def sort_by_marks():
    students.sort(key=lambda x: x["marks"], reverse=True)
    print("Students sorted by marks (descending).")

    for s in students:
        print(s["id"], s["name"], s["marks"])


def count_fail():
    count = 0
    for s in students:
        if s["marks"] < 40:
            count += 1

    print("Number of failed students:", count)


def top_five():
    students.sort(key=lambda x: x["marks"], reverse=True)

    print("Top 5 Students:")
    for s in students[:5]:
        print(s["id"], s["name"], s["marks"])


while True:
    print("""
---- Student Result Management ----
1. Add Student
2. Search by ID
3. Sort by Marks
4. Count Failed Students
5. Find Top 5 Students
6. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_by_id()
    elif choice == "3":
        sort_by_marks()
    elif choice == "4":
        count_fail()
    elif choice == "5":
        top_five()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
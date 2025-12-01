print("1. Issue a Book")
print("2. Return a Book")
print("3. Check List of Books")
print("4. View Available Books")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Book Issued Successfully.")

elif choice == 2:
    days = int(input("Enter number of days you kept the book: "))
    fine = days // 15   # Rs 1 for every 15 days
    print("Book Returned.")
    print("Fine =", fine)

elif choice == 3:
    print("List of Books:")
    print("Maths, Science, English, Computer")

elif choice == 4:
    print("Available Books:")
    print("Maths, Science, English, Computer")

else:
    print("Invalid Choice!")
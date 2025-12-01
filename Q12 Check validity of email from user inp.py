mail = input("Enter Gmail ID: ")

if mail.endswith("@gmail.com") and " " not in mail:
    name = mail.replace("@gmail.com", "")

    if len(name) >= 1:
        print("Valid Gmail ID")
    else:
        print("Invalid Gmail ID")
else:
    print("Invalid Gmail ID")
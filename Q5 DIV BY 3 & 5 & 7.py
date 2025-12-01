numb = int(input("Enter a number: "))

if (numb % 3 == 0 and numb % 5 == 0 and numb % 7 == 0):
    print(numb, "is a div by 3, 5 and 7")
else:
    print(numb, "is not div by 3, 5 and 7")
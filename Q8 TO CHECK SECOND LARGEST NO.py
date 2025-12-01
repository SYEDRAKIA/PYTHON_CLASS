num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            second= num2
        else:
            second= num3
    else:
        second= num1
else:

    if num2 > num3:
        if num1 > num3:
            second= num1
        else:
            second= num3
    else:
        second= num2
        print(second)
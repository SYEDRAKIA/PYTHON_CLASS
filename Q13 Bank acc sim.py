bal = 0

print("1. deposit money")
print("2. withdraw money")
print("3. check balance")

choice = int(input("enter choice: "))

if choice == 1:
    amt = int(input("enter amount to deposit: "))
    bal = bal + amt
    print("money deposited")
    print("curr bal:", bal)

elif choice == 2:
    amt = int(input("enter amount to withdraw: "))
    if amt <= bal:
        bal = bal - amt
        print("money withdrawn")
        print("curr bal:", bal)
    else:
        print("not enough money")

elif choice == 3:
    print("your bal:", bal)

else:
    print("invalid choice")
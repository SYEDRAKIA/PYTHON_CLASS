n = int(input("Enter no of terms: "))

a=0
b=1

print("Fibbonacci seies:")
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
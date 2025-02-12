arr=list(map(int,input("enter the elements of array: ").split()))
k=int(input("Enter the number of rotations:"))
k=k%len(arr)
rotated=arr[k:]+arr[:k]
print("Rotated array is: ")
print(rotated)
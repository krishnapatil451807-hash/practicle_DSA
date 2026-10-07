array=[]
n=int(input("enter the size "))
for i in range(n):
    element=int(input(f"enter the element {i} : "))
    array.append(element)
unique=[]
for item in array:
    if item not in unique:
        unique.append(item)
print("unique element are : ",unique)
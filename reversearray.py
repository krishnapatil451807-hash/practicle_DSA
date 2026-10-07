array=[]
n=int(input("enter the size of an array : "))
for i in range(n):
    element=int(input(f"enter element no . {i} : "))
    array.append(element)
for i in range((len(array)-1),-1,-1):
    print(array[i], end=" ")
array=[]
n=int(input("enter the size of the array :"))
for i in range(n):
    element=int(input(f"enter the element of array {i} :"))
    array.append(element)
num=int(input("enter a number for search"))
for idx,i in enumerate(array):
    if i==num:
        print("the num found at ",idx)
        break

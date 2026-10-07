array=[]
n=int(input("enter size of array ="))
for i in range (n):
    element=int(input(f"enter the element {i+1} :"))
    array.append(element)
sum=0
for i in array:
    sum+=i
print(sum)
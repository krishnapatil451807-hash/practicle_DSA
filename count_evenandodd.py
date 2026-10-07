array=[]
n=int(input("enter the size of array :"))
for i in range (n):
    element=int(input(f"enter the array element {i} :"))
    array.append(element)
counter={
    "even":0,
    "odd":0
}
for i in array:
    if i%2==0:
        counter["even"]+=1
    else:
        counter["odd"]+=1
print("counter :",counter)
array=[]
n=int(input("enter the array size "))
for i in range (n):
    element=int(input(f"enter the element {i} :"))
    array.append(element)
small=array[0]
large=array[0]
for items in array:
    if items<small:
        small=items
    if items>large:
        large=items
s_small=array[0]
s_large=array[0]
for item in array:
    if item<s_small and item>small:
        s_small=item
    if item<large and item>s_large:
        s_large=item
print("smallest :",small)
print("largest element :",large)
print("second_small :",s_small)
print("second_large :",s_large)
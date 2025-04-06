def binary_sort(sorted, length, key):
    start = 0
    end = length-1
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted[mid]:
            print("Name ",key, " is present at index: ", mid)
            return -1
        elif key < sorted[mid]:
            end = mid - 1
        elif key > sorted[mid]:
            start = mid + 1
    print("Element", key ,"not found in the list!")
    return -1
 
lst = []
 
size = int(input("Enter number of list: "))
 
for n in range(size):
    name = str(input("Enter any name: "))
    lst.append(name)
 
lst.sort()
print("__________________________________________________________")
print("The list will be sorted . . .")
print("The sorted list is:", lst)
 
x = str(input("\nEnter the name to search: "))
 
binary_sort(lst, size, x)

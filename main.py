arr1=[10,20,30,40,50,60,70,80,90,100,110]
arr2=[23,34,12,93,23,45,39,48,8,1,5,2,77]

def array_add(arr1):
    print("This is current arry : " , arr1)
    pos = int(input("Enter element Position :"))
    value = int(input("Enter Element :"))
    if (pos < len(arr1)):
        arr1.insert(pos, value)
    else:
        print("Invalid Position")
    print("This is New Array : ", arr1)
def leaner_search(arr1):
    target=int(input(f"Enter your Target : "))
    a=0
    for i in arr1:
        if (i == target):
            print(f"Yeah! Found...{target}  is Located in  { arr1.index(target)}")
            a = 1
            break
    if (a!=1):
        print(f"Target Not Found !")
def binary_search(arr1):
    target=int(input("Enter your target number : "))
    low,a=0,0
    high=len(arr1)-1
    while low <=high:
        mid =(low+ high) // 2
        if arr1[mid] == target:
            print(f"Found {target} at {mid}")
            a=a+1
            break
        if arr1[mid] > target: # Search in the left half
            high = mid - 1
        if arr1[mid] < target: # Search in the right half
            low = mid + 1
    if a==0:
        print(f"Sorry... {target} Not found in {arr1}")
def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            first_half = arr[:mid]
            second_half = arr[mid:]
            # Using recursion
            merge_sort(first_half)
            merge_sort(second_half)
            i = j = k = 0
            #Merge the two halves
            while i < len(first_half) and j < len(second_half):
                if first_half[i] < second_half[j]:
                    arr[k] = first_half[i]
                    i += 1
                else:
                    arr[k] = second_half[j]
                    j += 1
                k += 1
            #Copy remaining elements of first_half
            while i < len(first_half):
                arr[k] = first_half[i]
                i += 1
                k += 1
            #Copy remaining elements of second_half
            while j < len(second_half):
                arr[k] = second_half[j]
                j += 1
                k += 1
def quick_sort(arr):
    print("hello")

#array_add(arr1)
#leaner_search(arr1)
#binary_search(arr1)
merge_sort(arr2)
#quick_sort(arr2)
print(arr2)




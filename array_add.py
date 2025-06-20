def array_adding(arr1):
    print("This is current arry : " , arr1)
    pos = int(input("Enter element Position :"))
    value = int(input("Enter Element :"))
    if (pos < len(arr1)):
        arr1.insert(pos, value)
    else:
        print("Invalid Position")
    print("This is New Array : ", arr1)
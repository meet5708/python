arr = bytearray([10,20,30,40,60])

for i in arr :
    print(i)
print("array at index 4 = ",arr[4])

arr[4] = 50
print("modified number at index 4 = ",arr[4])

for i in arr :
    print(i)
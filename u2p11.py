
num = list(range(1, 11))
print("Original List:", num)
num.append(11)
print("After Appending 11:", num)

num[4] = 99
print("After Updating 5th Element (index 4):", num)

del num[2]
print("After Deleting Element at Index 2:", num)

num.remove(99)
print("After Removing Value 99:", num)

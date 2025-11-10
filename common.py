
l1 = [10, 20, 30, 40, 50]
l2 = [20, 40, 50, 60, 70]

common = []
for i in l1:
    if i in l2:
        common.append(i)

non_common = []
for i in l1+l2:
    if (i not in l1)or( i not in l2):
        non_common.append(i)


print("List 1:", l1)
print("List 2:", l2)
print("Common elements:", common)
print("Non-common elements:", non_common)

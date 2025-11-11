lis=[
    [1,2,3,4],
    [5,4,3,2,1]
    ]
print(lis)
for row in lis:
    print(row)

for row in lis:
    for element in row:
        print(element,end=" ")
        print()
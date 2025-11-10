
num = [10, 20, 30, 40, 50, 60]
for i in num :
    print(i)

search = int(input("Enter number to search: "))

for i in num:
    if i == search:
        print(f"{search} found in the list!")
        break
else:
    
    print(f"{search} not found in the list.")

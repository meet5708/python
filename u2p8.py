def pos(a,b):
    print(a+b)

a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))

pos(a,b)

def key(name,a,b):
    print(a+b,name)

key(b=12,a=43,name="meet")

def de(a,b,c=0):
    print(a+b,c)

a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
de(a,b)

def var(*abc):
    print(abc)
var(2,"Meet")
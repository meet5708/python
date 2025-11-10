while True:
    print("\n===== MENU =====")
    print("1. Find Area of Circle")
    print("2. Find Area of Triangle")
    print("3. Find Area of Square")
    print("4. Find Simple Interest")
    print("5. Exit")
    
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            r = float(input("Enter radius of the circle: "))
            area = 3.14159 * r * r
            print(f"Area of Circle = {area:.2f}")
        
        case 2:
            
            base = float(input("Enter base of triangle: "))
            height = float(input("Enter height of triangle: "))
            area = 0.5 * base * height
            print(f"Area of Triangle = {area:.2f}")
        
        case 3:
           
            l = float(input("Enter side of the square: "))
            area = l * l
            print(f"Area of Square = {area:.2f}")
        
        case 4:
           
            p = float(input("Enter Principal amount: "))
            r = float(input("Enter Rate of Interest: "))
            t = float(input("Enter number of years: "))
            si = (p * r * t) / 100
            print(f"Simple Interest = {si:.2f}")
        
        case 5:
            print("Exiting program... Thank you!")
            break
        
        case _:
            print("Invalid choice! Please enter a number between 1 and 5.")

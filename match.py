#Tuple

x,y= int(input("Enter the value of x:")), int(input("Enter the value of y:"))
t = (x,y)

match t:
    case (x,y) if x > 0 and y > 0:
        print("Both x and y are positive numbers.")
    case (x,y) if x < 0 and y < 0:
        print("x and y is negative.")
    case (x,y) if x > 0 and y < 0:
        print("x is positive and y is negative.")
    case (x,y) if x < 0 and y > 0:
        print("x is negative and y is positive.")
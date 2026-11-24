load = float(input("Enter the load in kg\n "))
water = float(input("Enter the water level percentage\n "))
if load <=0:
    print("Invalid Load")
elif load >= 8:
    print("Overload")
elif water <=20:
    print("Low Water level ")
else:
    print("Wash can start")

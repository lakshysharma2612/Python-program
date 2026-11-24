water = float(input("Enter the water level percentage\n "))
if water <=20:
    print("Low Water level ")
elif water >= 21 and water <= 80:
    print("Normal Water level ")
elif water >= 81 and water <= 100:
    print("Tank Almost Full")
else:
    print("Invalid Reading.")

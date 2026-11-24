battery = float(input("Enter the battery percentage\n "))
charging = input("Is the laptop connected to Charger? (yes/no)\n ")
if charging == "yes":
    print("Laptop is charging") 
elif charging == "no":
    if battery > 0 and battery <= 10:
        print("critical battery level")
    elif battery >= 10 and battery <= 30:
        print("Enable Battery Saver Mode")
    elif battery <= 31:
        print("Battery normal")
    else:
        print("Invalid Battery percentage.")
attendance = float(input("Enter your attendance percentage\n "))
project = int(input("Enter the project completed by you \n "))
if attendance >= 90 and project >= 3:
    print("Employee incentive is 5000")
elif attendance >= 74 and project >= 2:
    print("Employee incentive is 2000")
else:
    print("No incentive awarded")
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# d=int(input("Enter a number: "))
# e=int(input("Enter a number: "))
# f=int(input("Enter a number: "))
# g=int(input("Enter a number: "))
# h=int(input("Enter a number: "))
# i=int(input("Enter a number: "))
# j=int(input("Enter a number: "))
sum=0
for i in range(10):
    num=int(input("Enter a number: "))
    if num<0:
        continue
    else:
        sum+=num
print("The sum of positive numbers is:", sum)
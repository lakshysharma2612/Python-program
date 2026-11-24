#WAP to check a number is armstrong or not
n=int(input("Enter a number: "))
temp=n
sum=0
for i in range (n):
    digit=n%10
    sum+=digit**3
    n//=10
if sum==temp:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
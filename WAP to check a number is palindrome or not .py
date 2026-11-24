12#WAP to check a number is palindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reversed number:", rev)
if num == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    
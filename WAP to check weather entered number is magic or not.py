#WAP to check whether entered number is magic no. or not
num  = int(input("Enter a number: "))
n = num

while n > 9:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    n = sum

if num > 0 and n == 1:
    print(num, "is a magic number")
else:
    print(num, "is not a magic number")
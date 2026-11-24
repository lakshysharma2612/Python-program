A=float(input("Enter Your First Number\n"))
B=float(input("Enter Your Second Number\n"))
C=float(input("Enter Your Third Number\n"))
if A<B and A<C:
    print("The Smallest Number",A)
elif B<A and B<C:
    print("The Smallest Number",B)
elif C<A and C<B:
    print("The Smallest Number",C)
else:
    print("All Numbers are Equal Number")
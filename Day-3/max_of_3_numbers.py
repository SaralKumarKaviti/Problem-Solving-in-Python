a=int(input("Enter a Value:"))
b=int(input("Enter b Value:"))
c=int(input("Enter c Value:"))

if a>b and a>c:
    print("The maximum value of a is {}".format(a))

elif b>c and b>a:
    print("The maximum value of b is {}".format(b))

else:
    print("The maximum value of c is {}".format(c))

print("Select your respective units...")
print("1.centimetre")
print("2.metre")
print("3.millimetre")
print("4.kilometre")

choice= input("Enter choice(1/2/3/4)"
unit1=input("Enter units from converting:")
unit2=input("Enter units to coverting:")
number=float(input("Enter value:"))

if choice == '1':
    if unit1 == 'centimetre' and unit2 == 'metre':
        value=number/100
        print("Metre value is {}".format(value))
    elif unit1 == 'metre' and unit2 == 'centimetre':
        value=number*100
        print("Centimetre value is {}".format(value))
    else:
        print("Please enter the valid units...")

elif choice == '2':
    if unit1 == 'millimetre' and unit2 == 'centimetre':
        value=number/10
        print("Millimetre value is {}".format(value))
    elif unit1 == 'centimetre' and unit2 == 'millimetre':
        value=number*10
        print("Centimetre value is {}".format(value))
    else:
        print("Please enter the valid units...")

elif choice == '3':
    if unit1 == 'millimetre' and unit2 == 'metre':
        value=number/1000
        print("Millimetre value is {}".format(value))
    elif unit1 == 'metre' and unit2 == 'millimetre':
        value=number*1000
        print("Metre value is {}".format(value))
    else:
        print("Please enter the valid units...")
    
elif choice == '4':
    if unit1 == 'kilometre' and unit2 == 'metre':
        value=number*1000
        print("Kilometre value is {}".format(value))
    elif unit1 == 'metre' and unit2 == 'kilometre':
        value=number/1000
        print("Metre value is {}".format(value))
    elif unit1 == 'millimetre' and unit2 == 'kilometre':
        value=number/1000000    
    else:
        print("Please enter the valid units...")


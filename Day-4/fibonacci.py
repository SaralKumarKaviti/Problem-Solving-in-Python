num=int(input("Enter the Range Number:"))
i=0
first_value=0
second_value=1

while i<num:
    if i<=1:
        next_value=i
    else:
        next_value=first_value + second_value
        first_value = second_value
        second_value=next_value
    print(next_value)
    i=i+1
        

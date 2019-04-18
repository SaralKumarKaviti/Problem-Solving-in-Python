start=int(input("Enter start value:"))
end=int(input("Enter end value:"))
print("The range of prime numbers between {} and {} are:".format(start,end))

for num in range(start,end):
    end=end+1
    if num>1:
        for i in range(2, num):
            if(num % i)==0:
                break
        else:
            print(num)

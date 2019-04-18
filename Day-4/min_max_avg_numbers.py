print("Select your option...")
print("1.maximum")
print("2.minimum")
print("3.average")

choice=input("Choice your 1/2/3:")

if choice=='1':
    print("Maximum number....")
    list1=[]
    n=int(input("Enter number of elements in list:"))
    for i in range(1,n+1):
        elements=int(input("Enter elements:"))
        list1.append(elements)
    print("Largest element is:",max(list1))

elif choice=='2':
    print("Minimum number....")
    list1=[]
    n=int(input("Enter number of elements in list:"))
    for i in range(1,n+1):
        elements=int(input("Enter elements"))
        list1.append(elements)
    print("Largest element is:",min(list1))
elif choice=='3':
    print("Average number....")
    sum=0
    list1=[]
    n=int(input("Enter number of elements in list:"))
    for i in range(1,n+1):
        elements=int(input("Enter elements"))
        list1.append(elements)
        sum=sum+i
    avg=sum/len(list1)
    print("Sum of elements",sum)
    print("Average of list elemrnts",avg)
    
  
    
    

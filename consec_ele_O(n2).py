#ar=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
ar=[int(x) for x in input("Enter the integers sep by commas:\n").split(",")]
no=int(input("Enter how many consecutive elements to check:\n"))
temp=min(ar)
if(len(ar)>2):
    for i in range(len(ar)-(no-1)):
        s=sum(ar[i:i+no])
        if(s>temp):
            temp=s
    print("Sum is:",temp)
else:
    try:
       raise Exception()
    except Exception:
        print("enter number of elements>=3")

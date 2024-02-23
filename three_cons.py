#ar=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2] ar=[1,2,3,4]
ar=[int(x) for x in input("Enter the integers sep by commas:\n").split(",")]
temp=min(ar)
if(len(ar)>2):
    for i in range(len(ar)-2):
        if(ar[i]+ar[i+1]+ar[i+2]>temp):
            temp=ar[i]+ar[i+1]+ar[i+2]
            a=ar[i]
            b=ar[i+1]
            c=ar[i+2]
    print("Sum is:",temp,"Elements are:",a,b,c)
else:
    try:
       raise Exception()
    except Exception:
        print("enter number of elements>=3")





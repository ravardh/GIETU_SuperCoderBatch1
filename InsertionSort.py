def insertionSort(n):
    for i in range(0,len(n)):
        for j in range(i,0,-1):
            if n[j-1]>n[j]:
                n[j-1],n[j]=n[j],n[j-1]
        print(n)
n=eval(input("Enter a list of elements for sorting: "))
insertionSort(n)
print("After Sorting:",n)


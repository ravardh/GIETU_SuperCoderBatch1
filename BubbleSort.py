def bubbleSort(n):
    for i in range(0,len(n)):
        for j in range(0,len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
n=eval(input("Enter a list of elements for sorting: "))
bubbleSort(n)
print("After Sorting:",n)

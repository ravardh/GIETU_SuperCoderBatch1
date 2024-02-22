def selectionSort(n):
    for i in range(len(n)):
        min_index=i
        for j in range(i+1,len(n)):
            if n[min_index]>n[j]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
n=eval(input("Enter a list of elements for sorting: "))
selectionSort(n)
print("After Sorting:",n)
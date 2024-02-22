def InsertionSort(a):
  
    for i in range(1, len(a)):
  
        temp = a[i]
  
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp
       
a = [62, 26, 122, 8, 52]
InsertionSort(a)
print(a)



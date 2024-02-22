def Selection(arr):
    n=len(arr)
    for i  in range(n):
        min_index = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
            arr[i],arr[min_index] = arr[min_index],arr[j]
print(Selection([-2, 45, 0, 11, -9,88,-97,-202,747]))




n=int(input("Enter the number of elements:"))
list_1 = []
for i in range(n):
    m=int(input())
    list_1.append(m)
print(list_1)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
bubble_sort(list_1)

print("Sorted array:", list_1)
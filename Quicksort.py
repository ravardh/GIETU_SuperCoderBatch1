#QUICK_SORT algorithm
def find(arr, S, E):
    p = arr[E]
    i = S
    j = S - 1
    for i in range(S, E):
        if arr[i] < p:
            j = j + 1
            arr[i], arr[j] = arr[j], arr[i]
    j = j + 1
    arr[j], arr[E] = arr[E], arr[j]
    return j

def quicksort(arr, S, E):
    if S < E:
        pi = find(arr, S, E)
        quicksort(arr, S, pi - 1)
        quicksort(arr, pi + 1, E)

if __name__ == '__main__':
    arr = [4, 8, 2, 3, 7, 5, 1, 9, 6]
    quicksort(arr, 0, len(arr) - 1)
print(arr)
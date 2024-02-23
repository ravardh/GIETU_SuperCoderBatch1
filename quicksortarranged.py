def partition(ar, S, E):
    pivot = ar[E]
    i = S - 1
    for j in range(S, E):
        if ar[j] < pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i + 1], ar[E] = ar[E], ar[i + 1]
    return i + 1

def quickSort(ar, S, E):
    if S < E:
        pi = partition(ar, S, E)
        quickSort(ar, S, pi - 1)
        quickSort(ar, pi + 1, E)

if __name__ == '__main__':
    ar = [4, 8, 2, 3, 7, 5, 1, 9, 6]
    quickSort(ar, 0, len(ar) - 1)
    print(ar)

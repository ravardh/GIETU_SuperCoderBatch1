# Selection Sort algorithm in Python
def selectionSort(array, size):
	for s in range(size):
		min_idx = s
		for i in range(s + 1, size):
			if array[i] < array[min_idx]:
				min_idx = i
		(array[s], array[min_idx]) = (array[min_idx], array[s])
data = [ 6,7,9,3,19,39,69,67,45, ]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order is :')
print(data)

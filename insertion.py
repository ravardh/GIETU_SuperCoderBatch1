
n=int(input("Enter the number of elements:"))
list1=[]
for i in range(n):
    m=int(input())
    list1.append(m)
print(list1)

def insertion_sort(list1):

        for i in range(1, len(list1)):
            a = list1[i]
            j = i - 1
            while j >= 0 and a < list1[j]:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j + 1] = a
        return list1


print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))
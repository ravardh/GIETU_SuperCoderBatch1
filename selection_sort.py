list1 = [ 10 , 9 , 8 , 6, 7, 5,4]
for i in range (len(list1)):
    min_index =i
    for j in range (i+1 , len(list1)):
        if list1[min_index] > list1[j]:
            min_index = j
            
    list1[i],list1[min_index] = list1[min_index], list1[i]
print(list1)

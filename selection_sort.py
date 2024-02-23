def selection_sort(li):
 for i in range(len(li)):
    for j in range(i+1,len(li)-1):
        if(li[i]>li[j]):
           li[j],li[i]=li[i],li[j]
           
 print(li)
        



li=[7,5,2,3,9]
selection_sort(li)

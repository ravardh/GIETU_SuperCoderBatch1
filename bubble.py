def bubble (list):  
     for i in range(0,len(list)-1):  
        for j in range(len(list)-1):  
            if(list[j]>list[j+1]):   
                 list[j],list[j+1] = list[j+1], list[j]  
     return list 
list = [5, 3, 8, 6, 7, 2]  
print(" sorted list is: ", bubble (list))  
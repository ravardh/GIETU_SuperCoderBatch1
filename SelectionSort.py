Array = [38, 18, 42, 28, 4]
  
for i in range(len(Array)):
          
    min_indx = i
    for j in range(i+1, len(Array)):
    
        if Array[min_indx] > Array[j]:
            min_indx = j
              
    Array[i], Array[min_indx] = Array[min_indx], Array[i]
  
print(Array)


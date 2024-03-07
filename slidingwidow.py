# arr=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
# window_size=int(input("Enter the widow size"))
# l1=[]
# for x in range(0,len(arr)-window_size+1):
#     #  print(arr[x:x+window_size])
#      window_sum = sum(arr[x:x+window_size])
#      l1.append(window_sum)
# print(max(l1))

#sliding window
arr=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
window_size=int(input("Enter the window size : "))
maxsum=-999999
csum=0
for i in range(0,window_size):
    csum=csum+arr[i] 
for i in range(window_size,len(arr)):
    csum=csum-arr[i-window_size]+arr[i]
    maxsum=max(maxsum,csum)
print(maxsum)


# str="ABABCABACBCABCABABCABACB"
# patt="ABC"
# for i in range(len(str)-len(patt)+1):
#     num=''
#     for j in range(i,i+len(patt)):
#         num=num+str[j]
#         if(num==patt):
#             print(i)
        
        
    


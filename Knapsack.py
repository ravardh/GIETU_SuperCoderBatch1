def knapSack(W, wt, val, n):
   if n == 0 or W == 0 :
      return 0
  
   if (wt[n-1] > W):
      return knapSack(W, wt, val, n-1)
   
   else:
      return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
         knapSack(W, wt, val, n-1))
   
# data
val = [10,5,15,7,6,18,3]
wt = [2,3,5,7,1,4,1]
W = 15
n = len(val)
print (knapSack(W, wt, val, n))
    

# M = [[0] * (15 + 1) for _ in range(7 + 1)]
# print(M)
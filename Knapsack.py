def knapSack(c,wt,p,n):
    M=[]
    for i in range(n+1):
        row=[]
        for w in range(c+1):
            row.append(0)
        M.append(row)

    for i in range(n+1): 
        for j in range(c+1): 
            if i==0 or j==0: 
                M[i][j]=0
            elif wt[i-1]<=j: 
                M[i][j]=max(p[i-1]+M[i-1][j-wt[i-1]],M[i-1][j]) 
            else: 
                M[i][j]=M[i-1][j] 

    return M[n][c] 
 
profit=[10,5,15,7,6,18,3] 
weight=[2,3,5,7,1,4,7] 
c=15
n=len(profit) 
print(knapSack(c,weight,profit,n)) 


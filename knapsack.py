arr = [['a',4,20], 
              ['b',5,60],
              ['c',6,70],
              ['d',6,65],
              ['e',4,25],
              ['f',2,80],
              ['g',2,10],
              ['h',4,22],
        ]
 
n = len(arr)

for i in range(n):
   for j in range(n-1-i):
     if arr[j][2]<arr[j+1][2]:
       arr[j],arr[j+1]=arr[j+1],arr[j]
       
visited=[False]*max(job[1] for job in arr)

jobs=['-1']*len(visited)

for i in range(len(arr)):
   for j in range(arr[i][1],-1,-1):
       if visited[j-1]==False:
           jobs[j-1]=arr[i][0]
           visited[j-1]=True
           break
print(jobs)
        
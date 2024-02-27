s='ABABCABACBCABCABABCABACB'
pattern='ABC'
n,k=len(s),len(pattern)


# Brute force search every substring TC: O(n*len(pattern))
ct=0
for i in range(n-k):  # O(n)
  if pattern==s[i:i+k]: # O(k)
    ct += 1

print(ct)

# Sliding window
ct=0
temp=s[:k-1]
for i in range(k-1,n):  # O(n)
  temp+=s[i]
  if temp == pattern: # O(k)
    ct += 1
  temp=temp[1:] # O(k)
print(ct)

''' LPS --> Longest Prefix Suffix
PseudoCode

func(s, n, lps)
  l=0
  lps[0]=0
  i=1

  while i<n
    if pat[i]==pat[l]
      l++
      lps[i]=l
      i++
    otherwise
      if l!=0
        l=lps[l-1]
      otherwise
        lps[i]=0
        i++
'''

'''KMP Algorithm
Step 1: Find LPS(pattern)
'''

'''KMP Pseudocode (s, pat)
m=len(pat)
n=len(s)

i=0

while(n-i)>=(m-j):
  if pat[j]==s[i]:
    i++
    j++
  if j==m:
    print("Found Pattern")
    j=lps[j-1]
  elif i<n and pat[j]!=s[i]:
    if j!=0:
      j=lps[j-1]
    else:
      i++

'''

def lps(s, n, lps):
  l=0 # length of current lps
  lps[0]=0  # length of LPS of single character is 0
  i=1 # start from 1 since 1st is already checked

  while i<n:
    if s[i] == s[l]:
      l+=1
      lps[i]=l
      i+=1
    else:
      if l!=0:
        l=lps[l-1]
      else:
        lps[i]=0
        i+=1

def KMPSearch(s, pat):
  m=len(pat)
  n=len(s)

  l = [0]*m
  j = 0 

  lps(pat, m, l)
  i=0

  while(n-i)>=(m-j):
    if pat[j]==s[i]:
      i+=1
      j+=1
    if j==m:
      print("Found pattern at index " + str(i-j))
      j=l[j-1]
    elif i<n and pat[j]!=s[i]:
      if j!=0:
        j=l[j-1]
      else:
        i+=1

# s='ABABABABABAB'
# pat='AB'
# KMPSearch(s,pat)
        
# s='ABCDABCDA'
l=[0]*len(s)
lps(s,len(s),l)
print(*l)

#!/usr/bin/env python
# coding: utf-8

# In[2]:


#KMP Algorithm


def KMPSearch(pat, data):
 M = len(pat)
 N = len(data)

 lps = [0]*M
 j = 0 

 LPS(pat, M, lps)

 i = 0 
 while (N - i) >= (M - j):
  if pat[j] == data[i]:
   i += 1
   j += 1

  if j == M:
   print("Found pattern at index " + str(i-j))
   j = lps[j-1]

  elif i < N and pat[j] != data[i]:
   if j != 0:
    j = lps[j-1]
   else:
    i += 1



def LPS(pat, M, lps):
 len = 0 

 lps[0] = 0 
 i = 1


 while i < M:
  if pat[i] == pat[len]:
   len += 1
   lps[i] = len
   i += 1
  else:
   if len != 0:
    len = lps[len-1]
   else:
    lps[i] = 0
    i += 1


# Driver code
if __name__ == '__main__':
 data = "ABAABABCABABABCAABABCABAC"
 pat = "ABABC"
 KMPSearch(pat, data)


# In[ ]:





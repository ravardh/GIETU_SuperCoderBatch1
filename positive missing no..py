#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=max(nums)
        l=set(nums)
        for i in range(1,n):
            if i not in l:
                return i
            else:l.remove(i)
        return n+1


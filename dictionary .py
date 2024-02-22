#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={1:"devi",2:"guddi"}
print(d)


# In[2]:


d={1:"devi",2:"devidatta"}
for x in d:
    print(x)


# In[3]:


d={1:"devi",2:"devidatta"}
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values():
    print(x)


# In[4]:


d = {1:"devi", 2:"datta"}
print(d)
print(type(d))

d.update({3:"guddi"})
print(d)

for x in d.keys():
    print(x)
for x in d.values():
    print(x)

s = int(input("Enter any key :"))
try:
    print(d[s])
except KeyError:
    print("Key value is not present.")


# In[5]:





# In[6]:





# In[7]:





# In[ ]:





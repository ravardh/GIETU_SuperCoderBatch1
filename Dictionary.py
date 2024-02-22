#!/usr/bin/env python
# coding: utf-8

# In[11]:


d= { 1:"car", 2:"bike", 3:"scooty"}
print(d)
print(type(d))

d.update({4:"scooter"})
print(d)

for x in d:
    print(x)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

s = int(input("Enter any key :"))
try:
    print(d[s])
except:
    print("Key value is not present")
        


# In[ ]:





# In[ ]:





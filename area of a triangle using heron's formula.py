#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
a = 4
b = 16
c = 3
# where 's' is the semi perimeter
s = (a + b + c) / 2
area1 =(s*(s-a)*(s-b)*(s-c))*-1
area =(math.sqrt(area1))
print("the area of a triangle using hero's formula is:" ,round(area, 2))


# In[ ]:





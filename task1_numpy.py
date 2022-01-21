#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


a = np.array([[1,2,3,3,1],
              [6,8,11,10,7]])
a = np.transpose(a)
mean_a = a.mean(axis=0)
mean_a


# In[5]:


a_centered = a - mean_a
a_centered


# In[15]:


b = a_centered[:,0].copy()
c = a_centered[:,1].copy()
a_centered_sp = b@c
a_centered_sp


# In[16]:


unbiased_cov = a_centered_sp / (a.shape[0] - 1)
unbiased_cov


# In[23]:


cov = np.cov(a.T)[0][1]
cov


# In[ ]:





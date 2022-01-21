#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[10]:


authors = {
    "author_id":[1,2,3],
    "author_name":['Тургенев','Чехов','Островский']
}
authors = pd.DataFrame(authors)
authors


# In[11]:


book = {
    "author_id":[1,1,1,2,2,3,3],
    "book_title":['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price":[450, 300, 350, 500, 450, 370, 290]
}
book = pd.DataFrame(book)
book


# In[12]:


authors_price = pd.merge(authors,book,on='author_id',how='inner')
authors_price


# In[13]:


top5 = authors_price.nlargest(5,'price')
top5


# In[14]:


authors_stat = pd.DataFrame({'author_name' : authors_price['author_name'].unique(),
                             'min_price' : authors_price.groupby('author_name', sort=False)['price'].min(),
                             'max_price' : authors_price.groupby('author_name', sort=False)['price'].max(),
                             'mean_price' : authors_price.groupby('author_name', sort=False)['price'].mean()})
authors_stat


# In[15]:


authors_price['cover']=['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price


# In[19]:


book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], 
                           aggfunc=np.sum,fill_value=0)
book_info


# In[21]:


book_info.to_pickle('book_info.pkl')
book_info


# In[22]:


book_info_2=pd.read_pickle('book_info.pkl')
book_info_2


# In[ ]:





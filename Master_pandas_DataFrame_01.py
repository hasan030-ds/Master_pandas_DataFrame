#!/usr/bin/env python
# coding: utf-8

# # pandas

# pandas is a python library used for working with data sets . It has functions for analyzing , cleaning , exploring , and manipulating data
# 

# In[1]:


#pandas installation
get_ipython().system('pip install pandas')


# In[2]:


#import pandas library
import pandas as pd


# DataFrame is one type of data structure we used pandas library to create dataframe 
# 
# DataFrame has many in-build function which we used to do many different opretions on data

# In[4]:


# create simple data frame using list 
L1 = [[1,2,3],[4,5,6],[7,8,9]]


# In[5]:


df = pd.DataFrame(L1)


# In[6]:


df


# In[7]:


# now adding column and row name in data frame 
df = pd.DataFrame(L1 , columns = ['c1','c2','c3'] , index = ['r1','r2','r3'])


# In[8]:


df


# In[13]:


# creating data frame using dictionry
dict = {'NAME':['A','B','C'],'GENDER':['M','F','F']}


# In[14]:


df = pd.DataFrame(dict, index = ['r1','r2','r3'])


# In[15]:


df


# In[16]:


# create dataframe using numpy arrays
import numpy as np


# In[17]:


var = np.arange(0,20).reshape(4,5)


# In[19]:


var


# In[20]:


type(var)


# In[23]:


#now converts this into the form of dataframe
df = pd.DataFrame(var)


# In[22]:


df


# In[24]:


# we can also add cols and rows name if we need 
df = pd.DataFrame(var , columns = ['c1','c2','c3','c4','c5'] , index = ['r1','r2','r3','r4'])


# In[25]:


df


# In[26]:


type(df)


# In[ ]:





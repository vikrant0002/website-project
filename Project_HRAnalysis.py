#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # HR data Analysis 

# In[2]:


df=pd.read_csv("C:\\Users\\admin\\Downloads\\HR_Analytics.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns


# In[7]:


type[df.columns]


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df.isnull()


# In[11]:


df.head()


# In[12]:


type(df)


# In[13]:


df.dtypes


# In[14]:


df.describe()


# In[15]:


df.dtypes


# In[16]:


df[['EmpID','SalarySlab']]


# In[17]:


df.dtypes == 'object'


# In[18]:


df.dtypes[df.dtypes == 'object'].index


# In[19]:


df[df.dtypes[df.dtypes == 'object'].index].describe()


# In[20]:


df.dtypes


# In[21]:


df.dtypes == 'float'


# In[22]:


df[df.dtypes[df.dtypes == 'float'].index]


# In[23]:


df[df.dtypes[df.dtypes == 'int64'].index]


# In[24]:


df.columns


# In[25]:


df[['BusinessTravel','Age']][4:10]


# In[26]:


df['new_col'] = 0


# In[27]:


df


# In[28]:


df["new_col1"] = df['EducationField'] + df['Department']


# In[29]:


df


# In[30]:


pd.Categorical(df['Attrition'])


# In[31]:


df['StockOptionLevel'].unique()


# In[32]:


df.head()


# In[33]:


df[df['Age']>18]


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


#importing your data 
data= pd.read_excel("Call Data April 15th - April 23rd.xlsx")


# In[5]:


#checking out the first 5 rows
data.head()


# In[7]:


#checking out the dataset if there are null values. It looks like there are a lot of them.
pd.isnull(data)


# In[11]:


#dropping all columns that have only null values with the (how="all")- argument
data= data.dropna(axis=1, how="all") 
#much better!


# In[12]:


data.shape


# In[14]:


#let's delete some columns that we don't need using the drop - method
data.drop(columns= ["Title", "Created", "Item Type"], inplace= True)
#you probably noticed that it would be easier to just save your dataframe with the colums needed. Thus, we will do that.


# In[16]:


#We will only need these two columns. The "Created By" column tells us who created the entry, and the "Topic of Phone Call" tells us the reason a student called.
data= data[["Created By", "Topic of Phone Call"]]


# In[25]:


#Typically we would check duplicate values. But in our case we have many duplicates which doesn't affect our analysis
#We need to keep them to see how many calls we received for each department
data.duplicated()


# In[26]:


#make sure to doublecheck if there any other null values in our dataset. In our case we got rid of them all!
data.isnull()


# In[27]:


#To make the analysis easier, we must rename the columns. They include spaces which isn't very good.
data.rename(columns = {"Created By":"CreatedBy", "Topic of Phone Call": "Topic"}, inplace= True)


# In[28]:


#make sure to check that it was indeed renamed.
data.head()
#great! :) 


# In[30]:


#let's sort our dataset by topic, if you don't pass an argument, it will automatically sort in ascending order.
data= data.sort_values(by= "Topic")
#wonderful!


# In[32]:


#let's check how many calls we received for Admissions, the normalize attribute will show us the fraction of the total amount
byDepartment= pd.DataFrame(data.Topic.value_counts(normalize= True))


# In[33]:


#let's take a look at how many calls we received for each department
byDepartment


# In[34]:


byDepartment.plot(kind= "bar")


# In[ ]:


#This was a basic analysis with graph. I hope you can learn something.


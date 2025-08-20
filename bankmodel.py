#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

import warnings
warnings.filterwarnings("ignore")


# In[2]:


data = pd.read_csv("BankNote_Authentication.csv")
data.head()


# In[3]:


df = data.copy()
df.head()


# In[28]:


df[df['class']==1]


# In[26]:


X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X.tail()


# In[5]:


y.head()


# In[7]:


X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2)


# In[8]:


print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[16]:


model = RandomForestClassifier()
model.fit(X_train,y_train)


# In[17]:


y_pred = model.predict(X_test)
score = accuracy_score(y_test,y_pred)
score


# In[19]:


with open("classifier.pkl","wb")as file:
    pickle.dump(model,file)


# In[29]:


model.predict([[-1.3,3.3,-1.39,-1.99]])


# In[ ]:





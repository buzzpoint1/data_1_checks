#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# In[47]:


df = pd.read_csv("~/Desktop/python assignments gitHub/assets/titanic_data.csv")
df.head()


# In[64]:


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=df['Fare'],
                y=df['Age'], data=df,hue='Pclass',palette='Dark2')


# In[ ]:





# In[ ]:





# In[ ]:





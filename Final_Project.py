#!/usr/bin/env python
# coding: utf-8

# In[6]:


from matplotlib import pyplot as plt


# In[14]:


# Comparing GDP and Health in top 5 countries
x = ["Finland","Denmark","Norway","Netherlands","Switzerland"]
y = [1, 2, 3, 4, 5]
z = [22,14,7,15,12]
w = [27, 23,12,13,18]
plt.scatter(x,y,s=150,marker='o')
plt.scatter(x,z,s=150,marker='o')
plt.scatter(x,w,s=150,marker='o')
plt.title("Comparison")
plt.xlabel("Top 5 Countries")
plt.ylabel("Ranking")
plt.legend(["Ladder","Log of GDP per capita","Healthy life expectancy"])
plt.show()


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


# Comparing Freedom and Social Support in top 5 countries
x = ["Finland","Denmark","Norway","Iceland","Netherlands"]
y = [5, 6, 3, 7, 19]
w = [2, 4, 3, 1, 15]
plt.scatter(x,y,s=150,marker='x')
plt.scatter(x,w,s=150,marker='x')
plt.xlabel('Top 5 Countries')
plt.ylabel('Freedom, and Social Support')
plt.title('Freedom, and Social Support in Top 5 Countries')
plt.legend(["Freedom","Social support"])
plt.show()


# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('economic_freedom_index2019_data.csv', encoding="ISO-8859-1")


# In[4]:


df


# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('economic_freedom_index2019_data.csv', encoding="ISO-8859-1")


# In[4]:


df


# In[55]:


# Check the countries that will have a declining GDP Growth rate in the next 5 years
df.loc[(df['5 Year GDP Growth Rate (%)'] < 0)]


# In[4]:


df.shape


# In[5]:


df.ndim


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[9]:


# Check the last 3 countries 
df.tail(3)


# In[11]:


# Analyze Yemen
df[df["Country Name"] == "Yemen"]


# In[12]:


import matplotlib.pyplot as plt


# In[18]:


Yemen = {
    "Property_Rights": 19.6,
    "Judical_Effectiveness": 22.2,
    "Government_Integrity": 20.3,
    "Population_(Millions)":30.0,
    "GDP_(Billions,PPP)": 38.6,
    "GDP_Growth_Rate": -13.8,
    "5_Year_GDP_Growth_Rate": -16.1,
    "GDP_per_Capita": 1287,
    "Unemployment": 14,
    "Inflation": 4.9,
    "FDI_Inflow": -269.9,
    "Public_Debt": 141
    
}
print(Yemen)
    


# In[16]:


from matplotlib.pyplot import *
import matplotlib.pyplot as plt


# In[31]:


x = ['Property Rights','Judicial Effectiveness','Government Integrity','Population(Millions)','GDP(Billions,PPP)','GDP Growth Rate','5 Year GDP Growth Rate','GDP per Capita','Unemployment','Inflation','FDI Inflow','Public Debt']
y = [22.2,20.3,30.0,38.6,-13.8,-16.1,1,287,14.0,4.9,-269.9,141.0]
plt.xticks(rotation=90)
plt.scatter(x,y,s=150,marker='o')
plt.title("Yemen")
plt.xlabel("Category")
plt.ylabel("Score")
plt.show()


# In[33]:


df.sort_values("World Rank", ascending = False).head(5)


# In[34]:


df.sort_values("World Rank", ascending = False, inplace = True)


# In[35]:


df


# In[1]:


import pandas as pd
import os


# In[2]:


df = pd.read_csv('economic_freedom_index2019_data.csv', encoding="ISO-8859-1")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.ndim


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[12]:


import matplotlib.pyplot as plt


# In[18]:


Yemen = {
    "Property_Rights": 19.6,
    "Judical_Effectiveness": 22.2,
    "Government_Integrity": 20.3,
    "Population_(Millions)":30.0,
    "GDP_(Billions,PPP)": 38.6,
    "GDP_Growth_Rate": -13.8,
    "5_Year_GDP_Growth_Rate": -16.1,
    "GDP_per_Capita": 1287,
    "Unemployment": 14,
    "Inflation": 4.9,
    "FDI_Inflow": -269.9,
    "Public_Debt": 141
    
}
print(Yemen)
    


# In[16]:


from matplotlib.pyplot import *
import matplotlib.pyplot as plt


# In[31]:


x = ['Property Rights','Judicial Effectiveness','Government Integrity','Population(Millions)','GDP(Billions,PPP)','GDP Growth Rate','5 Year GDP Growth Rate','GDP per Capita','Unemployment','Inflation','FDI Inflow','Public Debt']
y = [22.2,20.3,30.0,38.6,-13.8,-16.1,1,287,14.0,4.9,-269.9,141.0]
plt.xticks(rotation=90)
plt.scatter(x,y,s=150,marker='o')
plt.title("Yemen")
plt.xlabel("Category")
plt.ylabel("Score")
plt.show()


# In[33]:


df.sort_values("World Rank", ascending = False).head(5)


# In[34]:


df.sort_values("World Rank", ascending = False, inplace = True)


# In[35]:


df


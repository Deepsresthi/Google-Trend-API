#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()


# In[6]:


#top searches in a region
print("Write full name in lowercase")
geoname = input("Geoname: ")
trending_searches_df = pytrend.trending_searches(pn= geoname)
print(trending_searches_df.head(20))


# In[7]:


# Get Google Hot Daily Trends data 
print("Write region name in code (example: IN, US)")
geoname = input("Geoname: ")
today_searches_df = pytrend.today_searches(pn= geoname)
print(today_searches_df.head(20))


# In[8]:


# Get Google Top Charts
print("Write region name in code (example: IN, US)")
geoname = input("Geoname: ")
year = input("year: ")
top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo=geoname)
print(top_charts_df)


# In[9]:


# Get Google Keyword Suggestions
keyword = input("Keyword: ")
suggestions_dict = pytrend.suggestions(keyword= keyword)
print(pd.DataFrame(suggestions_dict).drop('mid', axis=1))


# In[16]:


# Create payload and capture API tokens. Only needed for interest_over_time()
keyword = input("Keyword: ")
pytrend.build_payload(kw_list=[keyword])
 
# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.tail(20))


# In[11]:


# Interest by Region
keyword = input("Keyword: ")
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.sort_values([keyword], ascending=False).head(20))


# In[14]:


#Interest of rising related topics
related_topic = pytrend.related_topics()
keyword = input("Keyword: ")
related_topic[keyword]['rising'].drop(['link','topic_mid'], axis=1).head(20)


# In[15]:


#interest of top related queries
related_topic = pytrend.related_topics()
keyword = input("Keyword: ")
related_topic[keyword]['top'].drop(['link','topic_mid'], axis=1).head(20)


# In[21]:


#interest of rising related queries
related_topic = pytrend.related_queries()
keyword = input("Keyword: ")
related_topic[keyword]['rising'].head(20)


# In[23]:


#interest of top related queries
related_topic = pytrend.related_queries()
keyword = input("Keyword: ")
related_topic[keyword]['top'].head(20)


# In[ ]:





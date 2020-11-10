#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import datetime, date, time, timedelta


# In[ ]:


file_url = "https://www.ag.ch/media/kanton_aargau/themen_1/coronavirus_1/daten_excel/Covid-19-Daten_Kanton_Aargau.xlsx"


# In[5]:


today = date.today()
today = today.strftime("%Y-%m-%d")

todays_weekday = date.today().weekday()
two_days_ago = date.today() - timedelta(days=2)
two_days_ago = two_days_ago.strftime("%Y-%m-%d")


#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install bs4')
get_ipython().system('pip install request')


# In[2]:


import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re 
import requests
import time
from time import sleep


# # Question:2

# In[50]:


driver=webdriver.Chrome()


# In[51]:


driver.get("http://www.bcci.tv/")


# In[ ]:


html(/body/div[5]/div/div[2]/div/div[2]/div/div[1]/div[2]/a)


# In[52]:


vew=driver.find_elements(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/div[1]/div[2]/a')[0].click()


# In[63]:


mor=driver.find_elements(By.XPATH,'//button[@class="match-btn btn-red d-flex align-items-center justify-content-center mx-auto mt-3"]')[0].click()


# In[98]:


title=[]
V=driver.find_elements(By.XPATH,'//div[@class="match-card-middle__inner d-flex justify-content-between"]')
for i in V:
    title.append(i.text.replace('\n'," "))

series=[]

T=driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')

for i in T:
    series.append(i.text)
D=[]
d=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in d:
    D.append(i.text)
    
    
T=[]
t=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in t:
    T.append(i.text)
    
P=[]
p=driver.find_elements(By.XPATH,'//span[@class="ng-binding"]')
for i in p:
    P.append(i.text)
data=({"MATCH_TITLE":title,"SERIES":series,"MATCH_DATE":D,"TIME":T,"PLACE_OF _MATCH":P})
df=pd.DataFrame(data)
df.to_csv("Series2023.csv")


# # Question:5

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get('https:/www.billboard.com/')


# In[ ]:





# In[9]:


page=requests.get('https://www.billboard.com/charts/hot-100/')
##page


# In[10]:


soup=BeautifulSoup(page.content)
#soup


# In[18]:


t=[]
o=driver.find_elements(By.XPATH,'//div[@class="chart-results-list-header // lrv-a-unstyle-list lrv-u-text-align-center lrv-u-background-color-brand-primary lrv-u-color-white lrv-u-flex lrv-u-align-items-center lrv-u-text-transform-uppercase lrv-u-line-height-small u-z-index-4 lrv-u-position-relative"]')

for i in o:
    t.append(i.text.replace('\n'," "))
k=[]
K=driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]')
for i in K:
    k.append(i.text.replace('\n'," ")) 
    
df=pd.DataFrame(k,columns=t)    


# # Question:8

# In[15]:


driver=webdriver.Chrome()


# In[16]:


driver.get('https://archive.ics.uci.edu/')


# In[17]:


button=driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/header/nav/ul/li[1]/a')[0].click()


# In[18]:


#driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[3]/label/select')[0].click()


# In[19]:


driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[3]/label/select/option[5]')[0].click()


# In[20]:


page=requests.get('https://archive.ics.uci.edu/datasets?skip=0&take=25&sort=desc&orderBy=NumHits&search=')
soup=BeautifulSoup(page.content)


# # Question:3

# In[22]:


driver=webdriver.Chrome()


# In[23]:


driver.get("http://statisticstimes.com/")


# In[24]:


driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/button')[0].click()


# In[25]:


driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/a[3]')[0].click()


# In[27]:


driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')[0].click()


# In[35]:


page=requests.get('https://www.statisticstimes.com/economy/india/indian-states-gdp.php')


# In[36]:


soup=BeautifulSoup(page.content)


# In[85]:


mytable1=[]
for i in soup.find_all('tr'):
    for y in i.find_all('th'):
        
              mytable1.append(y.text)
#print(mytable1[0:6])

table=[]
for x in soup.find_all('tr')[4:38]:
    td=x.find_all('td')
    td_val=[y.text for y in td]
    table.append(td_val)
df=pd.DataFrame(table,columns=mytable1[0:8])


# In[86]:


df


# # Question:4

# In[10]:


driver=webdriver.Chrome()


# In[11]:


driver.get(' https://github.com/')


# In[12]:


driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')[0].click()


# In[13]:


d=driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
d[0].click()


# In[73]:


title=[]
data=driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]')
for i in data:
    title.append(i.text)
    
description=[]
data=driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
for i in data:
    description .append(i.text) 
langu=[]
data=driver.find_elements(By.XPATH,'//span[@itemprop="programmingLanguage"]')
for i in data:
    langu.append(i.text)
    


# In[80]:


print(len(title),len(langu),len(description))


# In[123]:


len(r)


# # Question:6

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[6]:


PAGE=requests.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')
PAGE


# In[15]:


soup=BeautifulSoup(PAGE.content)
mytable=soup.find('table',class_="in-article sortable")
#mytable


# In[35]:


rh=[]
for i in mytable.find_all('tr'):
    for y in i.find_all('th'):
        rh.append(y.text.replace('\n',""))
    
table=[]
for x in mytable.find_all('tr')[2:]:
    td_teg=x.find_all('td')
    td_val=[y.text for y in td_teg]
    table.append(td_val)
df= pd.DataFrame(table,columns=rh)        
  


# # Question:7

# In[47]:


driver=webdriver.Chrome()


# In[ ]:





# In[48]:


driver.get('https://www.imdb.com/list/ls095964455/')


# In[66]:


h=[]
data=driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]')
for i in data:
    h.append(i.text)
u=[]
data=driver.find_elements(By.XPATH,'//span[@class="genre"]')
for i in data:
    u.append(i.text)
y=[]
data=driver.find_elements(By.XPATH,'//span[@class="runtime"]')
for i in data:
    y.append(i.text) 
R=[]
data=driver.find_elements(By.XPATH,'//div[@class="ipl-rating-widget"]')
for i in data:
    R.append(i.text.replace('\n',""))  
    
VOte=[]
data=driver.find_elements(By.XPATH,'//span[@name="nv"]')
for i in data:
    VOte.append(i.text)    
data=({"NAME_YEAR_SPAN":h,"Genre":u,"RUN_TIME":y,"RATING":R,"VOTE":VOte})
df=pd.DataFrame(data)    


# # Question:1

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[8]:


page=requests.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
page


# In[9]:


soup=BeautifulSoup(page.content)


# In[40]:


Header=[]
for i in soup.find_all('tr'):
    for y in i.find_all('th'):
        Header.append(y.text.replace('\n',""))
header=Header[0:6] 
table=[]
for x in soup.find_all('tr')[2:33]:
    td_teg=x.find_all('td')
    td_val=[y.text for y in td_teg]
    table.append(td_val)
df= pd.DataFrame(table,columns=header)
df.iloc[:-1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





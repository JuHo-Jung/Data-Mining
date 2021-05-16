#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver


# In[3]:


driver = webdriver.Chrome('chromedriver')


# In[4]:


url = "http://factcheck.snu.ac.kr/"
driver.get(url)


# In[5]:


btn = driver.find_element_by_xpath('/html/body/div[5]/div[2]/label')
btn.click()  #팝업창1번 삭제


# In[6]:


btn1 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/label')
btn1.click()   #팝업창2번 삭제


# In[7]:


input_ = driver.find_element_by_xpath('//*[@id="gnb"]/div/div/form/fieldset/input')
input_


# In[8]:


input_.send_keys('코로나')   #검색어 "코로나"입력하기 


# In[9]:


btn3= driver.find_element_by_xpath('//*[@id="gnb"]/div/div/form/fieldset/button')
btn3.click()


# In[10]:


pages_url = driver.find_elements_by_xpath('//*[@id="container"]/div/div[3]/div/ul/li/div/div[1]/div[3]/p[1]/a')
len(pages_url)


# In[11]:


##### url 한개씩 가져오기
brief_url = []
for page in pages_url:
    brief_url.append(page.get_attribute('href'))
print(len(brief_url), brief_url[0])


# In[12]:


brief_url


# In[13]:


page_2 = driver.find_element_by_xpath('//*[@id="pagination"]/div/a[4]')
page_2.click()


# In[14]:


pages_url = driver.find_elements_by_xpath('//*[@id="container"]/div/div[3]/div/ul/li/div/div[1]/div[3]/p[1]/a')
len(pages_url)


# In[15]:


for page in pages_url:
    brief_url.append(page.get_attribute('href'))
print(len(brief_url))


# In[16]:


brief_url


# In[17]:


page_3 = driver.find_element_by_xpath('//*[@id="pagination"]/div/a[5]')
page_3.click()


# In[18]:


pages_url = driver.find_elements_by_xpath('//*[@id="container"]/div/div[3]/div/ul/li/div/div[1]/div[3]/p[1]/a')
len(pages_url)


# In[19]:


for page in pages_url:
    brief_url.append(page.get_attribute('href'))
print(len(brief_url))


# In[20]:


brief_url


# In[21]:


print(brief_url[0])


# In[22]:


print(brief_url[1])


# In[23]:


# Text 가져오는 함수
def ele_to_text(url):
    driver.get(url)
    
    category = driver.find_element_by_xpath('//*[@id="content_detail"]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li[2]')
    speaker = driver.find_element_by_xpath('//*[@id="content_detail"]/div/div[3]/div[1]/div/div[1]/p')
    title = driver.find_element_by_xpath('//*[@id="content_detail"]/div/div[3]/div[1]/div/div[2]/div[1]/p[1]/a')
    source = driver.find_element_by_xpath('//*[@id="content_detail"]/div/div[3]/div[1]/div/div[2]/div[1]/p[2]')
    veracity = driver.find_element_by_class_name('meter-label')
    
    return { 
        'category': category.text,
        'speaker': speaker.text,
        'title': title.text,
        'source': source.text,
        'veracity': veracity.text
    }


# In[24]:


# url text 가져오기
from tqdm import tqdm
import time

brief_data = []
for url in tqdm(brief_url):
    if url is not None: 
        #driver.get(url)
        data = ele_to_text(url)
        brief_data.append(data)
        time.sleep(5)


# In[25]:


brief_data


# In[26]:


import pandas as pd
df = pd.DataFrame(brief_data)
df.to_csv('covid-19-brief.csv')


# In[27]:


df.info()


# In[28]:


df.head()


# In[ ]:





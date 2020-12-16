#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


# In[11]:


completed = pd.read_csv("completed.csv")
completed.shape


# In[12]:


incomplete = pd.read_csv("links.csv")
incomplete.shape


# In[13]:


com_links = completed.links.to_list()
incom_links = incomplete.links.to_list()


# In[14]:


common = set(com_links).intersection(set(incom_links))


# In[15]:


if len(common)>0:
    incom_links = list(set(incom_links)-common)


# In[16]:


len(incom_links)


# In[17]:


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def start(self,user_link):
        bot = self.bot
        bot.get(user_link)
        time.sleep(3)
        try:
            all_links =[]
            for i in range(0,1):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(4)
                posts = bot.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
                links =[post.find_element_by_css_selector('a').get_attribute('href') for post in posts]
                for link in links:
                    all_links.append(link)

            all_links = list(set(all_links))
            if len(all_links)>5:
                all_links = all_links[:5]
            print(len(all_links))

            for link in all_links:
                bot.get(link)
                try:
                    bot.find_elements_by_class_name('QBdPU')[1].click()
                    time.sleep(2)

                except Exception as ex:
                    print(ex)
                    time.sleep(10)
        except Exception as ex:
            print(ex)


# In[23]:


usernmae,password ='',''
ins = Instagram(usernmae,password)
ins.login()
try:
    while len(incom_links)>0:
        link = incom_links.pop()
        ins.start(link)
        com_links.append(link)
        print(len(com_links),len(incom_links))
except:
    print("Error occured")


# In[9]:


if os.path.exists("links.csv"):
    os.remove("links.csv")
if os.path.exists("completed.csv"):
    os.remove("completed.csv")
completed = pd.DataFrame({"links":com_links})
incomplete = pd.DataFrame({"links":incom_links})
completed.to_csv("completed.csv",index=False)
incomplete.to_csv("links.csv",index=False)


# In[25]:


incomplete.shape


# In[ ]:




